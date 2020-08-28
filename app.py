from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def goToHome():
    return render_template('home.html')


@app.route("/admin")
def goToAdmin():
    return render_template('admin.html')
if __name__ == "__main__":
    app.run(debug = True)