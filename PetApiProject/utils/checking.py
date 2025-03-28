class Checking:

    @staticmethod
    def check_status_code(response_code, expected_code):
        '''Проверка статус кода'''
        assert response_code.status_code == expected_code, f'ОШИБКА! Статус код: {response_code.status_code}'
        print(f'Успешно! Статус код: {expected_code}')

    @staticmethod
    def check_key_and_value(result_response, expected_key, expected_value):
        '''Проверка ключа и значения'''
        response_json = result_response.json()
        if expected_key not in response_json:
            raise KeyError(f'Ключ: "{expected_key}" не найден в ответе')
        factual_value = response_json[expected_key]
        assert factual_value == expected_value, f'ОШИБКА! Фактическое значение: {factual_value}, ожидаемое значение: {expected_value}'
        print('Успешно! Ключ и значение совпадает')
