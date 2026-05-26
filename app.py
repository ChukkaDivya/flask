from flask import Flask
#create instance of flask(creates flask application)
app=Flask(__name__)
"""Creating Differnt routes of the application
   decorator maps url to the function below"""
@app.route("/")
def home():
    return "Welcome to Home page of Flask application"
@app.route("/index")
def index():
    return "This is index page of Flask application"
@app.route("/about")
def about():
    return "This is about page of Flask application "
#runs the application
if __name__=="__main__":
    app.run(debug=True)
