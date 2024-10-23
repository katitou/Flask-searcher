from flask import Flask


app = Flask(__name__)

if __name__ == '__main__': 
    from routes import *
    app.run(debug=True)