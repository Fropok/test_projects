import requests
from utils.logger import Logger


class HttpMethods:
    '''Кастомные методы HTTP запроса'''
    headers = {"Content-Type": "application/json"}
    cookies = ''

    @staticmethod
    def get(url):
        Logger.log_request(url, method="GET")
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookies)
        Logger.log_response(result)
        return result

    @staticmethod
    def post(url, body):
        Logger.log_request(url, method="POST")
        result = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookies)
        Logger.log_response(result)
        return result

    @staticmethod
    def put(url, body):
        Logger.log_request(url, method="PUT")
        result = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookies)
        Logger.log_response(result)
        return result

    @staticmethod
    def delete(url, body):
        Logger.log_request(url, method="DELETE")
        result = requests.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookies)
        Logger.log_response(result)
        return result
