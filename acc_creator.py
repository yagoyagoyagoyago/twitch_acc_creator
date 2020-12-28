import requests
import random
import string
import time
import threading
from sys import argv
from termcolor import colored
import os
proxies = open(argv[1]).read().splitlines()
captcha = argv[2]
start = float(requests.get("https://2captcha.com/res.php?key="+captcha+"&action=getbalance").text)
contas = []
def nickname():
    carafodase = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(12))
    emergencia = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(25))
    f = "yyy_{}".format(carafodase)
    data = '[{"operationName":"UsernameValidator_User","variables":{"username":"hahahahahah7835y9578936536789359678"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"fd1085cf8350e309b725cf8ca91cd90cac03909a3edeeedbd0872ac912f3d660"}}}]'.replace("hahahahahah7835y9578936536789359678", f)
    h = {"Client-Id": "kimne78kx3ncx6brgo4mv6wki5h1ko",
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"}
    url = "https://gql.twitch.tv/gql"
    rsp = requests.post(url, data=data, headers=h).json()[0]["data"]["isUsernameAvailable"]
    if rsp == True:
        return f
    else:
        return emergencia
def password():
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(70))
def email():
    return requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1").json()[0]
def date():
    return "{}/{}/{}".format(random.randint(1, 29), random.randint(1, 13), random.randint(1970, 2003))
def arkose_token(proxy):
    try:
        y = requests.get("https://2captcha.com/in.php?key="+captcha+"&method=funcaptcha&publickey=E5554D43-23CC-1982-971D-6A2262A2CA24&surl=https://client-api.arkoselabs.com&pageurl=https://twitch.tv/signup&nojs=1").text.split("|")[1]
        yyy = requests.get("http://2captcha.com/res.php?key="+captcha+"&action=get&id="+y).text
        c = 0
        while "CAPCHA_NOT_READY" in yyy:
            c += 1
            yyy = requests.get("http://2captcha.com/res.php?key="+captcha+"&action=get&id="+y).text
            print("(id|{}) {} tentativa nº {} | resposta: {}".format(proxy, colored("primeira", "blue"), c, colored(yyy, "blue")))
            time.sleep(5)
            if c == 24:
                print("acabaram-se as " + colored("primeiras tentativas ", "blue") + "do id: " + proxy)
                break
        if yyy == "ERROR_CAPTCHA_UNSOLVABLE":
            egg = requests.get("https://2captcha.com/in.php?key="+captcha+"&method=funcaptcha&publickey=E5554D43-23CC-1982-971D-6A2262A2CA24&surl=https://client-api.arkoselabs.com&pageurl=https://twitch.tv/signup&nojs=1").text.split("|")[1]
            eggs = requests.get("http://2captcha.com/res.php?key="+captcha+"&action=get&id=" + egg).text
            cu = 0
            while "CAPCHA_NOT_READY" in eggs:
                cu += 1
                eggs = requests.get("http://2captcha.com/res.php?key=b56c36c5acd7119194a8866172b7c884&action=get&id=" + egg).text
                print("(id|{}) {} tentativa nº {} | resposta: {}".format(proxy, colored("segunda", "magenta"), cu, colored(eggs, "magenta")))
                time.sleep(5)
                if cu == 24:
                    print("acabaram-se as " + colored("segundas tentativas ", "magenta") + "do id: " + proxy)
                    break
            return eggs.split("|", 1)[1]
        else:
            return yyy.split("|",1)[1]
    except Exception as e:
        print("(id|{}) {} | {}".format(proxy, colored("erro na resolução dos captchas.", "yellow"), colored(e, "yellow")))
        return "erro"
def criador(proxy):
    proxiesx = {"https": "https://" + proxy}
    try:
        print(colored("testando proxy: ", "magenta") + colored(proxy, "yellow") + " vai demorar no maximo 1 minuto...")
        for c in range(1, 13):
            requests.post("https://passport.twitch.tv/register", proxies=proxiesx, timeout=30)
            print(colored("{} passou na tentativa {} faltam {} | segundos que se passaram {}".format(proxy,c, 24-c, c*5), "green"))
            time.sleep(5)
        print("proxy {} acabou de ser testada.".format(colored(proxy, "magenta")))
    except requests.exceptions.ProxyError as e:
        print('antes mesmo de tudo acontecer, eu yago, detectei que essa proxy "{}" é um {}! [conta não foi criada] | {}'.format(colored(proxy, "yellow"), colored("LIXO", "red"), colored(e, "yellow")))
        return ""
    except Exception as e:
        print('antes mesmo de tudo acontecer, eu yago, detectei que essa proxy "{}" é um {}! [conta não foi criada] | {}'.format(colored(proxy, "yellow"), colored("LIXO", "red"), colored(e, "yellow")))
        return ""
    try:
        print(colored("caralho, essa proxy aqui é boa o suficiente: ", "cyan") + proxy)
        _1 = nickname()
        _2 = password()
        _3 = email()
        _4 = date()
        domain = _3.split("@")[1]
        login = _3.split("@")[0]
        dia = int(_4.split("/")[0])
        mes = int(_4.split("/")[1])
        ano = int(_4.split("/")[2])
        _5 = "kimne78kx3ncx6brgo4mv6wki5h1ko"
        _6 = arkose_token(proxy)
        if _6 == "erro":
            pass
        else:
            h = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"}
            data = {"username":_1,"password":_2,"email":_3,"birthday":{"day":dia,"month":mes,"year":ano},"client_id":_5,"include_verification_code":True,"arkose":{"token":_6}}
            url = "https://passport.twitch.tv/register"
            rsp = requests.post(url, json=data, headers=h, proxies=proxiesx, timeout=30)
            print("(id|{}) ".format(proxy) + colored(rsp.text, "cyan"))
            hdrs = rsp.headers
            oauth = rsp.json()["access_token"]
            usr_id = hdrs["Set-Cookie"].split("=")[7].split("%")[0]
            time.sleep(2)
            rip = requests.get("https://www.1secmail.com/api/v1/?action=getMessages&login={}&domain={}".format(login, domain)).json()
            code = rip[0]["subject"].split(" ")[0]
            hnew = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0p","Client-Id": "kimne78kx3ncx6brgo4mv6wki5h1ko", "Authorization": "OAuth " + oauth}
            payload = '[{"operationName":"ValidateVerificationCode","variables":{"input":{"code":"xdxdxdxdxd","key":"kkkkkkkkkkkkk","address":"aaaporraaaaa"}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"05eba55c37ee4eff4dae260850dd6703d99cfde8b8ec99bc97a67e584ae9ec31"}}}]'.replace(
                "xdxdxdxdxd", code).replace("kkkkkkkkkkkkk", usr_id).replace("aaaporraaaaa", _3)
            foi = requests.post("https://gql.twitch.tv/gql", data=payload, headers=hnew)
            if foi.status_code == 200:
                print(colored("a verificação do email deu certo!", "green"))
            else:
                print(colored("a verificação do email não deu certo! :(", "red"))
            pay = "oauth_token:{}:username:{}:user_id:{}:client_id:{}".format(oauth, _1, usr_id, _5)
            contas.append(pay)
            print("(id|{}) {} [{}]|".format(proxy, colored("conta criada com sucesso.", "green"), _1))
    except requests.exceptions.ProxyError as e:
        print("(id|{}) {} | {}".format(proxy, colored("algum erro na proxy ocorreu e a conta não foi criada.", "red"), colored(e, "yellow")))
    except Exception as e:
        print("(id|{}) {} | {}".format(proxy, colored("algum erro ocorreu e a conta não foi criada.", "red"), colored(e, "yellow")))
def main():
    print("resolvendo captcha, pode demorar até 2 minuto...")
    print("expectativa de contas que serão criadas: " + str(len(proxies)))
    threads = [threading.Thread(target=criador, args=(p,)) for p in proxies]
    for th in threads:
        th.daemon = True
        th.start()
    for th in threads:
        th.join()
main()
n = random.randint(1, 99999)
filen = "yyycontas{}.txt".format(str(n))
for conta in contas:
    with open(filen, "a+") as file:
        file.write("{}{}".format(conta, os.linesep))
final = float(requests.get("https://2captcha.com/res.php?key="+captcha+"&action=getbalance").text)
print("Contas criadas: {}\nTentativas: {}\nAs contas foram salvadas em: {}\nDinheiro gasto: {}\nSaldo atual: {}".format(len(contas), len(proxies), filen, start-final, final))