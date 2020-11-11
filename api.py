from flask import Flask, request
from taylor import Cosine, Exponential

app = Flask(__name__)


@app.route("/taylor-series/cosine", methods=["GET"])
def taylor_cosine():
    num_terms = request.args.get("num_terms", default=None, type=int)
    cos = Cosine(num_terms)
    return f"cos({num_terms}) = {cos(num_terms)}"


@app.route("/taylor-series/exponential", methods=["GET"])
def taylor_exponential():
    num_terms = request.args.get("num_terms", default=None, type=int)
    exp = Exponential(num_terms)
    return f"exp({num_terms}) = {exp(num_terms)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
