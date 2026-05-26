from flask import Flask,render_template,request
#create instance of flask(creates flask application)
app=Flask(__name__)
"""Creating Differnt routes of the application
   decorator maps url to the function below"""
@app.route("/")
def home():
    return "<html><h1>This is home page of application using h1</h1></html>"
@app.route("/index",methods=['GET'])
def index():
    return render_template("using_template_index.html",message="Using GET http method")
@app.route("/about")
def about():
    return render_template("using_template_about.html")
@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=="POST":
        name=request.form['name']
        return f"Hello {name}!"
    return render_template("getpost_form.html")
#runs the application
if __name__=="__main__":
    app.run(debug=True)
