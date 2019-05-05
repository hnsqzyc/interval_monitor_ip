from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from monitor_out_ip.monitor_ip import jiankong
import random
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp.log',
                    filemode='a')


def job():
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_info = [{"messageHead": {"version":"1.0","requestType":"01","UUID":"cff6105b-081b-466e-aee8-7aac06f9cfb5","sendTime": time},"request":{"name":"王瑞","cardType":"01","cardNumber":"65212219850914232"}},
                # {"messageHead": {"version":"1.0","requestType":"01","UUID":"cff6105b-081b-466e-aee8-7aac06f9cfb5","sendTime": time},"request":{"name":"邓伟","cardType":"01","cardNumber":"43282419790823077X"}},
                # {"messageHead": {"version": "1.0", "requestType": "01", "UUID": "cff6105b-081b-466e-aee8-7aac06f9cfb5","sendTime": time},"request": {"name": "王宁", "cardType": "01", "cardNumber": "14263519880723111X"}}
                ]
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    jiankong()

scheduler = BlockingScheduler()
scheduler.add_job(job, 'interval', minutes=1)
scheduler.start()