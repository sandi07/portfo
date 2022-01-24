from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def hello_world():
    # return 'Hello World!!!'
    return render_template('index.html')


# page_name is dynamic ---> ie index.html , about.html , works.html , work.html , about.html , component.html
@app.route('/<string:page_name>')
def page_name(page_name):
    # return 'Hello World!!!'
    return render_template(page_name)


# --------Write form data to txt file

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n Email : {email}, Subject:{subject}, Message: {message}')


# --------Write form data to CSV file

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # print(data)
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')

        except:
            return "did not saved database"
    else:
        return 'something went wrong'


if __name__ == '__main__':
    # app.debug = True
    # app.run(port=8080)
    app.run(port=8080, debug=True)  # function call by the app
