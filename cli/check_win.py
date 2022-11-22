def check_win():
    """
    Checking OS, if Windows need to use asyncio Fix
    """
    import sys
    return sys.platform == 'win32'
