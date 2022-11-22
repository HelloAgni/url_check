import json
import re
import sys
import threading
import time

import requests
from msg import msg_1, msg_2, msg_3

requests_session = requests.Session()
HTTP_METHODS = [
    requests_session.get, requests_session.post,
    requests_session.delete, requests_session.put,
    requests_session.patch, requests_session.options
    ]


def str_is_url(line):
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


def check_url(n_strings, result):
    # http_methods = [
    #     req_session.get, req_session.post,
    #     req_session.delete, req_session.put,
    #     req_session.patch, req_session.options
    #     ]
    in_result = {}
    try:
        for method in HTTP_METHODS:
            response = method(url=n_strings, allow_redirects=False, timeout=3)
            method_key = (response.request).method
            method_status = response.status_code
            if method_status != 405:
                in_result[str(method_key)] = method_status
        result[n_strings] = in_result
    except Exception as e:
        print(e)
    return result


def thread(n_strings, result):
    tasks = []
    for i in range(len(n_strings)):
        tasks.append(threading.Thread(
            target=check_url, args=(n_strings[i], result)))
    for t in tasks:
        t.start()
    for t in tasks:
        t.join()
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
            thread(n_strings, result)
            print(json.dumps(result, indent=4))
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
