class Customer:
    # Our customer class holds all common variables, and handles all common logic.

    def __init__(self, customer_id, account_type, first_name, last_name, current_video_rentals, rental_limit):
        self.rental_limit = rental_limit
        self.current_video_rentals = current_video_rentals
        self.last_name = last_name
        self.first_name = first_name
        self.account_type = account_type
        self.customer_id = customer_id
        self.rental_amount = self.count_rented_movies()

    def __str__(self):
        # Let's grab our current rentals, and replace the / with a nice ,
        movie_string = ', '.join(self.current_video_rentals.split('/'))

        # Just incase a customer doesn't have any movies rented, we just use a nice string
        if movie_string == "":
            movie_string = "No movie currently rented."

        # Let's display the customer info/movie list nicely.
        return f"Customer ID: {self.customer_id},\nMovies: {movie_string}\n"

    # We use this to help keep our movie count up to date, and repeated use of the logic
    def count_rented_movies(self):
        # If they don't have any movie's rented just return 0
        if self.current_video_rentals == "":
            return 0

        # Split up the string of rented movies if we can
        current_movies = self.current_video_rentals.split('/')

        # Return the length of the movie list
        return len(current_movies)

    def rent_movie(self, movie_to_rent):
        """
        * Only logic that all customer accounts share should be in here *

        Prior to calling this method - 'movie_to_rent' has been verified as an actual movie, and is the instanced object
        1. We ensure that the movie has at least one copy available for the customer to rent
        2. We ensure that the customer has at least one rental slot available from their account limit
        3. Add the movie to the list
            a. If the customer has at least one movie rented already, then apply the separator
        4. Update the rental amount for the customer

        :param movie_to_rent: Instanced object of the 'movie'
        :return: True or False
        """
        # If the movie is out of stock, we can just stop here, otherwise proceed
        if int(movie_to_rent.copies_available) < 1:
            print(f"There are no available copies of {movie_to_rent.title}\n")
            return False

        # If the customer cannot rent a movie, then no need to proceed, advise about limitation
        if self.rental_amount >= self.rental_limit:
            print(f"Customer ID: {self.customer_id} has reached their rental limit, "
                  f"therefor unable to rent {movie_to_rent.title}")
            return False

        # If we are dealing with a customer that has at least one rental, then we need our separator
        if self.current_video_rentals != "":
            # Add separator before we add the movie title
            self.current_video_rentals += "/"

        # We add the movie title to the current rentals
        self.current_video_rentals += movie_to_rent.title

        # We update our rental amount
        self.rental_amount += 1

        # We update the copies available since we have the object available
        # Convert to int, decrement, then update the value
        movie_to_rent.copies_available = int(movie_to_rent.copies_available) - 1

        # Successful rental has taken place
        return True

    def does_customer_have_movie(self, requested_movie):
        """
        This is our little helper method that we use to give us a specific failure/success reason
        :param requested_movie: The movie Object in question
        :return: True or False
        """
        # Let's grab our current movies separately
        current_movies = self.current_video_rentals.split('/')

        # Iterate over each movie in the list and see if we can find a matching title in the customer's rental list
        for movie in current_movies:
            # movie is the 'title' of the rented movie in the customer's rental list
            if movie == requested_movie.title:
                # We found it!
                return True

        # No movie with that title was found in the customer's rental list
        return False

    def return_movie(self, movie_to_return):
        # Step 1: Update the customer's rental list

        # Set up the customer's rental list
        rental_list = list(self.current_video_rentals.split('/'))

        # Let's make a variable that will be our new list of rented movies (if there are any)
        updated_rental_list = ""

        # Let's iterate over each title and compare to the 'movie_to_return' 's title
        for rental in rental_list:
            # "If these aren't the movies we're looking for" then add them to the customer's rental list
            if rental != movie_to_return.title:
                # If this isn't the first movie being added to the updated list, then add a separator
                if updated_rental_list != "":
                    updated_rental_list += "/"

                # This isn't the movie we're looking for, add it to the new rental list now
                updated_rental_list += rental

        # We have excluded the movie to be returned, let's update our rentals
        self.current_video_rentals = updated_rental_list

        # Step 2: Update rental count
        self.rental_amount -= 1

        # Step 3: Update the movie's stock
        movie_to_return.copies_available = int(movie_to_return.copies_available) + 1

    # # This is how we update the csv with new customers
    # @classmethod
    # def add_new_customer_csv(cls, data_as_dict):
    #     with open('data/customers.csv', 'a+', newline='') as file:
    #         field_names = ['customer_id', 'account_type', 'first_name', 'last_name', 'current_video_rentals']
    #         writer = csv.DictWriter(file, field_names)
    #
    #         if file.tell() == 0:
    #             # Just incase our stored file doesn't exist we write a new one with the headers
    #             writer.writeheader()
    #         # Add the new customer to the bottom of the list
    #         writer.writerow(data_as_dict)
