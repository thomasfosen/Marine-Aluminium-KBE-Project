from flask import Flask, render_template, request



app = Flask(__name__)


@app.route('/', methods=['GET','POST'])

def main():

    customer_form = request.form

    return render_template('User.html')



if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = '5000')
