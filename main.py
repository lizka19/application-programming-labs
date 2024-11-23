
import argparse
import re

def get_file_name() -> str:
    """
    получаем имя файла
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', type=str, help='Input file.txt')
    args = parser.parse_args()
    return args.file_name

def read_file(file_name: str) -> str:
    """
    Чтение файла построчно
    возыращаем строку со всем содержимым файла
    """
    try:
        with open(file_name, mode='r', encoding='UTF-8') as file:
            date = file.read()
        return date
    except Exception:
        print("File was not found")

class NoPatternFoundError(Exception):
    """
    пользовательское исключение для случаев, когда шаблон не найден
    """
    pass

def split(dates: str) -> list[str]:
    """
    Разделяет полученную строку по анкетам.
    """
    divider = re.split(r'\d+\)\n', dates)
    if len(divider) == 1:
        raise NoPatternFoundError("pattern is not found in the text")
    return divider

def find_people_with_city_code(divider: list[str]) -> list[str]:
    """
    Поиск всех людей с данным кодом города
    возвращаем список требуемых анкет
    """
    found = [i for i in divider if re.search(r'\+7 927', i)]
    return found

def out_form(found: list[str]) -> None:
    """
    Вывод требуемых анкет
    ничего не возвращаем
    """
    print("\n")
    for j in found:
        print(j)


def main() -> None:
    try:
        filename = get_file_name()
        dates = read_file(filename)
        divider = split(dates)
        found = find_people_with_city_code(divider)
        out_form(found)
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()

