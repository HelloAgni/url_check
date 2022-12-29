from cli import check_win, msg, check_open


def test_files():
    """
    Проверка наличия файлов
    """
    try:
        from cli import cli_asyncio, cli_threading, msg, check_win
    except ImportError as e:
        assert False, f'Не найден файл {e}'
    # try:
    #     from cli import check_win
    # except ModuleNotFoundError:
    #     assert False, f'Не найден файл {check_win.__name__}'


def test_check_win():
    """
    Функция проверки OS возвращает корректный тип данных
    """
    win = check_win.check_win()
    name = check_win.check_win.__name__
    assert isinstance(win, bool), (
        f'Проверьте, что функция {name}'
        f' возвращает логический тип данных'
    )


def test_msg():
    """
    Сообщения возвращают корректный тип данных
    """
    line = 'https://www.google.com'
    n_strings = ['https://www.google.com', 'https://httpbin.org/post']
    assert type(msg.msg_1()) == list, (
        f'Функция {msg.msg_1.__name__} должна возвращать список'
    )
    assert type(msg.msg_2(line)) == str, (
        f'Функция {msg.msg_2.__name__} должна возвращать строку'
    )
    assert type(msg.msg_3(line, n_strings)) == str, (
        f'Функция {msg.msg_3.__name__} должна возвращать строку'
    )


def test_check_open():
    """
    Функция check_open возвращает корректный тип данных
    """
    result = check_open.url_reader()
    assert isinstance(result, list)
