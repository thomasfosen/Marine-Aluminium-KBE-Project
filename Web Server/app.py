from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])

def main():
    customer_form = request.form

    if len(customer_form) > 0:
        forcevalue = customer_form['forcevalue']
        torquevalue = customer_form['torquevalue']
        print(forcevalue, torquevalue)
        if int(forcevalue) > 0 and int(torquevalue) > 0:
            os.system("start /B start cmd.exe @cmd /k start_communicate.bat optimize " + str(forcevalue) + " " + str(torquevalue))

    return render_template('User.html')




if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = '5000')



# The process needs to be launched from a seperate process thread. Doing this inside a flask application wasn't as straight forward as initially thought..
# When initation a secondary thread for this server command inside FLASK, NXOpen doesn't run certain codes for an unknown reason
# os.system("start /B start cmd.exe @cmd /k refresh.bat")
