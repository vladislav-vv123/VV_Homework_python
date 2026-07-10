import pytest

API_URL = "https://ru.yougile.com/api-v2"
API_TOKEN = "4Qt0AhVmLpOr9z-YWceOR7I3omooABqKZ+xtoS5ulwFkwqyiX474ga95ZaVHSPMj"


@pytest.fixture
def api_token():
    return API_TOKEN


@pytest.fixture
def base_url():
    return API_URL
