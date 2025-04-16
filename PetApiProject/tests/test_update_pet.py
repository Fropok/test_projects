import pytest
from utils.constants import TEST_PET_ID, TEST_CATEGORY, TEST_NAME, TEST_CATEGORY_UPDATE, TEST_NAME_UPDATE, FIELD_ID, \
    FIELD_CATEGORY, FIELD_NAME
from utils.checking import Checking
from api.pet_api import PetApi


@pytest.mark.parametrize(
    "pet_id, category, name",
    [
        (TEST_PET_ID, TEST_CATEGORY, TEST_NAME),
    ]
)
def test_update_pet(pet_id, category, name, prepare_data):
    # Добавление питомца через фикстуру
    response = prepare_data(pet_id=pet_id, category=category, name=name)
    Checking.check_status_code(response, 200)

    # Обновляем данные питомца
    response_put = PetApi.put_update_pet(pet_id, TEST_CATEGORY_UPDATE, TEST_NAME_UPDATE)

    # Проверяем обновленные данные
    Checking.check_status_code(response_put, 200)
    Checking.check_key_and_value(response_put, FIELD_ID, pet_id)
    Checking.check_key_and_value(response_put, FIELD_CATEGORY, TEST_CATEGORY_UPDATE)
    Checking.check_key_and_value(response_put, FIELD_NAME, TEST_NAME_UPDATE)
    print(f'Обновление данных питомца ID: {pet_id}')

    # Проверка через GET
    response_get = PetApi.get_pet_by_id(pet_id)
    Checking.check_status_code(response_get, 200)
    Checking.check_key_and_value(response_get, FIELD_ID, pet_id)
    Checking.check_key_and_value(response_get, FIELD_CATEGORY, TEST_CATEGORY_UPDATE)
    Checking.check_key_and_value(response_get, FIELD_NAME, TEST_NAME_UPDATE)
    print(f'Данные питомца обновлены ID: {pet_id}')

    # Удаляем питомца в фикстуре
