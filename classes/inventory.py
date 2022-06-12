class Inventory:
    # This is our inventory which consists of movies!

    def __init__(self, movie_id, title, rating, release_year, copies_available):
        self.movie_id = movie_id
        self.title = title
        self.rating = rating
        self.release_year = release_year
        self.copies_available = copies_available

    def __str__(self):
        # Made an alias to help visualize the output that the user with see
        movie_details = f"Title: {self.title},\n" \
                        f"Movie ID: {self.movie_id},\n" \
                        f"Rating: {self.rating},\n" \
                        f"Current Stock: {self.copies_available},\n" \
                        f"Release Year: {self.release_year}\n"

        # Return the string
        return movie_details
