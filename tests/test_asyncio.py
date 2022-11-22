import types
import pytest


def test_asyncio_exists():
    """
    Проверка наличия функций new_asyncio
    """
    from cli import cli_asyncio
    assert isinstance(cli_asyncio.str_is_url, types.FunctionType), (
        f'{cli_asyncio.str_is_url.__name__} должна быть функцией'
    )
    assert isinstance(cli_asyncio.check_url, types.FunctionType), (
        f'{cli_asyncio.check_url.__name__} должна быть функцией'
    )
    assert isinstance(cli_asyncio.async_execute, types.FunctionType), (
        f'{cli_asyncio.async_execute.__name__} должна быть функцией'
    )
    assert isinstance(cli_asyncio.main, types.FunctionType), (
        f'{cli_asyncio.main.__name__} должна быть функцией'
    )


@pytest.mark.asyncio
async def test_async_execute():
    """
    Проверка async_execute возвращает корректный тип данных
    """
    from cli import cli_asyncio
    result = {}
    n_strings = ['https://www.google.com', 'https://httpbin.org/post']
    cor = await cli_asyncio.async_execute(result=result, n_strings=n_strings)
    name = cli_asyncio.async_execute.__name__  # func.__qualname__
    assert isinstance(cor, dict), (
        f'Проверьте, что функция {name} возвращает словарь'
    )


@pytest.mark.asyncio
async def test_asyncio_check_url():
    """
    Проверка asyncio.check_url возвращает корректный тип данных
    """
    from cli import cli_asyncio
    result = {}
    n_strings = 'https://www.google.com'
    cor = await cli_asyncio.check_url(n_strings=n_strings, result=result)
    name = cli_asyncio.check_url.__name__
    # assert type(result.cr_frame.f_locals) == dict
    assert isinstance(cor, dict), (
        f'Проверьте, что функция {name} возвращает словарь'
    )


def test_asyncio_str_is_url():
    """
    Проверка asyncio.str_is_url возвращает корректный тип данных
    """
    from cli import cli_asyncio
    line = 'https://www.google.com'
    result = cli_asyncio.str_is_url(line=line)
    name = cli_asyncio.str_is_url.__name__
    assert isinstance(result, str), (
        f'Проверьте, что функция {name} возвращает строку'
    )


def test_msg_asyncio_str_is_url(capfd):
    """
    Проверка вывода сообщения функции asyncio.str_is_url
    """
    from cli import cli_asyncio, msg
    line = ''
    cli_asyncio.str_is_url(line=line)
    correct = msg.msg_2(line=line)
    name = cli_asyncio.str_is_url.__name__
    out, err = capfd.readouterr()
    assert out.replace('\n', '') == correct.replace('\n', ''), (
        f'Проверьте, что функция {name} сообщает что ссылка не корректная'
    )


def test_asyncio_main(capsys):
    """
    Проверка вывода сообщений asyncio_main
    """
    from cli import cli_asyncio
    from cli import msg
    import io
    import sys
    sys.stdin = io.StringIO('stop\n')
    cli_asyncio.main()
    out, err = capsys.readouterr()
    h = msg.msg_1()
    x = '\n'.join(h) + '\n'
    assert err == ''
    assert out == x
