from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p> Hello World!</p>"


@app.route("/info")
def display_info():
    return "This subpage is additional info"


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
