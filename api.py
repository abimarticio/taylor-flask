from flask import Flask, request
from taylor import Cosine, Exponential, Sine

app = Flask(__name__)


@app.route("/taylor-series/cosine", methods=["GET"])
def taylor_cosine():
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
