import random


class RollResult:
    def __init__(self, has_exploded=False, result=None):
        self.has_exploded = has_exploded
        self.result = result


class Roller:
    def __init__(self, number, sides, explodes=False, explosion_index=None):
        self.sides = sides
        self.number = number
        self.explodes = explodes
        self.explosion_index = explosion_index

    def roll(self):
        roll_results = list()
        results = list()
        try:
            for i in range(0, self.number):
                x = RollResult()
                roll_results.append(x)
            for i in range(0, len(roll_results)):
                roll_results[i].result = random.randint(1, self.sides)
                do_explosions = self.explodes and roll_results[i].result == self.explosion_index and roll_results[
                    i].has_exploded == False
                if do_explosions:
                    x = RollResult(True, random.randint(1, self.sides))
                    roll_results.append(x)

            for r in roll_results:
                results.append(r.result)
        except (ValueError, TypeError):
            return "Anna..."
        return results
