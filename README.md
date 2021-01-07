# Taylor Series Flask

## Overview

An implementation of Taylor Series for Sine, Cosine and Exponential function as Flask application.

## Usage

In this repository, Python 3.8.2 was used and it is recommended to create a virtual environment to isolate the dependencies used by this module.
```
$ virtualenv taylor-series-env
$ source ./taylor-series-env/Scripts/activate
$ pip install -r requirements.txt
```

To use the Taylor Series Flask app for Sine, Cosine and Exponential functions, we have the following view functions:

* `/taylor-series/sine` for Sine. The request parameters for this function are `num_terms` and `value`.
* `/taylor-series/cosine` for Cosine. The request parameters for this function are `num_terms` and `value`.
* `/taylor-series/exponential` for Exponential. The request parameters for this function are `num_terms` and `value`.

To run this app, we can use flask command
```
$ export FLASK_APP=api.py
$ flask run
```

We can also use python -m flask
```
export FLASK_APP=api.py
python -m flask run
```

Or simply use python command
```
python api.py
```

And head over to 
```
http//127.0.0.1:5000/taylor-series/sine?num_terms=10&value=60
```
