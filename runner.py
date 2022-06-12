import csv
import os

# Let's import our custom classes
from classes.store import Store
from classes.inventory import Inventory

# To help make our code below look neater, and readable we set up constants for each menu and sub menu

# Main menu
MAIN_MENU_TEXT = "--== Welcome to Block Buster's Inventory Management System ==--\n" \
                 "1. View store inventory\n" \
                 "2. View customer rented videos\n" \
                 "3. Add new customer\n" \
                 "4. Rent a video\n" \
                 "5. Return a video\n" \
                 "6. Exit\n"

# We want to allow the user to set the pace of how the app refreshes menus
CONTINUE = "Enter any key to continue...\n"

# This is so we can change only the text we want to change instead of the entire string
SUB_LIST_TEXT = "Select an option from below:\n" \
                "1. {option_one}\n" \
                "2. {option_two}\n" \
                "Otherwise enter any key to go back to the main menu.\n"


def iterate_with_input(list_of_data):
    """
    This is a helper function that helps us iterate over any list and allow the user to quit at any time

    The purpose of this is to allow the user to view a list one item at a time

    :param list_of_data: list
    :return: void
    """
    for data in list_of_data:
        # Simply print the data - If it's an object __str__ needs to be setup for proper text display
        print(f"{data}")
        # Allow the user to back out after we display each item in the list
        user_input = input("Enter Q to quit to the main menu, or any key to continue through the list...\n")
        if user_input == "Q":
            break


def create_inventory_from_csv():
    """
    This should only be used on start-up to initiate our inventory list
    :return: entire list of inventory
    """
    inventory = []
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "data/inventory.csv")

    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            inventory.append(Inventory(**dict(row)))

    return inventory


def create_customers_from_csv():
    """
    This should only be used on start-up to initiate our customer list
    :return: entire list of customers
    """
    customers = []
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "data/customers.csv")

    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # We need to find out what type of account we are opening, and open the correct one
            # We use our store class method 'create_customer_by_type' to identify and create the proper child class
            customer_obj = Store.create_customer_by_type(row)

            # Append the newest customer to our customer list
            customers.append(customer_obj)

    # return the entire list of customers
    return customers


# This is the main menu
def main_menu():
    # Start-up the blockbuster!
    block_buster = Store("Block Buster")

    # On start-up let's grab our stored CSV data
    block_buster.customers = create_customers_from_csv()
    block_buster.inventory = create_inventory_from_csv()

    # Let's keep looping til we exit the application.
    while True:
        # Display the main menu text each time
        user_input = input(MAIN_MENU_TEXT)

        # "1. View store inventory\n"
        if user_input == "1":
            # "Select an option from below:\n"
            user_input = input(SUB_LIST_TEXT.format(option_one="View the entire store's movie stock at once",
                                                    option_two="View one movie at a time"))

            # "1. View the entire store's movie stock at once"
            if user_input == "1":
                # This just spams the terminal with the entire list of the store's stock
                print(block_buster.list_current_stock())

                # We don't want to force the main menu on the user until they've been given time to review the list
                input(CONTINUE)

            # "2. View one movie at a time"
            elif user_input == "2":
                # We use our helper function that allows the user to cycle through each item in the list one at a time
                iterate_with_input(block_buster.inventory)

        # "2. View customer rented videos\n"
        elif user_input == "2":
            # "Select an option from below:\n"
            user_input = input(SUB_LIST_TEXT.format(option_one="Find customer by ID",
                                                    option_two="View one customer at a time"))

            # "1. Find customer by ID"
            if user_input == "1":
                # Let the user give a potential valid ID
                user_input = input("Input customer ID:\n")

                # We use our helper function to find the user id, or advise the user that they don't exist
                customer = block_buster.get_customer_by_id(user_input)

                # Display the output results
                if customer is not None:
                    print(customer)

                # No customer found with this ID
                else:
                    print("The customer ID was entered was invalid.\n")

                # Let the user decide when to continue
                input(CONTINUE)

            # "2. View one customer at a time"
            elif user_input == "2":
                # We use our helper function that allows the user to cycle through each item in the list one at a time
                iterate_with_input(block_buster.customers)

        # "3. Add new customer\n"
        elif user_input == "3":
            # We use our helper function 'gather_new_customer_data' to grab the customer's data from the user
            new_customer = gather_new_customer_data()

            # We make sure that they have valid data, or if the user elected to return to the main menu
            if new_customer is not None:
                # Our helper function ensures that we get the proper args to do this call
                block_buster.add_customer(*new_customer)

        # "4. Rent a video\n"
        elif user_input == "4":
            # Take us to the rental sub menu
            gather_movie_rental_data(block_buster)

        # "5. Return a video\n"
        elif user_input == "5":
            # Take us to the return sub menu
            return_movie(block_buster)

        # "6. Exit\n"
        elif user_input == "6":
            # Goodbye!
            print("Signing out...")
            exit()

        # else refresh the menu


def gather_new_customer_data():
    """
    This is a sub menu that handles obtaining valid data for creating a new customer,
    this sub menu also allows the user to exit the menu without an issue.
    The user must confirm the account data after all the required data is obtained.
    :return: customer data (first name, last name, account type)
    """
    # Let's setup our variables
    step = 0
    first_name = ""
    last_name = ""
    account_type = ""

    # Let's keep looping til we return
    while True:
        # Get the customer's First and Last name
        if step == 0:
            # We will do a version of "tokenize" for our full name input
            full_name = input("Enter the customer's full name: (Q to quit to main menu)\n"
                              "Example:\n"
                              "First Last\n"
                              "John Smith\n")

            # We do our base case catch to let the user go back to the main menu
            if full_name == "Q":
                # Quit the sub menu
                return None

            # "tokenize" (not real tokenization) our full name
            split_name = full_name.split(' ')

            # Ensure it's 2 words (Customers with multiple last names will have to use ' or -)
            if len(split_name) == 2:
                # Assign the first and last name variables accordingly
                first_name, last_name = split_name
                step += 1

            # The customer name that was entered did not get entered correctly
            else:
                # Advise the user about the invalid entry
                print("The name entered was invalid, please try again.\n")

        # Establish the customer's account type starting with free or premium
        if step == 1:
            # "Select an option from below:\n"
            user_input = input(SUB_LIST_TEXT.format(option_one="Premium Account",
                                                    option_two="Free Account"))

            # "1. Premium Account"
            if user_input == "1":
                account_type += "p"
                step += 1

            # "2. Free Account"
            if user_input == "2":
                account_type += "s"
                step += 1

        if step == 2:
            # "Select an option from below:\n"
            user_input = input(SUB_LIST_TEXT.format(option_one="Family Account",
                                                    option_two="Standard Account"))

            # "1. Family Account"
            if user_input == "1":
                account_type += "f"
                step += 1

            # "2. Standard Account"
            if user_input == "2":
                account_type += "x"
                step += 1

        # We confirm the entries or deny
        if step == 3:
            # Add to our sub menu text
            confirmation_text = "Please confirm that the information is correct:\n" \
                                f"Customer Full Name: {first_name} {last_name}\n" \
                                f"Account Type: {account_type}\n" \
                                "Select an option from below:\n" \
                                "1. {option_one}\n" \
                                "2. {option_two}\n"

            # "Select an option from below:\n"
            user_input = input(confirmation_text.format(option_one="Confirm Account",
                                                        option_two="Restart"))

            # "1. Confirm Account"
            if user_input == "1":
                # The customer details have been confirmed, return them so we can finalize the account creation
                return first_name, last_name, account_type

            # "2. Restart"
            if user_input == "2":
                # We reset the variable data to ensure that no old data is used
                step = 0
                first_name = ""
                last_name = ""
                account_type = ""


def gather_movie_rental_data(block_buster):
    """
    We gather the users input to ensure we get valid params for a movie to be rented
    :param block_buster:
    :return: void
    """
    # Let's setup variables for our menu
    step = 0
    movie = ""
    customer = ""

    # Let's keep looping until we break out of it | breaking out will return us to the main menu
    while True:
        # Gather the title of the movie
        if step == 0:
            user_input = input("Enter the title of the movie that the customer would like to rent.\n"
                               "(Q to go back to menu)\n")

            # If we have some kind of input let's attempt to use it as a title
            if user_input != "":
                # (Q to go back to menu)
                if user_input == "Q":
                    break

                # Let's see if we have the movie in stock
                movie = block_buster.get_movie_by_title(user_input)

                # If we found the movie in our potential stock of movies
                if movie is not None:
                    step += 1

                # The entered movie was not found!
                else:
                    # Looks like a customer wants a movie we don't have.
                    print(f"{user_input} is not a valid movie title. Please try again.\n")

        # Confirm the movie title before continuing or let them retry
        if step == 1:
            # Add to our sub menu text
            confirmation_text = "Please confirm that the information is correct:\n" \
                                f"Movie Title: {movie.title}\n" \
                                "1. {option_one}\n" \
                                "2. {option_two}\n"

            # "Select an option from below:\n"
            user_input = input(confirmation_text.format(option_one="Confirm movie title",
                                                        option_two="Select a different movie"))

            # "1. Confirm movie title"
            if user_input == "1":
                step += 1

            # "2. Select a different movie"
            if user_input == "2":
                step = 0
                movie = ""

        # Gather the customer ID from the user
        if step == 2:
            # Let's try to get the customer's ID
            user_input = input("Enter the customer's ID that would like to rent this movie.\n")

            # If we get some kind of input let's try to do something with it
            if user_input != "":
                # Let's try to find the customer's ID
                customer = block_buster.get_customer_by_id(user_input)

                # If we found a customer in our list that matched that ID
                if customer is not None:
                    step += 1

                # No customer found at this ID
                else:
                    # Didn't find a customer with that ID
                    print("Invalid entry, please try again.\n")

        # Confirm Customer ID
        if step == 3:
            # Set up our confirmation text
            additional_text = "Please confirm the customer ID:\n" \
                              f"Customer ID: {customer.customer_id}\n"

            # "Select an option from below:\n"
            user_input = input(additional_text + SUB_LIST_TEXT.format(option_one="Confirm",
                                                                      option_two="Re-select customer ID"))

            # "1. Confirm"
            if user_input == "1":
                step += 1

            # "Re-select customer ID"
            if user_input == "2":
                step -= 1
                customer = ""

        # We have confirmed all the information up to this point, let's see if the customer can actually rent the movie.
        if step == 4:
            # We call 'rent movie' to handle the rest - it'll also tell us our failure reason if there is one.
            if customer.rent_movie(movie):
                # The customer can indeed rent this movie, so we send a nice confirmation message
                print(f"Success:\nCustomer: {customer.customer_id} has rented the movie: {movie.title}.\n")

                # Allow the user to decide when to continue
                input(CONTINUE)
                break

            # The customer cannot rent the movie, reset their step
            else:
                # Each failure has a message preset to its condition, so just set step to 0
                step = 0


def return_movie(block_buster):
    """
    This is our sub menu for returning a movie.
    In this menu we ensure valid movie titles, and customer IDs. Along with those validations, with ensure the
    customer (if a valid customer is found) has at least one movie rented.

    * Additional logic could be added to automatically let customers with only one movie rented to simply return it
    instead of inquiring about the title.
    :param block_buster:
    :return:
    """
    # Setup variables
    step = 0
    customer = ""
    movie = ""

    # Loop over the menu until the user 'break's it
    while True:
        # Get the customer's ID that is trying to return a movie
        if step == 0:
            # Let's try to get the customer's ID
            user_input = input("Enter the customer's ID that would like to return a movie.\n"
                               "(Q to go back to menu)\n")

            # If we get some kind of input let's try to do something with it
            if user_input != "":
                # (Q to go back to menu)
                if user_input == "Q":
                    break

                # Let's try to find the customer's ID
                customer = block_buster.get_customer_by_id(user_input)

                # If we found a customer in our list that matched that ID
                if customer is not None:
                    # Since we found a valid customer, we can immediately check if they even have a movie rented
                    if customer.rental_amount < 1:
                        # Let the user know
                        print("This customer doesn't have a rented movie.\n")

                    # The customer has at least one movie rented, so continue
                    else:
                        step += 1

                # We didn't find a valid customer ID, let them try again.
                else:
                    # Didn't find a customer with that ID
                    print("Invalid customer ID, please try again.\n")

        # Get the title of the movie that the customer is trying to return
        if step == 1:
            # Let the user input the movie title that the customer is attempting to return
            user_input = input("Enter the title of the movie that the customer would like to return.\n")

            # If we have some kind of input let's attempt to use it as a title
            if user_input != "":
                # Let's see if the user input a correct movie; grab the movie object
                movie = block_buster.get_movie_by_title(user_input)

                # If we found the movie in our potential stock of movies
                if movie is not None:
                    step += 1

                # Looks like a customer wants return a movie we don't have.
                else:
                    # Advise the user of the issue
                    print(f"please provide a valid movie title.\n")

        # Let the customer know they have returned the movie
        if step == 2:
            # Let's find out if the customer has the movie rented.
            if customer.does_customer_have_movie(movie):
                # We have verified the customer ID, and that the customer has this movie rented, let's return it
                customer.return_movie(movie)

                # Let's advise the user about the return
                print(f"Customer: {customer.customer_id} has returned the movie {movie.title}.\n")

                # Let the user review the information before being sent back to the main menu
                input(CONTINUE)
                break

            # The customer is not currently renting this particular movie
            else:
                # Reset the user's step, and advise them of the failure
                print(f"The Customer doesn't a rental out with this title: {movie.title}\n")
                step = 0


# This call starts the program
main_menu()
