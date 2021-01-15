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

We can also test out our API using curl command in the following manner
```
$ curl http//127.0.0.1:5000/taylor-series/sine?num_terms=10&value=60
```

## License

```
Taylor Series Flask app
Copyright (C) 2021  Abigail A. Marticio

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```