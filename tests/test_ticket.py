# tests/test_ticket.py

import pytest
from raffle.ticket import Ticket


def test_ticket_creation_with_ticket_count_less_than_5() -> None:
    ticket = Ticket(name="John", tickets_count=1)
    assert ticket.name == "John"
    assert ticket.tickets_count == 1


def test_ticket_creation_with_ticket_count_greater_than_5() -> None:
    with pytest.raises(Exception) as execinfo:
        ticket = Ticket(name="John", tickets_count=6)
    assert "Maximum of 5 tickets allowed per user" in str(execinfo.value)


def test_ticket_creation_with_ticket_count_less_than_1() -> None:
    with pytest.raises(Exception) as execinfo:
        # ticket_1 = Ticket(name="John", tickets_count=0)
        ticket_2 = Ticket(name="John", tickets_count=-1)
    assert "Number of tickets cannot be less than 1" in str(execinfo.value)


def test_generate_ticket() -> None:
    ticket = Ticket.generate_ticket()

    assert len(ticket) == 5
    for item in ticket:
        assert item <= 15
        assert item > 0
    for index, item in enumerate(ticket):
        temp_list = list(ticket)
        temp_list.pop(index)
        assert item not in temp_list
