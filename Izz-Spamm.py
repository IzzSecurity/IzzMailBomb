# -*- coding: utf-8 -*-
#!/usr/bin/python3

import smtplib
import time
import os
import getpass
import sys


class bcolors:
	GREEN = "\033[92m"
	WARNING = "\033[93m"
	FAIL = "\033[91m"
	ENDC = "\033[0m"




def spam():
	os.system("clear")
	print( bcolors.GREEN + """
       
       


 __     ______     ______     ______     ______   ______     __    __    
/\ \   /\___  \   /\___  \   /\  ___\   /\  == \ /\  __ \   /\ "-./  \   
\ \ \  \/_/  /__  \/_/  /__  \ \___  \  \ \  _-/ \ \  __ \  \ \ \-./\ \  
 \ \_\   /\_____\   /\_____\  \/\_____\  \ \_\    \ \_\ \_\  \ \_\ \ \_\ 
  \/_/   \/_____/   \/_____/   \/_____/   \/_/     \/_/\/_/   \/_/  \/_/ """ + bcolors.ENDC)
                                                                         

os.system("clear")
try:
	file1 = open("python.txt", "r")
	print(" ")
	print(bcolors.GREEN + file1.read() + bcolors.ENDC)
	file1.close()
except IOError:
	print("Banner File not found")

#Input
print(bcolors.WARNING + """

Pilih Nak Guna Mana Satu :

1) Gmail

2) Yahoo

3) Hotmail / Outlook
""" + bcolors.ENDC + "")
try:
	server = input(bcolors.GREEN + "Mail Server: " + bcolors.ENDC)
	user = input(bcolors.GREEN + "Email Anda: " + bcolors.ENDC)
	pwd = getpass.getpass(bcolors.GREEN + "Password Anda: " + bcolors.ENDC)
	to = input(bcolors.GREEN + "Kepada: " + bcolors.ENDC)
	subject = input(bcolors.GREEN + "Tajuk (Optional): " + bcolors.ENDC)
	body = input(bcolors.GREEN + "Message Untuk Dihantar: " + bcolors.ENDC)
	nomes = input(bcolors.GREEN + "Berapa Banyak nak Hantar: " + bcolors.ENDC)
	no = 0
	message = "From: " + user + "\nSubject: " + subject + "\n" + body
except KeyboardInterrupt:
	print(bcolors.FAIL + "\nCanceled" + bcolors.ENDC)
	sys.exit()

#Gmail

if server == "1" or server == "gmail" or server == "Gmail":
	spam()
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print(bcolors.FAIL + """Your Username or Password is incorrect, please try again using the correct credentials
		Or you need to enable less secure apps
		On Gmail: https://myaccount.google.com/lesssecureapps """ + bcolors.ENDC)
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print(bcolors.WARNING + "Berjaya Hantar Ke Target :) " + str(no+1) + " Emails" + bcolors.ENDC)
			no += 1
			time.sleep(.3)
		except KeyboardInterrupt:
			print(bcolors.FAIL + "\nCanceled" + bcolors.ENDC)
			sys.exit()
		except:
			print("Failed to Send Cuba Try Lagi Sekali :( ")
	server.close()
	
#Yahoo
elif server == "2" or server == "Yahoo" or server == "yahoo":
	server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
	spam()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print(bcolors.FAIL + """Your Username or Password is incorrect, please try again using the correct credentials
		Or you need to enable less secure apps
		On Yahoo: https://login.yahoo.com/account/security?.scrumb=Tiby8TXUvJt#less-secure-apps
		""" + bcolors.ENDC)
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print(bcolors.WARNING + "Berjaya Hantar Ke Target :) " + str(no + 1) + " Emails" + bcolors.ENDC)
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print(bcolors.FAIL + "\nCanceled" + bcolors.ENDC)
			sys.exit()
		except:
			print("Failed to Send Cuba Try Lagi Sekali :(")
	server.close()
	
#Hotmail/Outlook
elif server == "3" or server == "outlook" or server == "Outlook" or server == "Hotmail" or server == "hotmail":
	server = smtplib.SMTP("smtp-mail.outlook.com", 587)
	spam()
	server.ehlo()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print(bcolors.FAIL + "Your Username or Password is incorrect, please try again using the correct credentials" + bcolors.ENDC)
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print(bcolors.WARNING + "Berjaya Hantar Ke Target :) " + str(no + 1) + " Emails" + bcolors.ENDC)
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print(bcolors.FAIL + "\nCanceled" + bcolors.ENDC)
			sys.exit()
		except smtplib.SMTPAuthenticationError:
			print("\nThe username or password you entered is incorrect.")
			sys.exit()
		except:
			print("Failed to Send Cuba Try Lagi Sekali :( ")
	server.close()
	
else:
	print("Works only with Gmail, Yahoo, Outlook and Hotmail.")
	sys.exit()
