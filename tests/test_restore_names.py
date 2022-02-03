from app.restore_names import restore_names


def test_name_none():
    initial_list = [
  {
    "first_name": None,
    "last_name": "Holy",
    "full_name": "Jack Holy",
  },
  {
    "first_name": "Mike",
    "last_name": "Adams",
    "full_name": "Mike Adams",
  },
]

    restore_names(initial_list)
    assert initial_list == [
  {
    "first_name": "Jack",
    "last_name": "Holy",
    "full_name": "Jack Holy",
  },
  {
    "first_name": "Mike",
    "last_name": "Adams",
    "full_name": "Mike Adams",
  },
]


def test_now_key_name():
    initial_list = [
      {
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy",
      },
      {
        "last_name": "Adams",
        "full_name": "Mike Adams",
      },
    ]

    restore_names(initial_list)
    assert initial_list == [
      {
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy",
      },
      {
        "first_name": "Mike",
        "last_name": "Adams",
        "full_name": "Mike Adams",
      },
    ]


def test_list_should_be_modified():
    initial_list = [
    {
      "first_name": None,
      "last_name": "Holy",
      "full_name": "Jack Holy",
    },
    {
      "last_name": "Adams",
      "full_name": "Mike Adams",
    },
    ]
    initial_id = id(initial_list)

    restore_names(initial_list)
    assert initial_list == [
      {
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy",
      },
      {
        "first_name": "Mike",
        "last_name": "Adams",
        "full_name": "Mike Adams",
      },
    ]

    assert id(initial_list) == initial_id

