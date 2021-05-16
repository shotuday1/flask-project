from flask import Flask
import json

app = Flask(__name__)


@app.route('/api/india')
def hello_world():
    return json.dumps('Hello, India data given')


@app.route('/api/us')
def hello_uday():
    return json.dumps('Hello, Us Data given!')


if __name__ == '__main__':
    app.run()
