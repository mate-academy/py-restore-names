from app.restore_names import restore_names


def test_if_first_name_none():
    dictionary = [
            {"first_name": None,
             "last_name": "Spice",
             "full_name": "Max Spice",
             },
            {"first_name": "Adam",
             "last_name": "Holy",
             "full_name": "Adam Holy",
             },
            {"last_name": "Break",
             "full_name": "David Holy",
             },
        ]
    assert restore_names(dictionary) == [
       {"first_name": "Max",
        "last_name": "Spice",
        "full_name": "Max Spice",
        },
       {"first_name": "Adam",
        "last_name": "Holy",
        "full_name": "Adam Holy",
        },
       {"first_name": "David",
        "last_name": "Break",
        "full_name": "David Holy",
        },
    ]
