import pytest

from api.pet_api import PetApi
from utils.checking import Checking


class TestPetApi:

    @pytest.mark.parametrize(
        f'pet_id, category_id, category_name, name',
        [
            (281273083, 1, 'BARNI', 'Cat')
        ]
    )
    def test_pet(self, pet_id, category_id, category_name, name, set_up):
        '''Проверка добавления, обновления, удаления питомца'''

        # POST
        result_post = PetApi.post_pet(pet_id, category={"id": category_id, "name": category_name}, name=name)
        Checking.check_status_code(result_post, 200)
        print('Добавление питомца')

        #GET
        result_get = PetApi.get_pet(pet_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_key_and_value(result_get, "id", pet_id)
        Checking.check_key_and_value(result_get, "name", name)
        print('Питомец добавлен')

        #PUT
        category_id_update = category_id + 1
        category_name_update = category_name + "Update"
        name_update = name + "Update"
        result_put = PetApi.put_pet(pet_id, category={"id": category_id_update, "name": category_name_update},name=name_update)
        Checking.check_status_code(result_put, 200)
        print('Обновление данных питомца')

        #GET
        result_get = PetApi.get_pet(pet_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_key_and_value(result_get, "id", pet_id)
        Checking.check_key_and_value(result_get, "name", name_update)
        print('Данные питомца обновлены')

        #DELETE
        result_delete = PetApi.delete_pet(pet_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_key_and_value(result_delete, "message", f"{pet_id}")
        print('Удаление питомца')

        #GET
        result_get = PetApi.get_pet(pet_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_key_and_value(result_get, "message", "Pet not found")
        print('Питомец удален')

        print('\nУСПЕШНО! тестирование запросов Pet API (class TestPetApi)\n')
