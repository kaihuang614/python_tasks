import sys
import pygame
from time import sleep
from random import randint

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameState
from button import Button
from scoreboard import Scoreboard
from star import Star


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self) -> None:
        """初始化游戏"""
        pygame.init()
        self.settings = Settings()
        self.bg_color = self.settings.backgroundColor
        # 全屏显示
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #定长显示
        self.screen = pygame.display.set_mode((1500, 800))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # 定制化显示
        # self.screen = pygame.display.set_mode(
        #     (self.settings.screen_width, self.settings.screen_height))  # 返回一个 surface 对象
        # 游戏命名
        pygame.display.set_caption("Alien Invasion")
        # 显示背景星星
        self.stars = pygame.sprite.Group()
        self._create_starry()
        self.starry()
        self.background = pygame.image.load("resource/image/starry_sky.png")
        self.screen.blit(self.background, (0, 0))
        # 飞船图形
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        # 外星人图形
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # 创建一个用于存储游戏统计信息的实例
        self.stats = GameState(self)
        # 创建计分板
        self.score_board = Scoreboard(self)
        # 绘制Play按钮
        self.play_button = Button(self, 'Play')



    def run_game(self):
        """游戏启动！"""
        """游戏主循环"""

        while True:
            # 监控按键
            self._check_events()
            if self.stats.game_active:
                # 更新飞船
                self.ship.update()
                # 更新子弹
                self._update_bullets()
                # 更新外星人
                self._update_aliens()
            # 循环每次重绘屏幕
            self._update_screen()

    def _check_aliens_bottom(self):
        """检查外星人到达是否到达底部"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # 类似飞船被撞
                self._ship_hit()
                break

    def _ship_hit(self):
        """响应飞船被敌人撞到"""
        if self.stats.ships_left > 0:
            # 更新飞船生命值
            self.stats.ships_left -= 1
            self.score_board.prep_ships()
            # 清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()
            # 创建一群新的外星人，新建飞船
            self._create_fleet()
            self.ship.center_ship()

            # 显示鼠标
            pygame.mouse.set_visible(True)
            # 暂停
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _check_fleet_edges(self):
        """当有外星人达到边缘是采取设施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将整群外星人下移,并改变方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        # 对编组调用方法update,会自动调用alien方法update
        self._check_fleet_edges()
        self.aliens.update()

        # 检测外星人和飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # 检查外星人是否到达屏幕底部
        self._check_aliens_bottom()

    def _create_fleet(self):
        """创建外星人"""
        # 创建外星人群
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        # 计算容纳多少行外星人
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (10 * alien_height)-ship_height)
        number_rows = available_space_y // (2*alien_height)
        # 创建第外星人群
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                # 创建一个外星人并加入队列
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """创建一个外星人"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2*alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_bullets(self):
        """更新子弹位置和删除消失的子弹"""
        # 更新子弹位置
        self.bullets.update()
        # 删除消失的子弹
        for bullet in self.bullets.copy():
            # 超出屏幕上方 删除
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            # 超出屏幕右方 删除 
            elif bullet.rect.right >= self.settings.screen_width :
                self.bullets.remove(bullet)
        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        """检查子弹是否击中了外星人"""
        # 击中了就删去子弹和外星人
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
                self.score_board.prep_score()
                self.score_board.check_high_score()

        # 外星人被清空
        if not self.aliens:
            # 删除现有子弹并新建敌人
            self.bullets.empty()
            self._create_fleet()
            # 提升难度
            self.settings.increase_speed()
            # 提高等级
            self.stats.level += 1
            self.score_board.prep_level()

    def _check_events(self):
        """响应键盘、鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        """键盘按下"""
        if event.key == pygame.K_RIGHT:
            # 向右移动飞船
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # 向左移动飞船
            self.ship.moving_left = True
        elif event.key ==  pygame.K_UP:
            # 向上移动飞船
            self.ship.moving_up = True
        elif event.key ==  pygame.K_DOWN:
            # 向上移动飞船
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            #退出前更新最高分
            self.update_score()
            # 按Q退出 英文输入法
            sys.exit()
        elif event.key == pygame.K_SPACE:
            # 空格开火
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """键盘松开"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        

    def _fire_bullet(self):
        """创建子弹,并发射"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):

        # 绘制屏幕颜色 只接受一个实参 ColorValue
        # self.screen.fill(self.settings.backgroundColor)
        self.screen.blit(self.background, (0, 0))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # 显示分数
        self.score_board.show_score()
        # 如果游戏存于非活动状态,就绘制Play按钮
        if not self.stats.game_active:
            self.play_button.draw_button()

        # 这个一定要放最后
        # ?显示 绘制屏幕/更新屏幕
        
        pygame.display.flip()



    def update_score(self):
        """ 更新最高得分 """
        filename = 'high_score.txt'
        # 取当前的最大值
        highScore = self.stats.high_score
        with open(filename,'w+') as file_object:
            # for score in file_object:
            #     self.highestScore = int(score)
            if highScore > self.stats.highestScore:
                file_object.write(str(highScore))


    def _check_play_button(self, mouse_pos):
        """玩家单击Play按钮是开始游戏"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # 重置游戏设置
            self.settings.initialize_dynamic_settings()

            # 重置游戏信息
            self.stats.reset_stats()
            self.stats.game_active = True
            self.score_board.prep_score()
            self.score_board.prep_level()
            self.score_board.prep_ships()

            # 清空余下的外星人
            self.aliens.empty()
            self.bullets.empty()

            # 创建一群新的外星人，并让飞船居中
            self._create_fleet()
            self.ship.center_ship()

            # 隐藏鼠标
            pygame.mouse.set_visible(False)


    def _create_starry(self):
        """ 创建星群 """
        # 创建一个星星并计算一行可容纳多少个星星
        star = Star(self)
        star_width, star_height = star.rect.size
        # 屏幕x方向左右各预留一个星星宽度
        self.availiable_space_x = self.screen.get_rect().width - (2 * star_width)
        # 星星的间距为星星宽度的3倍
        number_stars_x = self.availiable_space_x // (4 * star_width) + 1

        # 计算屏幕可容纳多少行星星
        # 屏幕y方向上下各预留一个星星宽度
        self.availiable_space_y = self.screen.get_rect().height - (2 * star_height)
        # 星星的间距为星星高度的3倍
        number_rows = self.availiable_space_y // (4 * star_height) + 1

        # 创建星群
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        # 创建一个星星并将其加入到当前行
        star = Star(self)
        star.rect.x = randint(0, self.availiable_space_x)
        star.rect.y = randint(0, self.availiable_space_y)
        self.stars.add(star)

    def starry(self):
        """ 开始星空展示 """
        # 每次循环时都重绘屏幕
        self.screen.fill(self.bg_color)

        self.stars.draw(self.screen)

        # 让最近绘制的屏幕可见
        pygame.display.flip()

        #保存为图像文件
        pygame.image.save(self.screen, 'resource/image/starry_sky.png')
if __name__ == "__main__":
    # 创建游戏实例并启动
    ai = AlienInvasion()
    ai.run_game()
