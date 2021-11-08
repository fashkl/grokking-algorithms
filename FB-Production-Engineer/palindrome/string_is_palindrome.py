def palindrome(wr):
    if len(wr) == 0:
        return False

    left = 0
    right = len(wr) - 1
    while left < right:
        if wr[left] != wr[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == '__main__':
    print(palindrome('anana'))
