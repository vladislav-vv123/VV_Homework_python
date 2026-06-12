from string_utils import StringUtils

utils = StringUtils()


def test_capitalize_first_letter():
    assert utils.capitalize("hello") == "Hello"


def test_capitalize_already_upper():
    assert utils.capitalize("Hello") == "Hello"


def test_capitalize_empty_string():
    assert utils.capitalize("") == ""


def test_capitalize_numbers():
    assert utils.capitalize("123") == "123"


def test_trim_spaces():
    assert utils.trim("  hello") == "hello"


def test_trim_no_spaces():
    assert utils.trim("hello") == "hello"


def test_trim_empty_string():
    assert utils.trim("") == ""


def test_to_list_basic():
    assert utils.to_list("a,b,c") == ["a", "b", "c"]


def test_to_list_custom_delimeter():
    assert utils.to_list("a:b:c", ":") == ["a", "b", "c"]


def test_to_list_empty_string():
    assert utils.to_list("") == []


def test_to_list_none():
    assert utils.to_list(None) == []


def test_contains_true():
    assert utils.contains("hello", "e") is True


def test_contains_false():
    assert utils.contains("hello", "x") is False


def test_delete_symbol():
    assert utils.delete_symbol("hello", "l") == "heo"


def test_delete_symbol_not_found():
    assert utils.delete_symbol("hello", "x") == "hello"


def test_starts_with_true():
    assert utils.starts_with("hello", "h") is True


def test_starts_with_false():
    assert utils.starts_with("hello", "e") is False


def test_end_with_true():
    assert utils.end_with("hello", "o") is True


def test_end_with_false():
    assert utils.end_with("hello", "x") is False


def test_is_empty_true():
    assert utils.is_empty("") is True


def test_is_empty_space():
    assert utils.is_empty(" ") is True


def test_is_empty_none():
    assert utils.is_empty(None) is True


def test_is_empty_false():
    assert utils.is_empty("hello") is False


def test_list_to_string_basic():
    assert utils.list_to_string([1, 2, 3]) == "1, 2, 3"


def test_list_to_string_custom_joiner():
    assert utils.list_to_string(["a", "b"], "-") == "a-b"


def test_list_to_string_empty():
    assert utils.list_to_string([]) == ""
