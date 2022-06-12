import csv
import os


class Customer:
    print("HELLO?")
    def __init__(self, customer_id, account_type, first_name, last_name, current_video_rentals):
        self.current_video_rentals = current_video_rentals
        self.last_name = last_name
        self.first_name = first_name
        self.account_type = account_type
        self.customer_id = customer_id
        print(f"{customer_id}, {account_type}, {first_name}, {last_name}, {current_video_rentals}")

    @classmethod
    def create_customers_from_csv(cls):
        print("Triggered")
        customers = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/customers.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                customers.append(Customer(**dict(row)))

        return customers
