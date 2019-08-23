# everything you'll need is imported:
from view import terminal_view
from controller import store_controller
from controller import hr_controller
from controller import inventory_controller
from controller import accounting_controller
from controller import sales_controller
from controller import crm_controller
from controller import common
import os


def run():

    os.system('cls||clear')

    title = "Main menu\n"

    options = ["(1) Store manager",
               "(2) Human resources manager",
               "(3) Inventory manager",
               "(4) Accounting manager",
               "(5) Sales manager",
               "(6) Customer Relationship Management (CRM)"]
    
    exit_message = "(0) Exit program\n"

    argument = None
    choice = None
    while argument != "0":
        choice = terminal_view.get_choice(title, options, exit_message)
        if choice == "1":
            store_controller.run()
        elif choice == "2":
            hr_controller.run()
        elif choice == "3":
            inventory_controller.run()
        elif choice == "4":
            accounting_controller.run()
        elif choice == "5":
            sales_controller.run()
        elif choice == "6":
            crm_controller.run()
        elif choice == "0":
            argument = terminal_view.kutas_kurwa()
        else:
            terminal_view.print_error_message("There is no such choice.")