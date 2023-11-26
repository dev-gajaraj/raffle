"""This module provides the raffle CLI."""
# raffle/cli.py

from ast import Dict, List
from typing import Optional

import typer

from rich import print
from raffle import __app_name__, __version__
from raffle.ticket import Ticket, Winner
from raffle.utility import clear_console
from .game_engine import Game, GameStatus, PrizeGroup

app = typer.Typer()


@app.command()
def start(
    start=typer.Option(
        None,
        "--start",
        "-s",
        # prompt="Do you want to start the game?",
    ),
) -> None:
    """Start the game"""
    game = Game(seed_amount=100, ticket_price=5)
    clear_console()

    while True:
        user_choice: int
        display_main_page(game.seed_amount, game.status)
        try:
            user_choice = int(input())
        except ValueError:
            print(f"[red]Please enter a valid choice[/]\n")
            continue

        if user_choice <= 0 or user_choice > 3:
            print("[red]Please enter a valid choice[/]\n")
            continue

        if user_choice == 1:
            try:
                game.start_new_draw()
                print(
                    f"\n[dark_orange3]New Raffle draw has been started. Initial pot size: [green]${round(game.seed_amount,2)}[/][/]"
                )
                input("Press any key to return to main menu\n")
            except Exception as e:
                print(f"{e}\n")
        elif user_choice == 2:
            try:
                user_buy_ticket_intput = get_tickets_and_validate()
            except Exception as e:
                print(f"[red]{e}[/]")
                continue

            ticket = Ticket(user_buy_ticket_intput[0], int(user_buy_ticket_intput[1]))

            try:
                game.buy_tickets(ticket)
            except Exception as e:
                print(f"[red]{e}[/]")
                continue

            print(
                f"Hi {ticket.name}, you have purchased {ticket.tickets_count} ticket(s)-\n"
            )

            for i, id in enumerate(ticket.tickets_ids):
                print(f"Ticket {i+1}: {id}")
        elif user_choice == 3:
            print("\nRunning Raffle...")

            winners: dict[PrizeGroup, list[Winner]]
            try:
                winners = game.run_raffle()
            except Exception as e:
                print(f"[red]{e}[/]")
                continue

            print(f"[bold gold3]Winning ticket: {game.winning_ticket}[/]")

            for prize_grp, winner_list in winners.items():
                print(f"\n[gold3]Group {prize_grp.value} Winners:[/]")

                if len(winner_list) == 0:
                    print("Nil")
                    continue

                for winner in winner_list:
                    print(
                        f"{winner.name} with {winner.ticket_won_count} winning ticket(s)- ${round(winner.won_amount,2)}"
                    )
            input("Press any key to return to main menu")
        else:
            raise ValueError


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the applications's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return


def display_main_page(seed_amount: float, status: GameStatus) -> None:
    """Display main page of raffle"""
    statuses = {
        0: "Draw has not started",
        1: f"Draw is ongoing. Raffle pot size is ${round(seed_amount,2)}",
    }
    print(
        f"""\nWelcome to My Raffle App\n[green][bold]Status:[/] {statuses[status.value]}[/]\n[1] Start a New Draw\n[2] Buy Tickets\n[3] Run Raffle"""
    )
    # print("""[1] Start a New Draw\n[2] Buy Tickets\n[3] Run Raffle\n""")

    # return int(input("""[1] Start a New Draw\n[2] Buy Tickets\n[3] Run Raffle\n"""))


def get_tickets_and_validate() -> list:
    """Get ticket input and validate"""
    usr_ticket_input = input(
        "Enter your name, no of tickets to purchase. Eg: James, 1\n"
    )
    user_ticket_input_list = [t.strip() for t in usr_ticket_input.split(",")]

    if len(user_ticket_input_list) != 2:
        raise ValueError("Invalid input entered")

    try:
        int(user_ticket_input_list[1])
    except Exception:
        raise Exception("[red]Invalid input for number of tickets[/]")

    return user_ticket_input_list
