# in app.py
# import flask
from flask import Flask, render_template, request
import subprocess
import time 

# config app
app = Flask(__name__)

from algotrader import *
import time

sleep = time.sleep(5)

account = api.get_account()
actstat = account.status
actbp=account.buying_power
clock = api.get_clock()
portfolio = api.list_positions()
print("The market is open: {}".format(clock.is_open))





# make route!
@app.route('/')
def home():
    
    """
     want to run program when button is clicked.
     might want to have button as T/F value, then if true, runs trader. 
     need to make sure trader only runs once, cant keep starting it.
    """

    
    return render_template("basic.html", run=run,  portfolio=portfolio, actstat=actstat, actbp=actbp, clock=clock)




@app.route('/info')
def info():
    
    return render_template("info.html", start_date=start_date)

@app.route('/login')
def login():
    return render_template('login.html')



@app.route('/get_data')
def get_data():
    x = 0
    return render_template('runpy.html', sleep=sleep, portfolio=portfolio, actstat=actstat, actbp=actbp, clock=clock, start_date=start_date, run=run, x=x)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404







if __name__ == '__main__':
    app.run(debug=True)