class Checking:
    '''Методы проверки'''

    @staticmethod
    def check_status(result_response, expected_code):
        '''Проверка статус кода'''
        assert result_response.status_code == expected_code, f'ОШИБКА! Статус: {result_response.status_code}'
        print(f'Успешно! Статус: {expected_code} ')

    @staticmethod
    def check_key(result_response, *args):
        '''Проверка наличия полей'''
        for i in args:
            assert i in result_response.json(), f'ОШИБКА! Нет поля: {i}'
        print('Успешно! Все поля на месте.')

    @staticmethod
    def check_value(result_response, key, value):
        '''Проверка соответствия значения в выбранном поле'''
        key_value = result_response.json()[key]
        key_value = key_value.replace("'", '"')
        value = value.replace("'", '"')
        assert key_value == value, f'ОШИБКА! Ожидаемое значение: {value}, фактическое значение: {key_value}'
        print('Успешно! Значения совпадают.')
