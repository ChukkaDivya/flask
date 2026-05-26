from flask import Flask,render_template
#create instance of flask(creates flask application)
app=Flask(__name__)
"""Creating Differnt routes of the application
   decorator maps url to the function below"""
@app.route("/")
def home():
    return "<html><h1>This is home page of application using h1</h1></html>"
@app.route("/index")
def index():
    return render_template("using_template_index.html")
@app.route("/about")
def about():
    return render_template("using_template_about.html")
#runs the application
if __name__=="__main__":
    app.run(debug=True)
