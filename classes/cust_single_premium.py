from classes.customer import Customer


class SinglePremium(Customer):
    def __init__(self, customer_id, account_type, first_name, last_name, current_video_rentals):
        # Setup the rental limit
        rental_limit = 3
        super().__init__(customer_id, account_type, first_name, last_name, current_video_rentals, rental_limit)
