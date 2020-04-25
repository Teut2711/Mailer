####  mailer imports ##

import os
import pandas as pd
import mimetypes
import pathlib
import sys
import smtplib
import codecs
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

from PyQt5.QtCore import QThread, pyqtSignal


def get_doc_text(word_file):
    ''' Read message html file'''
    with codecs.open(os.path.join(word_file), "r") as f:
        return f.read()


def get_dataframe(excel_path):

    try:
        df = pd.read_excel(excel_path, dtype=str, keep_default_na=False)
    except:
        df = pd.read_csv(excel_path, dtype=str, keep_default_na=False)
    return df


def get_mime(path):
    mime = mimetypes.guess_type(path)[0]
    if mime:
        return mime
    elif path.endswith(".rar"):
        return "application/x-rar-compressed"
    else:
        raise TypeError("Filetype not supported invalid")


def html_embedding(word_file_converted_text):
    return f'''<!DOCTYPE html>
    <html>
    <body>
    {word_file_converted_text}    
    </body>
    </html>'''


class sendMail(QThread):

    sent_to = pyqtSignal(str, int)            
        
    def __init__(self, settings, excel_file):
        super().__init__()
        self.settings = settings
        self.excel_file = excel_file

    def run(self):
        
        df = get_dataframe(self.excel_file)
        nrows = df.shape[0]

        for index, row in df.iterrows():
            to, file_path, subject, message_file, from_ = *[
                i.strip() for i in row.tolist()
            ], self.settings["mailfrom"]

            try:
                msg = self.prepMail(from_, to, file_path, subject,
                                    message_file)
            except ValueError:
                self.sent_to.emit(
                    "Subject is Absent.. Mail not sent  to {to}" , -1)
            except Exception as e:
                self.sent_to.emit(f"{getattr(e, 'message', repr(e))}\n{index} {to}", -1)
            else:
                try:
                    self.fireMail(msg)
                    
                except Exception as e:
                    self.sent_to.emit(getattr(e, 'message', repr(e)), -1)
                    
                else:    
                    self.sent_to.emit("Sent mail to :::  " + to,
                                      ((index + 1) * 100) // nrows)

    def prepMail(self, from_, to, file_path, subject, message_file):

        msg = EmailMessage()
        msg['From'] = from_

        if subject.strip():
            msg['Subject'] = subject
        else:
            raise ValueError("Invalid value..")
        if to:
            msg['To'] = ", ".join(to.split(","))

        if message_file:
            msg.add_alternative(html_embedding(get_doc_text(message_file)),
                                subtype='html')

        for fil in file_path.split(","):
            if os.path.exists(fil.strip()):
                with open(os.path.join(fil.strip()), "rb") as f:
                    file_data = f.read()
                    file_name = pathlib.Path(file_path).name
                maintype, subtype = get_mime(file_path).split("/")

                msg.add_attachment(file_data,
                                   maintype=maintype,
                                   subtype=subtype,
                                   filename=file_name)
        return msg

    def fireMail(self, msg):
            
            with smtplib.SMTP(self.settings['smtphost'],
                              self.settings['smtpport']) as smtp:
                smtp.starttls()
                smtp.login(user=self.settings['smtpuser'],
                           password=self.settings['smtppass'])
                smtp.send_message(msg)
            