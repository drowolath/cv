#!/usr/bin/python3
# -*- coding: utf-8 -*-


from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    result = "Hello, world! This is my current CV"
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# EOF
