def shorten_number(suffixes, base):
    def filter(text):
        try:
            num = int(text)
        except (ValueError, TypeError):
            return str(text)

        i = 0
        while num > base:
            if i == len(suffixes) - 1:
                break
            num = num / base
            i += 1

        return str(int(num)) + suffixes[i]

    return filter