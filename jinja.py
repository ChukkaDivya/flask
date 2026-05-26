"""dynamic url
varibale rule
jinja 2 template
{{.....}} - expression to print output in html
{%.....%} - condition and for loops
{#.....#} - comments"""

from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)
@app.route("/")
def home():
    return "<html><h1>This is home page of application using h1</h1></html>"
@app.route("/index",methods=['GET'])
def index():
    return render_template("using_template_index.html",message="Using GET http method")

#variable rule
@app.route("/marks/<int:score>")
def marks(score):
    return "Marks acquired by the candidate is " + str(score)

@app.route("/checkresult/<int:score>")
def checkresult(score):
    res=""
    if score>50:
        res="PASSED"
    else:
        res="FAILED"
    return render_template("checkresult.html",result=res)

##jinja for loop
@app.route('/fruits')
def fruits():
    items=['apple','banana','mango']
    return render_template('fruits.html',fruits=items)

#jinja if condition
@app.route('/checkvote/<int:age>')
def checkvote(age):
    return render_template('checkvote.html',age=age)

#redirecting
@app.route("/submit",methods=["GET","POST"])
def submit():
    total_score=0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])

        total_score = (science + maths + c + data_science) / 4
    else:
        return render_template('getresult.html')

    return redirect(url_for("checkresult", score=total_score))

#runs the application
if __name__=="__main__":
    app.run(debug=True)

