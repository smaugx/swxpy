#!/usr/bin/env python
#-*- coding:utf8 -*-

import sys
from wxpy import *
from wechat_sender import listen
import response


CachePath = './.wxpy/swxpy.pkl'
PuidPath = './.wxpy/wxpy_puid.pkl'
mybot = None
smaug = None   #代表我自己(main  wechat)
tuling = Tuling(api_key='21f2717e82a646e3bebc6a9f4e4a1710')

def login(Cachepath,Puidpath,Qr_path=None):
  bot = Bot(cache_path=Cachepath, console_qr = 2,qr_path=Qr_path)
  bot.enable_puid(Puidpath)
  return bot


def search_friend(bot,name):
  #friend = ensure_one(bot.friends().search(name)[0])
  friend = ensure_one(bot.friends(True).search(name))
  print(friend.puid)
  return friend


mybot = login(CachePath,PuidPath)
smaug = ensure_one(mybot.friends(True).search('林夕水共'))
MissYang = ensure_one(mybot.friends(True).search('子不语'))

@mybot.register(smaug)
def onlyforsmaug(msg):
  #print(msg.text)
  #msg.reply('you are so handsome!')
  res = response.OnlyForSmaug(msg)   #dict
  if res['type']  == 'Text':
    msg.reply_msg(res['res'])
  elif res['type'] == 'tuling':
    tuling.do_reply(msg)


@mybot.register(MissYang)
def onlyformissyang(msg):
  #print(msg.text)
  #msg.reply('you are so handsome!')
  res = response.OnlyForMissYang(msg)   #dict
  if res['type']  == 'Text':
    msg.reply_msg(res['res'])
  elif res['type'] == 'tuling':
    tuling.do_reply(msg)

if __name__ == '__main__':
  recvers = []
  friend = search_friend(mybot,'林夕水共')
  recvers.append(friend)
  listen(mybot,receivers = recvers,token='daqiaoweijiu',port=6969,status_report=True,status_interval=30 * 60 * 1000)

