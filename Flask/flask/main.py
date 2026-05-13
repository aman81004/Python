from flask import Flask , render_template

'''
It creates an instance of the Flask class,
which will be our WSGI application. The first argument is the name of the application's module or package.
'''
## WSGI application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><body><h1>Welcome to Flask!</h1><p>This is a simple web application.</p></body></html>"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")
    

if __name__ == "__main__":
    app.run(debug=True)