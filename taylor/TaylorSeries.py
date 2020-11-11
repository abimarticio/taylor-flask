import math


class TaylorSeries(object):
    def __init__(self, num_terms: int):
        self.num_terms = num_terms

    def compute_series(self, x: float) -> float:
        raise NotImplementedError

    def __call__(self, x: float) -> float:
        return self.compute_series(x)

class Cosine(TaylorSeries):
    def compute_series(self, x: float) -> float:
        x = math.radians(x)
        approximation = 0
        for index in range(self.num_terms):
            coefficient = (-1) ** index
            numerator = x ** (2 * index)
            denominator = math.factorial(2 * index)
            approximation += coefficient * (numerator / denominator)
        return approximation


class Exponential(TaylorSeries):
    def compute_series(self, x: float) -> float:
        approximation = 0
        for index in range(self.num_terms):
            numerator = x ** index
            denominator = math.factorial(index)
            approximation += numerator / denominator
        return approximation


class Sine(TaylorSeries):
    def compute_series(self, x: float) -> float:
        x = math.radians(x)
        approximation = 0
        for index in range(self.num_terms):
            coefficient = (-1) ** index
            numerator = x ** (2 * index + 1)
            denominator = math.factorial(2 * index + 1)
            approximation += coefficient * (numerator / denominator)
        return approximation
