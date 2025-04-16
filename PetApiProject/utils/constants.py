BASE_URL = 'https://petstore.swagger.io/v2'
HEADERS = {"Content-Type": "application/json"}
COOKIES = ''

# ENDPOINT
ENDPOINT_PET = '/pet'
ENDPOINT_PET_BY_ID = '/pet/{pet_id}'

# FIELDS BODY
FIELD_ID = "id"
FIELD_CATEGORY = "category"
FIELD_NAME = "name"
FIELD_PHOTO_URLS = "photoUrls"
FIELD_TAGS = "tags"
FIELD_STATUS = "status"

# VALUES BODY
VALUE_ID = 0
VALUE_CATEGORY = {"id": 0, "name": "string"}
VALUE_NAME = "doggie"
VALUE_PHOTO_URLS = ["string"]
VALUE_TAGS = [{"id": 0, "name": "string"}]
VALUE_STATUS = "available"

# TEST VALUES
TEST_PET_ID = 20421403
TEST_CATEGORY = {"id": 21, "name": "cat"}
TEST_NAME = "Barni"

# TEST VALUES UPDATE
TEST_CATEGORY_UPDATE = {"id": 22, "name": "catUP"}
TEST_NAME_UPDATE = "BarniUP"