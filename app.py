from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
@app.route("/home")
def goToHome():
    return render_template('home.html')

@app.route("/book")
def bookTicket():
    return render_template('book.html')


@app.route("/admin")
def goToAdmin():
    return render_template('admin.html')

@app.route("/ticket")
def get_ticket():
    name = request.args.get('username')
    phone = request.args.get('phone')
    temp = request.args.get('slot')
    if temp == 's1':
        slot = "Slot 1 From 09:00 ITC"
    elif temp == 's2':
        slot = "Slot 2 From 13:00 ITC"
    elif temp == 's3':
        slot = "Slot 3 From 17:00 ITC"
    else:
        pass
    return render_template('ticket.html',name=name,phone=phone,slot=slot)

if __name__ == "__main__":
    app.run(debug = True)