# raffle/ticket.py

import random
from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Ticket:
    name: str
    tickets_count: int
    tickets_ids: List[List[int]] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.tickets_count <= 0:
            raise Exception("Number of tickets cannot be less than 1")

        if self.tickets_count > 5:
            raise Exception("Maximum of 5 tickets allowed per user")

        self.tickets_ids = [Ticket.generate_ticket() for _ in range(self.tickets_count)]

    def __eq__(self, other):
        return self.name == other.name

    @classmethod
    def generate_ticket(cls) -> List[int]:
        """Generate Ticket id"""
        return random.sample(range(1, 15), 5)


@dataclass
class Winner:
    name: str
    ticket_won_count: int
    won_amount: float

    def __eq__(self, other):
        return self.name == other.name
