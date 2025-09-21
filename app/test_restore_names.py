from __future__ import annotations

from typing import Dict, Optional, Union

from app.restore_names import restore_names


def _u(
    fn: Optional[str],
    ln: str,
    full: str,
    *,
    omit_first: bool = False,
) -> Dict[str, Union[str, None]]:
    """
    Helper para criar usuários nos testes.

    - Se omit_first=True, a chave 'first_name' não é criada.
    - Se omit_first=False, a chave 'first_name' é criada com o valor de `fn`.
    """
    user: Dict[str, Union[str, None]] = {"last_name": ln, "full_name": full}
    if not omit_first:
        user["first_name"] = fn
    return user


def test_restore_when_first_name_is_none() -> None:
    users = [
        _u(fn=None, ln="Holy", full="Jack Holy"),
        _u(fn=None, ln="Adams", full="Mike Adams"),
    ]
    expected = [
        _u(fn="Jack", ln="Holy", full="Jack Holy"),
        _u(fn="Mike", ln="Adams", full="Mike Adams"),
    ]

    result = restore_names(users)

    assert result is None, "A função deve operar in-place e não retornar nada"
    assert users == expected


def test_restore_when_first_name_key_is_missing() -> None:
    users = [
        _u(fn=None, ln="Doe", full="Jane Doe", omit_first=True),
        _u(fn=None, ln="Wayne", full="Bruce Wayne", omit_first=True),
    ]
    expected = [
        _u(fn="Jane", ln="Doe", full="Jane Doe"),
        _u(fn="Bruce", ln="Wayne", full="Bruce Wayne"),
    ]

    restore_names(users)

    assert users == expected, "Deve criar a chave first_name quando ausente"


def test_does_not_modify_existing_first_name() -> None:
    users = [
        _u(fn="Alice", ln="Smith", full="Alice Smith"),
        _u(fn="Bob", ln="Brown", full="Robert Brown"),
    ]
    original = [dict(u) for u in users]

    restore_names(users)

    assert users == original, "Não deve alterar first_name já válido"


def test_first_token_of_full_name_is_used() -> None:
    users = [
        _u(fn=None, ln="Trapp", full="Anna-Maria von Trapp"),
        _u(fn=None, ln="Lee", full="   Bruce   Lee  "),
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Anna-Maria"
    assert users[1]["first_name"] == "Bruce"
