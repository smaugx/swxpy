#!/usr/bin/env python
# -*- coding:utf8 -*-

import os
from wechat_sender import Sender

mysender = None
SHOME = os.environ.get('SHOME')


def login(token,port):
  sender = Sender(token=token,port= port)
  return sender


def get_log(lines = 10):
  reallog = ""
  logpath = os.path.join(SHOME,'send.data')
  for l in open(logpath,'r').readlines():
    reallog = "{0}{1}".format(reallog,l)

  return reallog


if __name__ == '__main__':
  mysender = login('daqiaoweijiu',6969)
  log = get_log()
  mysender.send(log)
  #print(log)
