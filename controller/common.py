""" Common functions for controllers
implement commonly used functions here
"""
from model.store import store
from view import terminal_view
import os

def display_clear():
    os.system('cls||clear')


def basic_submenu():
    title = "Store manager\n"

    options = ["(1) View table",
                "(2) Add to table",
                "(3) Remove from table",
                "(4) Update table",]

    exit_message = "(0) Back to main menu\n"
    
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(title, options, exit_message)
        if choice == "1":
            store.show(table)
        elif choice == "2":
            store.add(table, record)
        elif choice == "3":
            store.remove(table, id_)
        elif choice == "4":
            store.update(table, id_, record)
        else:
            terminal_view.print_error_message("There is no such choice.")