def to_lower(s):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':
            result = result + chr(ord(char) + 32)
        else:
            result = result + char
    return result

def to_upper(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result = result + chr(ord(char) - 32)
        else:
            result = result + char
    return result

def toggle_case(s):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':
            result = result + chr(ord(char) + 32)
        elif 'a' <= char <= 'z':
            result = result + chr(ord(char) - 32)
        else:
            result = result + char
    return result