def decode_bits(bits):
    # 去除开头和结尾的0
    bits = bits.strip("0")
    
    # 计算最小单位的长度
    unit = 0
    for bit in bits:
        if bit != "0":
            unit += 1
        else:
            break
    
    count = 1
    for i in range(1, len(bits)):
        if bits[i] == bits[i-1]:
            count += 1
        else:
            # 如果当前的连续计数小于最小单位长度，则更新最小单位长度
            if count < unit:
                unit = count
                count = 1
            else:
                count = 1
    
    morse_code = ""
    
    # 按照单词分割
    words = bits.split("0" * 7 * unit)
    for word in words:
        # 按照字符分割
        characters = word.split("0" * 3 * unit)
        for character in characters:
            # 按照最小单位长度分割
            signs = character.split("0" * unit)
            for sign in signs:
                if sign == "1" * 3 * unit:
                    morse_code += "-"
                else:
                    morse_code += "."
            morse_code += " "
        morse_code += "   "
    
    return morse_code


def decode_morse(morseCode):
    # 去除开头和结尾的空格
    morseCode.strip()
    
    result = ""
    characters = morseCode.split(" ")
    for character in characters:
        if character != "":
            result += MORSE_CODE[character]
        else:
            result += " "
    
    return ' '.join(result.split())