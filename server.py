"""We are creating a mini Flask server 
    to see the results of using bootstrap """

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("bootstrap.html")




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")