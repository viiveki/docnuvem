import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime
import model.email as dbemail

# Constantes
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

SENDER = 'vinicius@docnuvem.com.br'
PASS_APP = 'tohw auqm vonm sxex'

PATHFILE = 'documents/DOCMelhoria_{filename}.pdf'.format(filename=datetime.today().strftime('%Y-%m-%d'))

def create_email(email_server):
    # Destinatarios
    # #mail['To'] = dbemail.get_all()
    recipient = 'breno@docnuvem.com.br, vinicius@docnuvem.com.br, jessica@certificaminas.com, michele@certificaminas.com, juridico@novoaeon.com.br, credenciamento@certificaminas.com, luiz.gustavo@certificaminas.com, stella.ribeiro@certificaminas.com, julia@certificaminas.com, francisco.pena@bry.com.br, karol@bry.com.br, rafael@bry.com.br, sabrina.melo@bry.com.br, lorenacertificado@gmail.com, thiago@gcincocontabil.com.br, felipe@gcincocontabil.com.br, Gustavo@gcincocontabil.com.br, patricia@rmcertificados.com.br, contato@rmcertificados.com.br, endrioestanislau@gmail.com, alvesinvestiga@gmail.com, gabrielle.manhaes@yahoo.com, thihpires@gmail.com, alineffumagali@gmail.com, andressa.ascel@gmail.com, kellygerlach95@gmail.com, leandroscortegagna@gmail.com, lhpiresconsultoria@gmail.com, nathgoettems@hotmail.com, ar@mercantec.com.br, moacir@mercantec.com.br, camila@avantejuntos.com.br, rh@avantejuntos.com.br, pryscilla@avantejuntos.com.br, brunamoreira@cerdigitalmg.com.br, otavio@cerdigitalmg.com.br, lidiane.marques@certfacil.com.br, administrativo@virtualcert.com.br, robson_souza@sicredi.com.br, erick_willian@terceiros.sicredi.com.br, lins_bruno@sicredi.com.br, ana_calmeida@sicredi.com.br, adm@zayincertificado.com.br, gerencia@zayincertificado.com.br, gustavo@solucaodigitalsc.com.br, gustavo.mohr@syngularid.com.br, fabiana.araujo@syngularid.com.br, francisco.pena@bry.com.br, karol@bry.com.br, rafael@bry.com.br, sabrina.melo@bry.com.br, igor.efetiva@gmail.com, rtgdepoa@gmail.com, eduardo@libellumdigital.com.br, luizgustavo@libellumdigital.com.br, paulomachado@libellumdigital.com.br, contato@rmcertificados.com.br, Arnaldo.ribeiro@grupovaldirsaraiva.com.br, felipe.maia@grupovaldirsaraiva.com.br, contato@insigner.com.br, financeiro@minascomercial.com.br, milena.poletto@devzdigital.com, ines.picoli@devzdigital.com, erodi@atena.digital, mariahelena@certbr.com, credenciamento@certbr.com, natan@vexcertificadora.com.br, veigameneses@gmail.com, ketlyn@gcert.com.br, mariana@gcert.com.br, daniel.veiga@prisminas.com.br, marcela@legallab.com.br, mariane@legallab.com.br, contato@andrearaujoadvogados.com.br, adv.andrearaujo@gmail.com, ketlyn@gcert.com.br, mariana@gcert.com.br, veigameneses@gmail.com, financeiro@minascomercial.com.br, natan@vexcertificadora.com.br, igor.pedroso@docnuvem.com.br, jessica.castro@docnuvem.com.br'


    # MIMEMultipart cria um container para um mensagem de email que pode conter diferentes partes.
    message = MIMEMultipart()

    # Assunto do email
    message['Subject'] = 'DOCNUVEM - Últimas Melhorias Implementadas'
    message['From'] = SENDER
    message['To'] = recipient

    # Corpo do email
    body = '''
            Prezado(a) usuário(a),

            Estamos constantemente trabalhando para melhorar a experiência e a eficiência no uso do Docnuvem. Segue abaixo o documento explicativo com os detalhes das últimas melhorias desenvolvidas para a plataforma. Essas atualizações visam otimizar a organização e automação dos processos documentais, trazendo ainda mais praticidade e segurança ao seu dia a dia.

            Agradecemos por continuar utilizando o Docnuvem e estamos à disposição para esclarecer qualquer dúvida.

            Atenciosamente,
            Equipe Docnuvem
           '''
    
    # Associa a mensagem ao email a ser enviado
    message.attach(MIMEText(body))
    
    # Associa o arquivo ao email a ser enviado
    with open(PATHFILE, 'rb') as file:
        message.attach(MIMEApplication(file.read(), Name="Melhoria_Docnuvem.pdf"))
    
    message.add_header('Content-Type', 'text/html')
    email_server.sendmail(message['From'], [message['To']], message.as_string().encode('utf-8'))
    print('E-mail enviado com sucesso!')

def send_email():
    try:
        email_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        email_server.starttls()

        email_server.login(SENDER, PASS_APP)
        
        create_email(email_server)
        
        email_server.quit()
    except Exception as e:
        print('Erro ao enviar o email:\n')
        print(e)