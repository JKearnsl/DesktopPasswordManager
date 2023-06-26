
def is_ascii(string):
    try:
        string.encode(encoding='ascii')
        return True
    except UnicodeEncodeError:
        return False
