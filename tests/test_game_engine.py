# tests/test_game_engine.py

import pytest

from raffle.game_engine import Game, PrizeGroup
from raffle.ticket import Ticket


def test_buy_tickets_before_draw_throws_exception() -> None:
    game = Game(seed_amount=100)

    ticket = Ticket("John", 1)
    ticket.tickets_ids = [[4, 5, 6, 7, 8]]

    with pytest.raises(Exception) as e:
        game.buy_tickets(ticket)

    assert "Start a New Draw to Buy tickets" in str(e.value)


def test_run_raffle_before_draw_throws_exception() -> None:
    game = Game(seed_amount=100)

    ticket = Ticket("John", 1)
    ticket.tickets_ids = [[4, 5, 6, 7, 8]]

    with pytest.raises(Exception) as e:
        game.run_raffle()

    assert "Start a New Draw and buy tickets to run raffle" in str(e.value)


def test_get_winners_for() -> None:
    game = Game(seed_amount=100)
    game.start_new_draw()

    winning_ticket = [1, 2, 3, 4, 5]

    ticket = Ticket("John", 1)
    ticket.tickets_ids = [[4, 5, 6, 7, 8]]
    game.buy_tickets(ticket)

    ticket = Ticket("Mary", 2)
    ticket.tickets_ids = [[1, 2, 6, 7, 8], [3, 4, 1, 7, 8]]
    game.buy_tickets(ticket)

    ticket = Ticket("Doe", 3)
    ticket.tickets_ids = [[1, 2, 6, 7, 8], [3, 4, 15, 7, 8], [1, 2, 3, 4, 5]]
    game.buy_tickets(ticket)

    ticket = Ticket("Jane", 4)
    ticket.tickets_ids = [
        [1, 2, 6, 7, 8],
        [3, 4, 15, 7, 8],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 9],
    ]
    game.buy_tickets(ticket)

    winners = game.get_winners_for(PrizeGroup.Group2, winning_ticket)
    assert winners["John"] == 1
    assert winners["Mary"] == 1
    assert winners["Doe"] == 2
    assert winners["Jane"] == 2

    winners = game.get_winners_for(PrizeGroup.Group3, winning_ticket)
    assert winners["John"] == 0
    assert winners["Mary"] == 1
    assert winners["Doe"] == 0
    assert winners["Jane"] == 0

    winners = game.get_winners_for(PrizeGroup.Group4, winning_ticket)
    assert winners["John"] == 0
    assert winners["Mary"] == 0
    assert winners["Doe"] == 0
    assert winners["Jane"] == 1

    winners = game.get_winners_for(PrizeGroup.Group5, winning_ticket)
    assert winners["John"] == 0
    assert winners["Mary"] == 0
    assert winners["Doe"] == 1
    assert winners["Jane"] == 1


def test_winner_by_prize_group() -> None:
    game = Game(seed_amount=100)
    game.start_new_draw()

    winning_ticket = [1, 2, 3, 4, 5]

    ticket = Ticket("John", 1)
    ticket.tickets_ids = [[4, 5, 6, 7, 8]]
    game.buy_tickets(ticket)

    ticket = Ticket("Mary", 2)
    ticket.tickets_ids = [[1, 2, 6, 7, 8], [3, 4, 1, 7, 8]]
    game.buy_tickets(ticket)

    ticket = Ticket("Doe", 3)
    ticket.tickets_ids = [[1, 2, 6, 7, 8], [3, 4, 15, 7, 8], [1, 2, 3, 4, 5]]
    game.buy_tickets(ticket)

    ticket = Ticket("Jane", 4)
    ticket.tickets_ids = [
        [1, 2, 6, 7, 8],
        [3, 4, 15, 7, 8],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 9],
    ]
    game.buy_tickets(ticket)

    winners_grp2 = game.get_winners_for(PrizeGroup.Group2, winning_ticket)
    winners_grp3 = game.get_winners_for(PrizeGroup.Group3, winning_ticket)
    winners_grp4 = game.get_winners_for(PrizeGroup.Group4, winning_ticket)
    winners_grp5 = game.get_winners_for(PrizeGroup.Group5, winning_ticket)

    group_prize_amount = game.calculate_prize_amount(PrizeGroup.Group2)
    grp_winners = game.winner_by_prize_group(winners_grp2, group_prize_amount)
    assert len(grp_winners) == 4

    group_prize_amount = game.calculate_prize_amount(PrizeGroup.Group3)
    grp_winners = game.winner_by_prize_group(winners_grp3, group_prize_amount)
    assert len(grp_winners) == 1

    group_prize_amount = game.calculate_prize_amount(PrizeGroup.Group4)
    grp_winners = game.winner_by_prize_group(winners_grp4, group_prize_amount)
    assert len(grp_winners) == 1

    group_prize_amount = game.calculate_prize_amount(PrizeGroup.Group5)
    grp_winners = game.winner_by_prize_group(winners_grp5, group_prize_amount)
    assert len(grp_winners) == 2


def test_prize_amount_won_by_each_user() -> None:
    group_prize_amount: float = 10
    total_win_ticket_count: int = 3
    user_won_ticket_count: int = 1

    game = Game(100)

    prize_amount = game.prize_amount_won_by_each_user(
        group_prize_amount, total_win_ticket_count, user_won_ticket_count
    )

    assert prize_amount == 3.33

    group_prize_amount = 10
    total_win_ticket_count = 3
    user_won_ticket_count = 2

    game = Game(100)

    prize_amount = game.prize_amount_won_by_each_user(
        group_prize_amount, total_win_ticket_count, user_won_ticket_count
    )

    assert prize_amount == 6.67

    group_prize_amount = 10
    total_win_ticket_count = 3
    user_won_ticket_count = 3

    game = Game(100)

    prize_amount = game.prize_amount_won_by_each_user(
        group_prize_amount, total_win_ticket_count, user_won_ticket_count
    )

    assert prize_amount == 10


def test_calculate_prize_amount() -> None:
    game = Game(seed_amount=100)
    grp2_prize_amt = game.calculate_prize_amount(prize_group=PrizeGroup.Group2)
    grp3_prize_amt = game.calculate_prize_amount(prize_group=PrizeGroup.Group3)
    grp4_prize_amt = game.calculate_prize_amount(prize_group=PrizeGroup.Group4)
    grp5_prize_amt = game.calculate_prize_amount(prize_group=PrizeGroup.Group5)

    assert grp2_prize_amt == 10
    assert grp3_prize_amt == 15
    assert grp4_prize_amt == 25
    assert grp5_prize_amt == 50
