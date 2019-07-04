#!/usr/bin/env python3
# coding: utf-8

__all__ = ['send_mail']

import os

from smtplib import SMTP
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.multipart import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.encoders import encode_base64
from mimetypes import guess_type


def create_attachment(file):
    # MIME类型
    type, encoding = guess_type(file)
    if type is None or encoding is not None:
        type = 'application/octet-stream'
    maintype, subtype = type.split('/', 1)
    attachment = MIMEBase(maintype, subtype)
    with open(file, 'rb') as f:
        attachment.set_payload(f.read())
    # 把附件编码
    encode_base64(attachment)
    basename = os.path.basename(file)
    # 修改邮件头
    attachment.add_header('Content-Disposition',
                          'attachment', filename=basename)
    return attachment


def create_message(from_addr, to_addrs, subject, text, attachments=[]):
    # 创建一个带附件的实例
    message = MIMEMultipart()
    # 发件人
    message['From'] = from_addr
    # 收件人
    message['To'] = ','.join(to_addrs)
    # 主题
    message['Subject'] = Header(subject, 'utf-8')
    # 正文
    message.attach(MIMEText(text, 'plain', 'utf-8'))
    # 附件
    for file_name in attachments:
        message.attach(create_attachment(file_name))
    return message


def send_mail(smtp_host, smtp_port, over_ssl, user, password, from_addr, to_addrs, subject, text, attachments=[]):
    # 连接SMTP服务器
    if over_ssl:
        smtp = SMTP_SSL(smtp_host, smtp_port)
    else:
        smtp = SMTP(smtp_host, smtp_port)
    # 登录
    if user:
        smtp.login(user, password)
    # 创建message
    message = create_message(from_addr, to_addrs, subject, text, attachments)
    # 发送
    smtp.sendmail(from_addr, to_addrs, message.as_string())
    # 关闭
    smtp.close()
