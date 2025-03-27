from utils.google_maps_api import GoogleMapsApi
from utils.checking import Checking
import allure

@allure.epic('Проверка Google Maps API')
class TestGoogleMapsApi:
    '''Тест запросов Google Maps API'''

    @allure.description('Проверка создания, изменения и удаления локации')
    def test_location(self):
        '''Запрос POST для создания локации'''
        print('Метод POST')
        result_post = GoogleMapsApi.post_location()
        place_id = result_post.json()['place_id']  # сохраняем полученный place_id
        Checking.check_status(result_post, 200)
        Checking.check_key(result_post, 'place_id', 'reference')
        Checking.check_value(result_post, 'status', 'OK')

        print()

        '''Запрос GET для проверки создания локации'''
        print('Метод GET для POST')
        result_get = GoogleMapsApi.get_location(place_id)
        Checking.check_status(result_get, 200)
        Checking.check_key(result_get, 'location', 'phone_number', 'address')
        Checking.check_value(result_get, 'address', '29, side layout, cohen 09')

        print()

        '''Запрос PUT для изменения локации'''
        print('Метод PUT')
        result_put = GoogleMapsApi.put_location(place_id)
        Checking.check_status(result_put, 200)
        Checking.check_key(result_put, 'msg')
        Checking.check_value(result_put, 'msg', 'Address successfully updated')

        print()

        '''Запрос GET для проверки изменения локации'''
        print('Метод GET для PUT')
        result_get = GoogleMapsApi.get_location(place_id)
        Checking.check_status(result_get, 200)
        Checking.check_key(result_get, 'location', 'phone_number', 'address')
        Checking.check_value(result_get, 'address', '100 Lenina street, RU')

        print()

        '''Запрос DELETE для удаления локации'''
        print('Метод DELETE')
        result_delete = GoogleMapsApi.delete_location(place_id)
        Checking.check_status(result_delete, 200)
        Checking.check_key(result_delete, 'status')
        Checking.check_value(result_delete, 'status', 'OK')

        print()

        '''Запрос GET для проверки удаления локации'''
        print('Метод GET для DELETE')
        result_get = GoogleMapsApi.get_location(place_id)
        Checking.check_status(result_get, 404)
        Checking.check_key(result_get, 'msg')
        Checking.check_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")

        print()
        print('УСПЕШНО! тестирование запросов Google Maps API (class TestGoogleMapsApi)')
