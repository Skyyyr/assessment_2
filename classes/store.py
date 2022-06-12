from classes.cust_family_free import FamilyFree as fam_free
from classes.cust_family_premium import FamilyPremium as fam_premium
from classes.cust_single_free import SingleFree as standard_free
from classes.cust_single_premium import SinglePremium as standard_premium

SEPERATOR = "______________________________"


class Store:
    # This is the store class that assists in creating new customers, and retrieving data

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.inventory = []

    def list_current_stock(self):
        # List all our stock
        output = "--== Current store stock ==--\n"
        for video in self.inventory:
            # We set up aliases just to help visualize the output that the user will see
            movie_id = video.movie_id
            title = video.title
            rating = video.rating
            release_yr = video.release_year
            current_stock = video.copies_available

            # Concat the output string - Display the output like the user would see it
            output += f"Title: {title},\n" \
                      f"Movie ID: {movie_id},\n" \
                      f"Rating: {rating},\n" \
                      f"Current Stock: {current_stock},\n" \
                      f"Release Year: {release_yr}\n{SEPERATOR}\n"

        # We've iterated over the entire store's inventory, let's return the string
        return output

    def get_customer_by_id(self, requested_id):
        # Let's find the customer ID in our list of objects and return it if we can
        for customer in self.customers:
            if customer.customer_id == requested_id:
                # We found you! Return the instanced object
                return customer

        # No customer was found, return None

    def get_movie_by_title(self, requested_title):
        """
        we find the movie and return the instanced object
        if we don't find the object we return None
        :param requested_title: the title of the movie that is being requested
        :return: void
        """
        for movie in self.inventory:
            if movie.title == requested_title:
                # We found you! Return the instanced movie object
                return movie

        # No movie was found, return None

    def add_customer(self, first_name, last_name, account_type):
        """
        Before this method is called, we have ensured that each param is legal.
        We use this method to create new customers, we should also save them to the stored csv as well.
        """
        # We set up the new customer with the custom data, and ensure a unique id
        new_customer = {
            'first_name': first_name,
            'last_name': last_name,
            'account_type': account_type,
            'customer_id': str(len(self.customers) + 1),
            'current_video_rentals': "",
        }

        # Now we need to figure out what type of account we are opening
        customer_obj = self.create_customer_by_type(new_customer)

        # We add the new customer to the customer list
        self.customers.append(customer_obj)

    @classmethod
    def create_customer_by_type(cls, new_customer):
        """
        We need to make the appropriate account for the customer, we need to make an instance of
        the class and pass that to the customers list
        :param new_customer: This is the new customer that we need to now make an account for
        :return: customer_obj: the instance of the customer class
        """
        # Let's make a variable that we will return
        customer_obj = None
        # Just an alias for account type from the dictionary
        account_type = new_customer['account_type']

        # Create the account based off of the account type
        if account_type == "sx":
            customer_obj = standard_free(**new_customer)

        elif account_type == "sf":
            customer_obj = fam_free(**new_customer)

        elif account_type == "px":
            customer_obj = standard_premium(**new_customer)

        elif account_type == "pf":
            customer_obj = fam_premium(**new_customer)

        # After we create the account, return the instanced object, so we can keep track of it in our customer list
        return customer_obj
