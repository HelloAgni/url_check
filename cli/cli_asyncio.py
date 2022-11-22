import asyncio
import json
import re
import sys
import time

import aiohttp
from check_win import check_win
from msg import msg_1, msg_2, msg_3


def str_is_url(line: str):
    regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if re.match(regex, line):
        return line
    else:
        print(msg_2(line=line))


async def check_url(n_strings: str, result: dict):
    async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=3)) as session:
        http_methods = [
            session.get, session.post,
            session.delete, session.put,
            session.patch, session.options
            ]
        in_result = {}
        try:
            for method in http_methods:
                response = await method(
                    url=n_strings, allow_redirects=False, timeout=3)
                method_key = response.method
                method_status = response.status
                if method_status != 405:
                    in_result[str(method_key)] = method_status
            result[n_strings] = in_result
        except Exception as e:
            print(e)
        return result


async def async_execute(result: dict, n_strings: list):
    tasks = [asyncio.ensure_future(
        check_url(n_strings[i], result)) for i in range(len(n_strings))]
    await asyncio.wait(tasks)
    return result


def main():
    result = {}
    print(*msg_1(), sep='\n')
    n_strings = []
    while True:
        line = sys.stdin.readline().rstrip()
        if line == 'start' and n_strings:
            print('Проверка запущена...')
            start_time = time.time()
            if check_win() is True:
                asyncio.set_event_loop_policy(
                    asyncio.WindowsSelectorEventLoopPolicy())
            answer = asyncio.run(async_execute(result, n_strings))
            print(json.dumps(answer, indent=4))
            end_time = time.time()
            run_time = end_time - start_time
            print(f'Время выполнения: {run_time:.7}c.')
        elif line == 'stop':
            break
        elif str_is_url(line):
            if line not in n_strings:
                n_strings.append(line)
            else:
                print(msg_3(line=line, n_strings=n_strings))


if __name__ == '__main__':
    main()
