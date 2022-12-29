import io
import sys
import types

from cli import cli_threading, msg


def test_threading_exists():
    """
    Проверка наличия функций new_threading
    """
    assert isinstance(cli_threading.str_is_url, types.FunctionType), (
        f'{cli_threading.str_is_url.__name__} должна быть функцией'
    )
    assert isinstance(cli_threading.check_url, types.FunctionType), (
        f'{cli_threading.check_url.__name__} должна быть функцией'
    )
    assert isinstance(cli_threading.thread, types.FunctionType), (
        f'{cli_threading.async_execute.__name__} должна быть функцией'
    )
    assert isinstance(cli_threading.main, types.FunctionType), (
        f'{cli_threading.main.__name__} должна быть функцией'
    )


def test_threading_str_is_url():
    """
    Проверка threading.str_is_url возвращает корректный тип данных
    """
    line = 'https://www.google.com'
    result = cli_threading.str_is_url(line=line)
    name = cli_threading.str_is_url.__name__
    assert isinstance(result, str), (
        f'Проверьте, что функция {name} возвращает строку'
    )


def test_msg_threading_str_is_url(capfd):
    """
    Проверка вывода сообщения функции threading.str_is_url
    """
    line = ''
    cli_threading.str_is_url(line=line)
    correct = msg.msg_2(line=line)
    name = cli_threading.str_is_url.__name__
    out, err = capfd.readouterr()
    assert out.replace('\n', '') == correct.replace('\n', ''), (
        f'Проверьте, что функция {name} сообщает что ссылка не корректная'
    )


def test_threading_check_url():
    """
    Проверка threading.check_url возвращает корректный тип данных
    """
    result = {}
    n_strings = 'https://www.google.com'
    res = cli_threading.check_url(n_strings=n_strings, result=result)
    name = cli_threading.check_url.__name__
    assert isinstance(res, dict), (
        f'Проверьте, что функция {name} возвращает словарь'
    )


def test_thread():
    """
    Проверка thread возвращает корректный тип данных
    """
    result = {}
    n_strings = ['https://www.google.com', 'https://httpbin.org/post']
    res = cli_threading.thread(result=result, n_strings=n_strings)
    name = cli_threading.thread.__name__  # func.__qualname__
    assert isinstance(res, tuple), (
        f'Проверьте, что функция {name} возвращает кортеж'
    )


def test_threading_main(capsys):
    """
    Проверка вывода сообщений threading_main
    """
    sys.stdin = io.StringIO('stop\n')
    cli_threading.main()
    out, err = capsys.readouterr()
    h = msg.msg_1()
    x = '\n'.join(h) + '\n'
    assert err == ''
    assert out == x
