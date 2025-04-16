import pytest
from utils.constants import TEST_PET_ID, TEST_CATEGORY, TEST_NAME
from utils.checking import Checking
from api.pet_api import PetApi


@pytest.mark.parametrize(
    "pet_id, category, name",
    [
        (TEST_PET_ID, TEST_CATEGORY, TEST_NAME),
    ]
)
def test_delete_pet(pet_id, category, name, prepare_data):
    # Создание питомца через фикстуру
    response = prepare_data(pet_id=pet_id, category=category, name=name)
    Checking.check_status_code(response, 200)

    # Удаляем питомца
    response_delete = PetApi.delete_pet(pet_id)

    # Проверка удаления
    Checking.check_status_code(response_delete, 200)
    Checking.check_key_and_value(response_delete, "message", f"{pet_id}")
    print(f'Удаление питомца ID: {pet_id}')

    # Проверка через GET
    response_get = PetApi.get_pet_by_id(pet_id)
    Checking.check_status_code(response_get, 404)
    Checking.check_key_and_value(response_get, "message", "Pet not found")
    print(f'Питомец удален ID: {pet_id}')

    # Удаляем питомца в фикстуре
