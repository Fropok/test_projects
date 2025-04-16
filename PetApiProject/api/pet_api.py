from typing import Optional

from utils.http_methods import HttpMethods
from utils.constants import BASE_URL, ENDPOINT_PET, ENDPOINT_PET_BY_ID, VALUE_ID, VALUE_CATEGORY, VALUE_NAME, \
    VALUE_PHOTO_URLS, VALUE_TAGS, VALUE_STATUS, FIELD_ID, FIELD_CATEGORY, FIELD_NAME, FIELD_PHOTO_URLS, FIELD_TAGS, \
    FIELD_STATUS


class PetApi:
    '''HTTP запросы для добавления, обновления, удаления питомца'''

    @staticmethod
    def post_add_pet(
            pet_id: int = VALUE_ID,
            category: Optional[dict] = None,
            name: str = VALUE_NAME,
            photo_urls: Optional[list] = None,
            tags: Optional[list] = None,
            status: str = VALUE_STATUS
    ):
        '''Добавить нового питомца'''
        print("\nPOST запрос для добавления нового питомца")

        url_post = f'{BASE_URL}{ENDPOINT_PET}'
        print(url_post)

        body_post = {
            FIELD_ID: pet_id,
            FIELD_CATEGORY: VALUE_CATEGORY if category is None else category,
            FIELD_NAME: name,
            FIELD_PHOTO_URLS: VALUE_PHOTO_URLS if photo_urls is None else photo_urls,
            FIELD_TAGS: VALUE_TAGS if tags is None else tags,
            FIELD_STATUS: status
        }

        result_post = HttpMethods.post(url_post, body_post)
        print(result_post.text)

        return result_post

    @staticmethod
    def get_pet_by_id(pet_id: int = 0):
        '''Найти питомца по ID'''
        print("\nGET запрос для поиска питомца по ID")

        url_get = f'{BASE_URL}{ENDPOINT_PET_BY_ID.format(pet_id=pet_id)}'
        print(url_get)

        result_get = HttpMethods.get(url_get)
        print(result_get.text)

        return result_get

    @staticmethod
    def put_update_pet(
            pet_id: int = VALUE_ID,
            category: Optional[dict] = None,
            name: str = VALUE_NAME,
            photo_urls: Optional[list] = None,
            tags: Optional[list] = None,
            status: str = VALUE_STATUS

    ):
        '''Обновить существующего питомца'''
        print("\nPUT запрос для обновления существующего питомца")

        url_put = f'{BASE_URL}{ENDPOINT_PET}'
        print(url_put)

        body_put = {
            FIELD_ID: pet_id,
            FIELD_CATEGORY: VALUE_CATEGORY if category is None else category,
            FIELD_NAME: name,
            FIELD_PHOTO_URLS: VALUE_PHOTO_URLS if photo_urls is None else photo_urls,
            FIELD_TAGS: VALUE_TAGS if tags is None else tags,
            FIELD_STATUS: status
        }

        result_put = HttpMethods.put(url_put, body_put)
        print(result_put)

        return result_put

    @staticmethod
    def delete_pet(pet_id: int = 0):
        '''Удаляет питомца'''
        print("\nDELETE запрос для удаления питомца")

        url_delete = f'{BASE_URL}{ENDPOINT_PET_BY_ID.format(pet_id=pet_id)}'
        print(url_delete)

        result_delete = HttpMethods.delete(url_delete)
        print(result_delete.text)

        return result_delete
