from flask import Flask, render_template, request

import json
import re
import os
import random
import time

#from Reasoner import Reasoner

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])

def main():

    customer_form = request.form
    
    return render_template('User.html')






if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = '5000')



#  #<form class="" action="{{ url_for('User') }}" method="post">
