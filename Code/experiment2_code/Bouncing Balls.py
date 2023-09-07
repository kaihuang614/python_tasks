```python
def bouncing_ball(h, bounce, window):
    res = -1
    if (bounce > 0 and bounce < 1):
        while (h > 0 and window < h):
            res += 2 
            h *= bounce
    return res
```