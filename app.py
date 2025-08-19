print("Starting flask....")

from flask import Flask,request,render_template

app = Flask(__name__) # to confirm the application is written by you

@app.route("/",methods = ["GET","POST"]) # able to get and post

def index():
    return(render_template("index.html"))

@app.route("/main",methods = ["GET","POST"])
def main():
    #database
    return(render_template("main.html"))

if __name__ == "__main__": # to confirm you want to run the vofr
    app.run()
