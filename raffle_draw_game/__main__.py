"""Raffle entry point script"""
# raffle_draw_game/main.py

from raffle_draw_game import cli, __app_name__


def main():
    cli.app(prog_name=__app_name__)


if __name__ == "__main__":
    main()
