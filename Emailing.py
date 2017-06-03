from email.mime.text import MIMEText
from smtplib import SMTP



def mail_checking(email):
    from_address = os.environ.get('EMAIL_USER', None)
    pass = os.environ.get('EMAIL_PASS',None)
    to_address = email
    message = "Hello, world!"
    mime_message = MIMEText(message, "plain")
    mime_message["From"] = from_address
    mime_message["To"] = to_address
    mime_message["Subject"] = "Correo de prueba"
    smtp = SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    print "Conexion exitosa con Gmail"
    print "Concectado a Gmail"
    #
    smtp.login(from_address, "Ym2wlar!")
    smtp.sendmail(from_address, to_address, mime_message.as_string())
    smtp.quit()
    print "fin"
    return None
