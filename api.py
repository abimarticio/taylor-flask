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
from flask import Flask, request
from taylor import Cosine, Exponential, Sine

app = Flask(__name__)


@app.route("/taylor-series/cosine", methods=["GET"])
def taylor_cosine():
    """ 
    GET request for Taylor Series in Cosine.

    Request Parameters
    ---------
    num_terms: int
        The number of terms to compute.
    value: int
        The value to compute.

    Returns
    -------
    string
        The result of Taylor approximation in Cosine.
    """
    num_terms = request.args.get("num_terms", default=None, type=int)
    value = request.args.get("value", default=None, type=int)
    cos = Cosine(num_terms)
    return f"cos({value}) = {cos(value)}"


@app.route("/taylor-series/exponential", methods=["GET"])
def taylor_exponential():
    num_terms = request.args.get("num_terms", default=None, type=int)
    value = request.args.get("value", default=None, type=int)
    exp = Exponential(num_terms)
    return f"exp({value}) = {exp(value)}"


@app.route("/taylor-series/sine", methods=["GET"])
def taylor_sine():
    num_terms = request.args.get("num_terms", default=None, type=int)
    value = request.args.get("value", default=None, type=int)
    sin = Sine(num_terms)
    return f"sin({value}) = {sin(value)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
