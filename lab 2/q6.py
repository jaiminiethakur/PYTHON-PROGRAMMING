def count_digits(n):
    s = str(n)
    if s[0] == '-':
        print(len(s) - 1)
    else:
        print(len(s))