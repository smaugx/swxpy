#!/usr/bin/env python
# -*- coding:utf8 -*-
import os
import json
import time
import copy
from wxpy import *
import random

onemsg = {
    "date":"",
    "msg":""
    }

storemsg = {
    "林夕水共":[
      ]
    }

history = './log/history.msg'


def flash_historymsg():
  global history,storemsg
  fout = open(history,'a',encoding='utf-8')
  for k,v in storemsg.items():
    if len(v) > 2:
      d = {}
      d[k] = v
      jstr = json.dumps(d,ensure_ascii=False)
      jstr += '\n'
      fout.write(jstr)
      storemsg[k]=v[-1:]

def OnlyForSmaug(msg):
  welcome = 'Hey Bro, There you are!\n Looking for some help? try to give me some instructions!'
  menu = 'help: 帮助菜单\n mon(monitor): 获取监控系统日志\n flash: 写历史消息到历史消息文件'
  support = '支持的类型:文本,图片,视频,位置,分享'
  single = copy.deepcopy(onemsg)
  res_to_uplevel  = {"type":"","res":""}
  timestamp = time.time()
  date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(timestamp))
  single['date'] = date

  if not storemsg['林夕水共']:
    #最初的第一次
    single['msg'] = 'user_login'
    res_to_uplevel['type'] = 'Text'
    res_to_uplevel['res'] = welcome + '\n' + menu
  elif storemsg['林夕水共']:
    lastmsg = storemsg['林夕水共'][-1]['date']
    lastmsg = time.mktime(time.strptime(lastmsg,'%Y-%m-%d %H:%M:%S'))
    #超过10分钟则发出重新发送欢迎消息
    if int(timestamp) - int(lastmsg) > 10 * 60:
      single['msg'] = 'user_relogin'
      res_to_uplevel['type'] = 'Text'
      res_to_uplevel['res'] = welcome + '\n' + menu
    elif msg.type == 'Text':
      rtext = msg.text
      single['msg']= rtext
      if rtext == 'help':
        res_to_uplevel['type'] = 'Text'
        res_to_uplevel['res'] = menu
      elif rtext == 'mon' or rtext == 'monitor':
        res_to_uplevel['type'] = 'Text'
        cmd = 'sh ./cronlog.sh'
        os.popen(cmd)
        res_to_uplevel['res'] = '' 
      elif rtext == 'flash':
        flash_historymsg()
        res_to_uplevel['type'] = 'Text'
        res_to_uplevel['res'] = 'Flash success'
      else:
        #使用图灵接口智能聊天
        res_to_uplevel['type'] = 'tuling'
    elif msg.type == 'Map':
      rlocation = msg.location
      single['msg'] = rlocation
      res_to_uplevel['type'] = 'Text'
      res_to_uplevel['res'] = 'location is %s' % rlocation
    elif msg.type == 'Picture' or msg.type == 'Video':
      filename = msg.file_name
      path = './log/%s' % msg.sender.remark_name
      filename = os.path.join(path,filename)
      msg.get_file(filename)
      single['msg'] = msg.type
      res_to_uplevel['type'] = 'Text'
      res_to_uplevel['res'] = 'Download success'
    elif msg.type =='Sharing':
      single['msg'] = msg.url
      res_to_uplevel['type'] = 'Text'
      res_to_uplevel['res'] = 'http://rebootcat.com'
    else:
      #给出帮助菜单
      single['msg'] = msg.type
      res_to_uplevel['type'] = 'Text'
      res_to_uplevel['res'] = '不支持的类型!\n%s \n %s' % ( support,menu)


  if single.get('msg'):
    storemsg['林夕水共'].append(single)
  print(storemsg)
  return  res_to_uplevel


def OnlyForMissYang(msg):
  welcome = 'Hey Miss Yang, There you are!\n Looking for some help? try to give me some instructions!'
  menu = 'help: 帮助菜单,白痴的你需要记住这个命令,嘿嘿\n secret: 告诉你一些你不知道的事\n'
  support = '支持的类型:文本,图片,视频,位置,分享'
  single = copy.deepcopy(onemsg)
  res_to_uplevel  = {"type":"","res":""}
  timestamp = time.time()
  date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(timestamp))
  single['date'] = date
  username = msg.sender.remark_name
  username = 'Yang'
  if not storemsg.get(username):
    #最初的第一次
    storemsg[username] = []
    single['msg'] = 'Miss_Yang_login'
    res_to_uplevel['type'] = 'Text'
    res_to_uplevel['res'] = welcome + '\n' + menu
  elif storemsg[username]:
    lastmsg = storemsg[username][-1]['date']
    lastmsg = time.mktime(time.strptime(lastmsg,'%Y-%m-%d %H:%M:%S'))
    #超过10分钟则发出重新发送欢迎消息
    if int(timestamp) - int(lastmsg) > 10 * 60:
      single['msg'] = 'Miss_Yang_relogin'
      res_to_uplevel['type'] = 'Text'
      res_to_uplevel['res'] = welcome + '\n' + menu
    elif msg.type == 'Text':
      rtext = msg.text
      single['msg']= rtext
      if rtext == 'help':
        res_to_uplevel['type'] = 'Text'
        res_to_uplevel['res'] = menu
      elif rtext == 'secret':
        res_to_uplevel['type'] = 'Text'
        res_to_uplevel['res'] = random.choice(['我的芝麻信用分772啦，哈哈哈','你叫我哥哥我心都会融化/小羞涩','我今晚不过来了','我肚子好饿现在'])
      else:
        #使用图灵接口智能聊天
        res_to_uplevel['type'] = 'tuling'
    elif msg.type == 'Map':
      rlocation = msg.location
      single['msg'] = rlocation
      res_to_uplevel['type'] = 'Text'
      res_to_uplevel['res'] = 'location is %s' % rlocation
    elif msg.type == 'Picture' or msg.type == 'Video':
      filename = msg.file_name
      path = './log/%s' % username 
      filename = os.path.join(path,filename)
      msg.get_file(filename)
      single['msg'] = msg.type
      res_to_uplevel['type'] = 'Text'
      res_to_uplevel['res'] = 'Download success'
    elif msg.type =='Sharing':
      single['msg'] = msg.url
      res_to_uplevel['type'] = 'Text'
      res_to_uplevel['res'] = "have a look about your handsome boyfriend's website: http://rebootcat.com"
    else:
      #给出帮助菜单
      single['msg'] = msg.type
      res_to_uplevel['type'] = 'Text'
      res_to_uplevel['res'] = '不支持的类型!\n%s \n %s' % ( support,menu)


  if single.get('msg'):
    storemsg[username].append(single)
  print(storemsg)
  return  res_to_uplevel



