class TaylorSeries(object):
    def __init__(self, num_terms: int):
        self.num_terms = num_terms

class Exponential(TaylorSeries):

class Sine(TaylorSeries):
    def compute_series(self, x: float) -> float:
        x = math.radians(x)
        approximation = 0
        for index in range(self.num_terms):
            coefficient = ((-1) ** index)
            numerator = x ** (2 * index + 1)
            denominator = math.factorial(2 * index + 1)
            approximation += (coefficient * (numerator / denominator))
        return approximation

