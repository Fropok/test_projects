import datetime
import os


class Logger:
    '''Запись логов'''

    file_log = f'logs/log_{datetime.datetime.now():%Y-%m-%d_%H-%M-%S}.log'

    @classmethod
    def log_add_file(cls, data=''):
        '''Запись логов в файл'''

        try:
            with open(cls.file_log, 'a', encoding='utf-8') as file:
                file.write(data)
        except Exception as e:
            print(f'ОШИБКА! При записи лога, файл: {e}')

    @classmethod
    def log_request(cls, url, method=''):
        '''Запись запросов'''

        data = (
            '\n-----\n'
            f'Test: {os.environ.get('PYTEST_CURRENT_TEST', 'Неизвестный тест')}\n' # имя теста
            f'Time: {datetime.datetime.now()}\n'
            f'Request method: {method}\n'
            f'Request URL: {url}\n'
            '\n'
        )

        cls.log_add_file(data)

    @classmethod
    def log_response(cls, result):
        '''Запись ответов'''

        data = (
            f'Response code: {result.status_code}\n'
            f'Response text: {result.text}\n'
            f'Response headers: {dict(result.headers)}\n'
            f'Response cookies: {dict(result.cookies)}\n'
            '\n-----\n'
        )

        cls.log_add_file(data)
