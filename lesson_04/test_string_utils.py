from string_utils import StringUtils

utils = StringUtils()


def test_capitalize_first_letter():
    assert utils.capitalize("skypro") == "Skypro"


def test_capitalize_russian():
    assert utils.capitalize("тест") == "Тест"


def test_capitalize_numbers():
    assert utils.capitalize("123") == "123"


def test_capitalize_with_spaces():
    assert utils.capitalize("04 апреля 2023") == "04 апреля 2023"


def test_capitalize_empty_string():
    assert utils.capitalize("") == ""


def test_trim_spaces():
    assert utils.trim("   skypro") == "skypro"


def test_trim_no_spaces():
    assert utils.trim("skypro") == "skypro"


def test_trim_space_only():
    assert utils.trim(" ") == ""


def test_trim_empty_string():
    assert utils.trim("") == ""


def test_contains_true():
    assert utils.contains("SkyPro", "S") is True


def test_contains_false():
    assert utils.contains("SkyPro", "U") is False


def test_contains_russian():
    assert utils.contains("Тест", "е") is True


def test_contains_empty_string():
    assert utils.contains("", "S") is False


def test_delete_symbol_basic():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"


def test_delete_symbol_substring():
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"


def test_delete_symbol_not_found():
    assert utils.delete_symbol("SkyPro", "x") == "SkyPro"


def test_delete_symbol_numbers():
    assert utils.delete_symbol("123", "2") == "13"


def test_delete_symbol_empty_string():
    assert utils.delete_symbol("", "S") == ""
