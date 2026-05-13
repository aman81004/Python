from flask import Flask

'''
It creates an instance of the Flask class,
which will be our WSGI application. The first argument is the name of the application's module or package.
'''
## WSGI application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to Flask  ! This is a simple web application."


if __name__ == "__main__":
    app.run(debug=True)