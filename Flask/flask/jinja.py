## Building url dynamically
## variable rule
## Jinja2 template engine

'''
{{}} is used to evaluate expressions and print the result in the template.
{% %} is used to execute statements, such as loops and conditionals, in the template.
{# #} is used for comments in the template, which will not be rendered in the final output.
'''


from flask import Flask , render_template, request

## WSGI application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><body><h1>Welcome to Flask!</h1><p>This is a simple web application.</p></body></html>"

@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/submit", methods=["GET","POST"])
def submit():
    if request.method == "POST":
        name = request.form.get("name")
        return f"<html><body><h1>Hello, {name}!</h1><p>Thank you for submitting the form.</p></body></html>"
    return render_template("form.html")

## variable rule
@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score >= 50:
        res = "Passed"
    else:
        res = "Failed"
    return render_template("result.html", result=res)

if __name__ == "__main__":
    app.run(debug=True)