import requests
from utils.logger import Logger
from utils.constants import HEADERS, COOKIES


class HttpMethods:
    '''Кастомные методы HTTP запроса'''

    @staticmethod
    def get(url):
        Logger.log_request(url, method="GET")
        result = requests.get(url, headers=HEADERS, cookies=COOKIES)
        Logger.log_response(result)
        return result

    @staticmethod
    def post(url, body):
        Logger.log_request(url, method="POST")
        result = requests.post(url, json=body, headers=HEADERS, cookies=COOKIES)
        Logger.log_response(result)
        return result

    @staticmethod
    def put(url, body=None):
        Logger.log_request(url, method="PUT")
        result = requests.put(url, json=body, headers=HEADERS, cookies=COOKIES)
        Logger.log_response(result)
        return result

    @staticmethod
    def delete(url, body=None):
        Logger.log_request(url, method="DELETE")
        result = requests.delete(url, json=body, headers=HEADERS, cookies=COOKIES)
        Logger.log_response(result)
        return result
