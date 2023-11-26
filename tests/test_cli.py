# tests/test_cli.py

from _pytest.capture import capsys
import pytest
from raffle.cli import display_main_page, get_tickets_and_validate
from raffle.game_engine import GameStatus


def test_display_main_page_game_not_started(capsys) -> None:
    seed_amount = 100.0
    status = GameStatus.NOT_STARTED

    display_main_page(seed_amount, status)
    captured = capsys.readouterr()

    assert (
        "\nWelcome to My Raffle App\nStatus: Draw has not started\n[1] Start a New Draw\n[2] Buy Tickets\n[3] Run Raffle\n"
        in captured.out
    )


def test_display_main_page_game_started(capsys) -> None:
    seed_amount = 100.0
    status = GameStatus.ONGOING

    display_main_page(seed_amount, status)
    captured = capsys.readouterr()

    assert (
        "\nWelcome to My Raffle App\nStatus: Draw is ongoing. Raffle pot size is $100.0\n[1] Start a New Draw\n[2] Buy Tickets\n[3] Run Raffle\n"
        in captured
    )


def test_get_tickets_and_validate_correct_name_and_tickets(monkeypatch) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "john,1")
    input = get_tickets_and_validate()

    assert input == ["john", "1"]


def test_get_tickets_and_validate_raise_exception_for_non_int_ticket_count(
    monkeypatch,
) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "john,a")

    with pytest.raises(Exception) as e:
        input = get_tickets_and_validate()

    assert "Invalid input for number of tickets" in str(e.value)


def test_get_tickets_and_validate_raise_exception_for_invalid_separator(
    monkeypatch,
) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "john.a")

    with pytest.raises(Exception) as e:
        get_tickets_and_validate()

    assert "Invalid input entered" in str(e.value)
