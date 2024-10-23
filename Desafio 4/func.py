import smtplib as slib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(name, value, mail):
    template = f"""
    Olá {name}, gostaríamos de informar que você tem um pagamento pendente no valor de {value}.

    Segue o boleto para pagamento em anexo.
    """

    msg = MIMEMultipart()
    msg['From'] = "seu_email@gmail.com"
    msg['Subject'] = "Pagamento Pendente"
    msg['To'] = mail
    password = 'sua_senha_de_app'
    
    msg.attach(MIMEText(template, 'plain'))
    
    try:
        server = slib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(msg['From'], password)
        server.sendmail(msg['From'], [msg['To']], msg.as_string())
        server.quit()
        
    except Exception as e:
        print(f"Falha ao enviar e-mail para {mail}. Erro: {str(e)}")
