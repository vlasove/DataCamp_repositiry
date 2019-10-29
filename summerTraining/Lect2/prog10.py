class Film:
    def __init__(self, timing, rating, year, title):
        self.Timing = timing
        self.Rating = rating
        self.Year = year
        self.Title = title

    def isGood(self):
        return self.Timing/self.Rating > 6


class Serial(Film):
    def __init__(self, timing, rating, year, title, actors, long):
        super().__init__(timing, rating, year, title)
        self.Actors = actors
        self.Long = long

    def isGood(self):
        pass


s1 = Serial(1, 2, 3, 4, "Dicaprio", 32)
