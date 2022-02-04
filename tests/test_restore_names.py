from app.restore_names import restore_names


def test_first_name_equals_none():
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


def test_key_first_name_does_not_exist():
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


def test_nothing_should_happen():
    initial_list = [
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

