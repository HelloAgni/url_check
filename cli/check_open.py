def url_reader():
    """
    Auto import urls from file.txt -> in active CLI
    """
    try:
        import pathlib
        import sys
        current_root = pathlib.Path(__file__).parent
        sys.path.append(str(current_root) + '/urls.txt')
        with open(sys.path[-1], 'r') as file:
            return [line.rstrip() for line in file]
    except FileNotFoundError as e:
        print(e)
