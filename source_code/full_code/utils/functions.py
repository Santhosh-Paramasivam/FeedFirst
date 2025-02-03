def is_integer(s) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False
