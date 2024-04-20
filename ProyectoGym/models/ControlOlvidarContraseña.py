from flask import redirect
from models.consultas import consultarCorreo
import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart # esto quiere decir que este correo va a estar compuesto de varias partes (html, imagenes, adjuntos etc)
from email.mime.text import MIMEText #como solo usaremos html importamos solo MIMEText 

def validarCorreo(email):
    existeCorreo = consultarCorreo(email)
    if existeCorreo:
        return True
    else:
        return False
    #return existeCorreo
def enviarCorreo(destinatario):
    try:
        load_dotenv() #carga las variables de entorno desde el archivo .env

        remitente = os.getenv('USER')
        destino = destinatario
        asunto = 'Actualice su contraseña en Fithub Innovations'

        msg = MIMEMultipart()
        msg['Subject'] = asunto
        msg['From'] = remitente
        msg['To'] = destino


        with open('Email.html', 'r') as archivo:
            html = archivo.read()
        
        #Adjuntar contenido html
        msg.attach(MIMEText(html, 'html')) #pasamos el contenido y el tipo del contenido

        #Representa una conexion con un servidor de correo saliente(smtp server)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        #conexion segura
        server.starttls()
        server.login(remitente, os.getenv('PASS'))

        #enviar correo electronico
        server.sendmail(remitente, destino, msg.as_string())
    except Exception as e:
        print("Error al enviar el correo: ", e)
    finally:
        if 'server' in locals():
            server.quit()

