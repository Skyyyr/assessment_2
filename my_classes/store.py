from classes.customer import Customer
"""
This class is the 'middle-man' between the inventory, and customer classes.

The Store class is our central location regarding any sort of information, or taking any actions.

The main or sub loops should only call this class, and not inventory or customer.
"""


class Store:
    print("STORE HI")
    def __int__(self):
        print("MADE STORE")
        self.customers = Customer.create_customers_from_csv()
        print(self.customers)

    def list_all_customers(self):
        output = ""
        for customer in self.customers:
            first_name = customer.first_name
            last_name = customer.last_name
            cust_id = customer.customer_id
            current_rentals = customer.current_video_rentals
            account_type = customer.account_type
            output += f"{first_name} {last_name} {cust_id} {current_rentals} {account_type}\n"
        return output
