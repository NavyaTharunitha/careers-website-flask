from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World,This is Flask!"

if __name__ == '__main__':
    # Make sure it's running on all addresses
    app.run(host='0.0.0.0', debug=True)