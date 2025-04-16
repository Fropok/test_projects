import pytest
from api.pet_api import PetApi
from utils.constants import FIELD_ID


@pytest.fixture()
def prepare_data():
    pet_ids_list = []  # список ID созданных сущностей

    def add_pet(**kwargs):
        response = PetApi.post_add_pet(**kwargs)  # создаем сущности
        pet_id = response.json()[FIELD_ID]
        print(f'Добавление питомца ID: {pet_id}')
        pet_ids_list.append(pet_id)  # добавляем id созданных сущностей в список
        return response

    yield add_pet

    for i in pet_ids_list:
        PetApi.delete_pet(i)  # удаляем сущности
        print(f'Питомец удален ID: {i}')
