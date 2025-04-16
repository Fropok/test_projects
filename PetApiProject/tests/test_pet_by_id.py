import pytest

from api.pet_api import PetApi
from utils.constants import TEST_PET_ID, TEST_CATEGORY, TEST_NAME, FIELD_ID, FIELD_CATEGORY, FIELD_NAME
from utils.checking import Checking


@pytest.mark.parametrize(
    "pet_id, category, name",
    [
        (TEST_PET_ID, TEST_CATEGORY, TEST_NAME),
    ]
)
def test_pet_by_id(pet_id, category, name, prepare_data):
    # Добавление питомца через фикстуру
    response = prepare_data(pet_id=pet_id, category=category, name=name)
    Checking.check_status_code(response, 200)

    # Проверяем GET
    response_get = PetApi.get_pet_by_id(pet_id)
    Checking.check_status_code(response_get, 200)
    Checking.check_key_and_value(response_get, FIELD_ID, pet_id)
    Checking.check_key_and_value(response_get, FIELD_CATEGORY, category)
    Checking.check_key_and_value(response_get, FIELD_NAME, name)
    print(f'Питомец добавлен ID: {pet_id}')

    # Удаляем питомца в фикстуре
