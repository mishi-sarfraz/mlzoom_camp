from flask import Flask
import pickle
# import pandas as pd
# from Flask import Flask, request, json
app=Flask('ping')
@app.route('/ping',methods=['GET'])
def ping():
    return 'Pong'
if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=9696)
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "Hello, world!"

# if __name__ == "__main__":
#     app.run(debug=True)