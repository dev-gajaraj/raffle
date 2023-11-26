# raffle/game_engine.py

from enum import Enum
from typing import List, Dict

from rich import print
from raffle.ticket import Ticket, Winner
from raffle.utility import clear_console


class GameStatus(Enum):
    NOT_STARTED = 0
    ONGOING = 1


class PrizeGroup(Enum):
    Group2 = 2
    Group3 = 3
    Group4 = 4
    Group5 = 5


class Game:
    """Class contains the methods and interface required for draw game"""

    def __init__(self, seed_amount: float = 100, ticket_price: float = 5.0) -> None:
        self.__seed_amount = seed_amount
        self.__ticket_price = ticket_price
        self.__tickets: List[Ticket] = []
        self.__status: GameStatus = GameStatus.NOT_STARTED
        self.__total_draw_won_amount: float = 0.0
        self.__winning_ticket: List[int] | None

        self.reset()
        # self.__display_main_promt()

    @property
    def seed_amount(self) -> float:
        return self.__seed_amount

    @property
    def ticket_price(self) -> float:
        return self.__ticket_price

    @property
    def tickets(self) -> List[Ticket]:
        return self.__tickets

    @property
    def status(self) -> GameStatus:
        return self.__status

    @property
    def winning_ticket(self) -> List[int] | None:
        return self.__winning_ticket

    def reset(self) -> None:
        """Reset game variables like tickets, game status and total draw amount"""
        self.__tickets = []
        self.__status = GameStatus.NOT_STARTED
        self.__total_draw_won_amount = 0

    def start_new_draw(self) -> None:
        """Start raffle game"""
        if self.__status == GameStatus.ONGOING:
            raise Exception(
                "[dark_orange3]Raffle draw is already ongoing.\nPlease buy tickets to play the game[/]"
            )
        self.reset()
        self.__winning_ticket = []

        self.__status = GameStatus.ONGOING

    def buy_tickets(self, user: Ticket) -> None:
        """Buy tickets for raffle draw game"""
        if self.__status != GameStatus.ONGOING:
            raise Exception("Start a New Draw to Buy tickets")

        # if user in self.__users and user.tickets_count:
        #     old_usr_index = self.__users.index(user)
        #     old_usr = self.__users[old_usr_index]
        #     old_usr.tickets_count += user.tickets_count

        self.__seed_amount += user.tickets_count * self.__ticket_price
        self.__tickets.append(user)

    def run_raffle(self) -> Dict[PrizeGroup, List[Winner]]:
        """Run raffle game"""
        if self.__status != GameStatus.ONGOING:
            raise Exception("Start a New Draw and buy tickets to run raffle")

        # Generate winning ticket
        self.__winning_ticket = Ticket.generate_ticket()

        # Get winners
        all_winners: Dict[PrizeGroup, List[Winner]] = {}
        for prize_group in PrizeGroup:
            group_prize_amount = self.calculate_prize_amount(prize_group)

            winners = self.get_winners_for(prize_group, self.__winning_ticket)
            grp_winners = self.winner_by_prize_group(winners, group_prize_amount)
            all_winners[prize_group] = grp_winners

        # Minus total draw won amount from total pot size
        self.__seed_amount -= self.__total_draw_won_amount
        # End Draw
        self.reset()

        return all_winners

    def winner_by_prize_group(self, winners, group_prize_amount: float) -> List[Winner]:
        grp_winners: List[Winner] = []
        if sum(winners.values()) <= 0:
            return grp_winners
        for name, no_tickets in winners.items():
            user_won_amt = self.prize_amount_won_by_each_user(
                group_prize_amount, sum(winners.values()), no_tickets
            )
            self.__total_draw_won_amount += user_won_amt
            if no_tickets > 0:
                grp_winners.append(Winner(name, no_tickets, user_won_amt))
        return grp_winners

    def prize_amount_won_by_each_user(
        self,
        group_prize_amount: float,
        total_win_ticket_count_in_grp: int,
        tickets_won_by_user: int,
    ) -> float:
        return round(
            group_prize_amount / total_win_ticket_count_in_grp * tickets_won_by_user, 2
        )

    def get_winners_for(
        self,
        prize_grp: PrizeGroup,
        winning_ticket: List[int],
    ) -> Dict[str, int]:
        winners: Dict[str, int] = {}

        for usr in self.__tickets:
            winners[usr.name] = 0
            for tid in usr.tickets_ids:
                matching_numbers = 0
                for item in tid:
                    if item in winning_ticket:
                        matching_numbers += 1

                if prize_grp.value == matching_numbers:
                    winners[usr.name] += 1

        return winners

    def calculate_prize_amount(self, prize_group: PrizeGroup):
        win_prize_amount: float = 0.0
        match prize_group.value:
            case 2:
                win_prize_amount = 10 / 100 * self.__seed_amount
            case 3:
                win_prize_amount = 15 / 100 * self.__seed_amount
            case 4:
                win_prize_amount = 25 / 100 * self.__seed_amount
            case 5:
                win_prize_amount = 50 / 100 * self.__seed_amount
            case other:
                raise Exception("Invalid prize group!!!")
        return win_prize_amount
