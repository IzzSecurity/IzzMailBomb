import smtplib
import platform
import getpass
import sys
import datetime
import os
import time

class bcolors:
	GREEN = "\033[92m"


os.system("clear")
os.system("figlet IzzSpammer")

print 
print
print
print

time.sleep(5)

print( bcolors.GREEN + """
       #########################################################
       #						       #
       #   [+] Author    : IzzFsociety     		       #
       #                                                       #
       #   [+] Github    : github.com/izzzfsociety             #
       #                                                       #
       #   [+] Instagram : https://instagram/izzfsociety       #
       #						       #
       #########################################################
    							     """

print
print
print
print
print
smtp   = raw_input("Enter Your Mail Server : ")
print
if smtp == 'Gmail':
		server = smtplib.SMTP('smtp.gmail.com',587)
		server.starttls()

		time.sleep(3)                

                email     = raw_input("Enter Your Email : ")
                print
	        print
		password  = getpass.getpass("Enter your Password:")
		print
		print
		if not  email  and not password:
				print ("You must Login to your Gmail")
		else:
				server.login(email,password)
				

				print ("Successfully Signed in")
				print 
				print
				print
			        send = raw_input("Please Enter Your Victim Email : ")
				print
				print
				print
				print("Type Berapa Banyak Nak Spam")
				print
				print
				print
				thread= int(raw_input("Count : "))
				print
				print
				print
				msg = raw_input("Enter Your Message : ")
				
				

				for count in range(int(thread)):
					server.sendmail(email,send,msg)
					print (count,"Mesej Berjaya Dihantar! : ")



				server.quit()

else:
		print("You Must Choose 'Gmail' ")	
