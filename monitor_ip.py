# -*- coding: utf-8 -*-
import re
import requests
import logging
from lxml import etree
from monitor_out_ip.mail import SendEmail


def jiankong():
    url = 'http://ip.cn/'
    header = {
        "Host": "ip.cn",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        # "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    res = requests.get(url).text
    print(res)
    # con = etree.HTML(res)
    # out_ip = str(con.xpath('//div[@id="result"]//p[1]/code/text()')[0])
    out_ip = re.search(r'Your IP</span>: (.*?)</span>', res).group(1)
    print(out_ip)
    if out_ip != '36.110.118.7':
        send_mail()

    else:
        pass


def send_mail():
    sendMail = SendEmail('1017253325@qq.com', 'gdnymtfmcmikbbdg', '1017253325@qq.com', ['1017253325@qq.com'], '程序提醒邮件',
                         '南京服务器出口出现变化, 及时更新...')  # 不要有测试之类的字眼
    sendMail.Send()
    logging.info("邮件发送成功...")


if __name__ == '__main__':
    jiankong()
    # send_mail()

# import smtplib
# from email.header import Header
# from email.mime.text import MIMEText
# server = smtplib.SMTP('smtp.163.com', 25)
# server.login('betbetter@163.com', 'lima2018')
# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# msg['From'] = 'betbetter@163.com <betbetter@163.com>'
# msg['Subject'] = Header('this is the company secret', 'utf8').encode()
# msg['To'] = '1017253325@qq.com'
# server.sendmail('betbetter@163.com', ['1017253325@qq.com'], msg.as_string())