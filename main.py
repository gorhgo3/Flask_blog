import os
from flask import Flask, render_template, request
import requests
from datetime import date
import smtplib

# SETTING ENVIRONMENT VARIABLES (EMAIL)
my_email = os.environ['MY_EMAIL']
sender_email = os.environ['SENDER_EMAIL']
app_password = os.environ['APP_PASSWORD']


URL = 'https://api.npoint.io/f5d3f91dcf787f857eb9'
blog_data = requests.get(url=URL)
blog = blog_data.json()
today = date.today()
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html', date=today, blogs=blog)


@app.route("/hello/<reference>")
def post_page(reference):
    for _ in blog:
        if _['id'] == int(reference):
            print(_)
            return render_template('new_page.html', selected_blog=_, date=today)


@app.route("/contact", methods=['POST', 'GET'])
def receive_data():
    """EMAIL THE MESSAGE TO PERSONAL EMAIL FROM THE CONTACT ME FORM"""
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        # includes environment variables to send contact emails
        PORT = 587
        MESSAGE = f"You received feedback from {name} \n" \
                  f"email:{email}\n phone:{phone}\n" \
                  f"message:{message}" \
                  f""
        with smtplib.SMTP("smtp.gmail.com", port=PORT) as server:
            try:
                server.starttls()
                server.login(sender_email, app_password)
                server.sendmail(from_addr=sender_email, to_addrs=my_email, msg=MESSAGE)
                server.quit()
            except Exception as e:
                print(e)
        return render_template('contact.html', success=True)
    elif request.method == 'GET':
        return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
