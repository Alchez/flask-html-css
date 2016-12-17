from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail()

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USERNAME='<contact@domain.com>',
    MAIL_PASSWORD='<password>',
    MAIL_USE_TLS=False,
    MAIL_USE_SSL=True
)

mail.init_app(app)


@app.route('/')
@app.route('/<name>/')
def index(name=None):
    author = "Rohan"
    return render_template('homepage.html', name=name, author=author)


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    email = request.form['email']
    msg = Message("Hello",
                  sender=("Rohan", "rohanbansal33@gmail.com"),
                  recipients=[email])
    msg.body = "Thanks for subscribing to #CatFacts!"
    mail.send(msg)
    return render_template('confirmation.html', email=email)


if __name__ == '__main__':
    app.run()
