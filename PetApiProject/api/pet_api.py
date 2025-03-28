from utils.http_methods import HttpMethods


class PetApi:
    '''HTTP запросы для добавления, обновления, удаления питомца'''
    base_url = 'https://petstore.swagger.io/v2'

    @staticmethod
    def post_pet(pet_id, **kwargs):
        '''Добавить нового питомца'''
        print("\nPOST запрос для добавления нового питомца")

        resource_post = '/pet'
        default_body = {
            "id": pet_id,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": "doggie",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }
        body_post = {**default_body, **kwargs}

        url_post = f'{PetApi.base_url}{resource_post}'
        print(url_post)

        result_post = HttpMethods.post(url_post, body_post)
        print(result_post.text)
        return result_post

    @staticmethod
    def get_pet(pet_id):
        '''Найти питомца по ID'''
        print("\nGET запрос для поиска питомца по ID")

        resource_get = f'/pet/{pet_id}'

        url_get = f'{PetApi.base_url}{resource_get}'
        print(url_get)

        result_get = HttpMethods.get(url_get)
        print(result_get.text)
        return result_get

    @staticmethod
    def put_pet(pet_id, **kwargs):
        '''Обновить существующего питомца'''
        print("\nPUT запрос для обновления существующего питомца")

        resource_put = '/pet'
        default_body = {
            "id": pet_id,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": "doggie",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }
        body_put = {**default_body, **kwargs}

        url_put = f'{PetApi.base_url}{resource_put}'
        print(url_put)

        result_put = HttpMethods.put(url_put, body_put)
        print(result_put)
        return result_put

    @staticmethod
    def delete_pet(pet_id):
        '''Удаляет питомца'''
        print("\nDELETE запрос для удаления питомца")

        resource_delete = f'/pet/{pet_id}'
        body = None

        url_delete = f'{PetApi.base_url}{resource_delete}'
        print(url_delete)

        result_delete = HttpMethods.delete(url_delete, body)
        print(result_delete.text)
        return result_delete
