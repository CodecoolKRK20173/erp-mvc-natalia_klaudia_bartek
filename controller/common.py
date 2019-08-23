""" Common functions for controllers
implement commonly used functions here
"""
from model.store import store
from view import terminal_view
import os
from controller import root_controller
def display_clear():
    os.system('cls||clear')


def basic_submenu():
    title = "Store manager\n"
            
    options = ["(1) View table",
                "(2) Add to table",
                "(3) Remove from table",
                "(4) Update table",
                "(6) Return to main menu"]
    argument = None
    choice = None
    while argument != "0":
        choice = terminal_view.get_choice(options)
        if choice == "1":
            store.show(table)
        elif choice == "2":
            store.add(table, record)
        elif choice == "3":
            store.remove(table, id_)
        elif choice == "4":
            store.update(table, id_, record)
        elif choice == "6":
            os.system('cls||clear')
            root_controller.run()
        else:
            terminal_view.print_error_message("There is no such choice.")