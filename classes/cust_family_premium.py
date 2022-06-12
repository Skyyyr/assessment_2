from classes.customer import Customer


class FamilyPremium(Customer):
    def __init__(self, customer_id, account_type, first_name, last_name, current_video_rentals):
        # Setup the rental limit
        rental_limit = 3
        super().__init__(customer_id, account_type, first_name, last_name, current_video_rentals, rental_limit)

    def rent_movie(self, movie_to_rent):
        # Only family accounts need to override the 'rent_movie' due to their special restrictions
        if movie_to_rent.rating == "R":
            # Advise the user of the customer's limitation
            print("This customer cannot rent this type of movie due to it's rating.\n")
            return False

        # If we reach this then the customer is trying to rent a movie that isn't rated R
        super().rent_movie(movie_to_rent)
