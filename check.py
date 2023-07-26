import requests, time as t, sys, os, re, urllib.parse
from colorama import Fore, Back
from bs4 import BeautifulSoup

t.sleep(2)
os.system("clear")
t.sleep(1)
print(Fore.GREEN , "")

def typewriter(message):
    for char in message:
        print(char, end='', flush=True)
        t.sleep(0.01)
    print()

def banner():
	banner = '''
  _     _  ______             _______ _     _ _______ _______ _     _ _______  ______
  |     | |_____/ |           |       |_____| |______ |       |____/  |______ |_____/
  |_____| |    \_ |_____      |_____  |     | |______ |_____  |    \_ |______ |    \_
  <------------------------------------------>
  | GitHub : TnYtCoder                       |
  | Python Script To Check Website Existance |
  <------------------------------------------>


	'''
	typewriter(banner)
banner()

t.sleep(0.5)

def ques():
	ques = '''
  [1] Start
  [2] Exit
  [3] Help


	'''
	typewriter(ques)
ques()

opt = int(input('  Choose an option :  '))

if opt == 1:
	url = input("\n  Enter Url :  ")
	parsed_url = urllib.parse.urlparse(url)
	domain = parsed_url.hostname
	if "https" in url:
		protocol = "Secured"
	elif "http" in url:
		protocol = "Not Secured"
	else:
		protocol = "Undefined"
	try:
		resp = requests.get(url)
		if resp.status_code == 200:
			print(Fore.LIGHTBLUE_EX,"\n  [>] Website Status :  Exist")
			t.sleep(0.5)
			print("  [>] Protocol :  {}".format(protocol))
			t.sleep(0.5)
			print("  [>] Status Code :  ", resp.status_code)
			t.sleep(0.5)
			print("  [>] Domain :  {}".format(domain))
			t.sleep(1)
			thank = "\n  [~] Thank You For Using !!!"
			typewriter(Fore.GREEN + thank)
			def get_website_name(url):
				url = url.replace("https://", "").replace("http://", "")
				url = url.split("/")[0]
				parts = url.split(".")
				website_name = parts[0]
				return website_name
			webn = get_website_name(url)
			webt = webn + ".txt"
			# File Logs
			text = "Saved WebLogs !!! \n"+ "\nWebsite Status : Exist"+ "\nProtocol : "+ protocol + "\nStatus Code : "+ str(resp.status_code) + "\nDomain : "+ domain +"\n\nMade By TnYtCoder ; )"
			f = open(webt, "w")
			f.write(text)
			f.close
			os.system("mv {} logs/".format(webt))
		else:
			print("\n [>] Website Status :  Not Exist\n")
	except requests.exceptions.RequestException as e:
		print("\n [>] Website Status :  Not Exist\n")
elif opt == 2:
	t.sleep(1)
	thank = "\n \033[0;32;47m Thank You For Using !!!\033[0m 0;32;47m \n"
	typewriter(thank)
	t.sleep(0.5)
	sys.exit()
elif opt == 3:
	print("\n  Please Wait...")
	os.system("am start -a android.intent.action.VIEW -d https://github.com/TnYtCoder/ > /dev/null 2>&1")
	os.system("python3 check.py")
else:
	sys.exit("\n  Option Doesn't Exist")
