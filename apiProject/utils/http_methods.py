import allure
import requests
from utils.logger import Logger


class HttpMethods:
    '''Методы HTTP запроса'''

    headers = {'Content-Type': 'applications/json'}
    cookie = ''

    @staticmethod
    def get(url):
        with allure.step('GET'):
            Logger.log_request(url, method='GET')
            result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.log_response(result)
            return result

    @staticmethod
    def post(url, body):
        with allure.step('POST'):
            Logger.log_request(url, method='POST')
            result = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.log_response(result)
            return result

    @staticmethod
    def put(url, body):
        with allure.step('PUT'):
            Logger.log_request(url, method='PUT')
            result = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.log_response(result)
            return result

    @staticmethod
    def delete(url, body):
        with allure.step('DELETE'):
            Logger.log_request(url, method='DELETE')
            result = requests.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.log_response(result)
            return result
