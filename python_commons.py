from pathlib import Path

def is_blank(obj):
    if obj is None:
        return True
    elif is_empty(obj):
        return True
    return False


def is_empty(s: str):
    if s == "":
        return True
    return False

def read_file_to_list_of_string(file_path: Path):
    with open(file_path, 'r', encoding='UTF-8') as file:
        file_content = file.readlines()
        return file_content
    pass

def write_strings_to_path_file_name(strings: list, target_path_file_name: str):
    if strings.__len__() == 0:
        return
    with open(target_path_file_name, 'w') as file:
        for line in strings:
            file.write(line.__str__())
    pass

def string_strip(s: str):
    if is_blank(s):
        return False
    return s.strip() if s != s.strip() else s