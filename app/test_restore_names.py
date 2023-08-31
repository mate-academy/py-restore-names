import pytest
from app.restore_names import restore_names


def get_first_name_from_full_name(full_name):
    parts = full_name.split()
    first_name = parts[0] if parts else ""
    return first_name


def test_get_first_name_from_full_name():
    assert get_first_name_from_full_name("Ostap Boiko") == "Ostap"
    assert get_first_name_from_full_name("Ivan Bilui") == "Ivan"
    assert get_first_name_from_full_name("Ivan Boiko") == "Ivan"
    assert get_first_name_from_full_name("Vasia") == "Vasia"
