from flask import Flask, render_template, request, redirect, url_for

from flask_mail import Mail, Message



def create_app():

    app = Flask(__name__)

    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'josepinadevbusiness@gmail.com'
    app.config['MAIL_PASSWORD'] = 'cbixcbycusltlbhh'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    mail = Mail(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/mail', methods=[ 'GET', 'POST'])
    def send_email():

        if request.method == 'POST':
            name = request.form.get('name')
            subject = request.form.get('subject')
            email = request.form.get('email')
            message = request.form.get('message')


            msg = Message(
                subject = 'Asunto del Mensaje: ' + subject,
                body=f'Nombre: {name}\nEmail: <{email}>\n\nMensaje: {message}',
                sender = email,
                recipients = ['josepinadevbusiness@gmail.com']
            )
            mail.send(msg)
            return render_template('mail.html' )
        
        return redirect(url_for('index'))

    return app

