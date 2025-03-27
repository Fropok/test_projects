from utils.http_methods import HttpMethods

url_base = 'https://rahulshettyacademy.com'  # базовый url для всех запросов
key = '?key=qaclick123'  # базовый параметр для всех запросов


class GoogleMapsApi:
    '''HTTP запросы'''

    @staticmethod
    def post_location():
        '''POST запрос для создания локации'''
        resource_post = '/maps/api/place/add/json'
        body_post = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        url_post = f'{url_base}{resource_post}{key}'
        print(url_post)

        result_post = HttpMethods.post(url_post, body_post)
        print(result_post.text)
        return result_post  # возвращает результат запроса POST

    @staticmethod
    def get_location(place_id):
        '''GET запрос для проверки существования локации'''
        resource_get = '/maps/api/place/get/json'
        url_get = f'{url_base}{resource_get}{key}&place_id={place_id}'
        print(url_get)

        result_get = HttpMethods.get(url_get)
        print(result_get.text)
        return result_get  # возвращает результат запроса GET

    @staticmethod
    def put_location(place_id):
        '''PUT запрос для изменения локации'''
        resource_put = '/maps/api/place/update/json'
        body_put = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        url_put = f'{url_base}{resource_put}{key}'
        print(url_put)

        result_put = HttpMethods.put(url_put, body_put)
        print(result_put.text)
        return result_put  # возвращает результат запроса PUT

    @staticmethod
    def delete_location(place_id):
        '''DELETE запрос для удаления локации'''
        resource_delete = '/maps/api/place/delete/json'
        body_delete = {
            "place_id": place_id
        }
        url_delete = f'{url_base}{resource_delete}{key}'
        print(url_delete)

        result_delete = HttpMethods.delete(url_delete, body_delete)
        print(result_delete.text)
        return result_delete  # возвращает результат запроса DELETE
