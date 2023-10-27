from email.message import EmailMessage
import smtplib
import ssl
import os
import mimetypes

email_senha = open('pass', 'r').read()
email_origem = 'seuemail@gmail.com'
email_distino = ('emaildestino@gmail.com')
email_origem
assunto = "Orçamento de produtos"

body = open('corpo_email_html.txt', 'r').read()

mensagem = EmailMessage()

mensagem['From'] = email_origem
mensagem['To'] = email_distino
mensagem['Subject'] = assunto

anexo_path = "imagem.png"
mime_type, mime_subtype = mimetypes.guess_type(anexo_path)[0].split('/')

mensagem.set_content(body, subtype='html')
safe = ssl.create_default_context()

with open(anexo_path, "rb") as ap:
    mensagem.add_attachment(ap.read(), maintype=mime_type,
                            subtype=mime_subtype, filename=anexo_path)


with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(email_origem, email_senha)
    smtp.sendmail(email_origem, email_distino, mensagem.as_string())
