class StringUtils:

    def capitalize(self, string: str) -> str:
        """Принимает строку, делает первую букву заглавной"""
        return string.capitalize()

    def trim(self, string: str) -> str:
        """Принимает строку, удаляет пробелы в начале"""
        return string.lstrip()

    def to_list(self, string: str, delimeter: str = ",") -> list:
        """Принимает строку, возвращает список слов"""
        if string == "" or string is None:
            return []
        return string.split(delimeter)

    def contains(self, string: str, symbol: str) -> bool:
        """Возвращает True если строка содержит символ"""
        return symbol in string

    def delete_symbol(self, string: str, symbol: str) -> str:
        """Удаляет символ из строки"""
        return string.replace(symbol, "")

    def starts_with(self, string: str, symbol: str) -> bool:
        """Возвращает True если строка начинается с символа"""
        return string.startswith(symbol)

    def end_with(self, string: str, symbol: str) -> bool:
        """Возвращает True если строка заканчивается символом"""
        return string.endswith(symbol)

    def is_empty(self, string: str) -> bool:
        """Возвращает True если строка пустая или None"""
        return string is None or string.strip() == ""

    def list_to_string(self, lst: list, joiner: str = ", ") -> str:
        """Преобразует список в строку через разделитель"""
        return joiner.join([str(x) for x in lst])
