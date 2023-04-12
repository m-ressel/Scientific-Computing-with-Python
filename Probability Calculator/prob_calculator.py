import random
import copy

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            self.contents += [k] * int(v)

    def draw(self, n):
        if n >= len(self.contents):
            old_self_contents = self.contents
            self.contents = []
            return old_self_contents
        drawn_balls = random.sample(self.contents, n)
        # deleting drawn balls from hat
        for i in drawn_balls:
            if i in self.contents:
                self.contents.remove(i)
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    if not all(item in list(set(hat.contents)) for item in list(expected_balls.keys())):
        return 0
    successes = 0
    list_expected_colors = list(expected_balls.keys())
    for i in range(num_experiments):
        # copying hat as drawing balls remove them from the hat
        hat_copy = copy.deepcopy(hat)
        k = hat_copy.draw(num_balls_drawn)
        # all drawn colors in set
        k_set = set(k)
        chance = 0
        # checking if all expected colors are in the set of drawn balls
        if all(item in k_set for item in list_expected_colors):
            # checking if number of drawn balls is equal or greater than expected value
            for element in list_expected_colors:
                if not k.count(element) >= expected_balls[element]:
                    # if the number of balls in a certain color is smaller than expected, function adds 1 to chance variable
                    chance += 1
            # only if all numbers are greater than expected, function adds +1 to successes
            if chance == 0:
                successes += 1
    # gotten probability of successes in num_experiments experiments
    return successes / num_experiments
