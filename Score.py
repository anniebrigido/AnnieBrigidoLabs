from counter import Counter

#Score class tracks points, scores, and saves the highest score.

class Score:
    #Attributes for Score class
    def __init__(self):
        self.current_score = Counter(1000)
        self.high_score = 0

    #Operations for Score class
    def increment(self, points):
        self.current_score.increment()
        print(f"Score incremented by {points}. Current score: {self.current_score.count}")

    def reset(self):
        self.current_score.reset()
        print("Score reset")

    def save_high_score(self):
        if self.current_score.count > self.high_score:
            self.high_score = self.current_score.count
        print(f"High score saved: {self.high_score}")