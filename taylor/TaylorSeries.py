# Taylor Series Flask app
# Copyright (C) 2021  Abigail A. Marticio

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
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
        """ 
        Computes Taylor Series for Cosine.

        Parameter
        ---------
        x: float
            The value to compute.

        Returns
        -------
        x: float
            The Taylor approximation in Cosine.
        """
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
        """ 
        Computes Taylor Series for Exponential.

        Parameter
        ---------
        x: float
            The value to compute.

        Returns
        -------
        x: float
            The Taylor approximation in Exponential.
        """
        approximation = 0
        for index in range(self.num_terms):
            numerator = x ** index
            denominator = math.factorial(index)
            approximation += numerator / denominator
        return approximation


class Sine(TaylorSeries):
    def compute_series(self, x: float) -> float:
        """ 
        Computes Taylor Series for Sine.

        Parameter
        ---------
        x: float
            The value to compute.

        Returns
        -------
        x: float
            The Taylor approximation in Sine.
        """
        x = math.radians(x)
        approximation = 0
        for index in range(self.num_terms):
            coefficient = (-1) ** index
            numerator = x ** (2 * index + 1)
            denominator = math.factorial(2 * index + 1)
            approximation += coefficient * (numerator / denominator)
        return approximation
