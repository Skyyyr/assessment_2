from classes.customer import Customer


class SingleFree(Customer):
    """
    This
    """
    def __int__(self, customer_id, account_type, first_name, last_name, current_video_rentals):
        rental_limit = 1
        rating_limit = False

        super().__init__(self, customer_id, account_type, first_name, last_name, current_video_rentals,
                         rental_limit, rating_limit)
