class Inventory:
    def __int__(self, movie_id, title, rating, release_year, copies_available):
        self.movie_id = movie_id
        self.title = title
        self.rating = rating
        self.release_year = release_year
        self.copies_available = copies_available

    def __str__(self):
        pass
