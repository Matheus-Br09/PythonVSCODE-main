import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen("https://www.pudim.com.br")
except urllib.error.URLError:
    print("\033[31mSite está indisponível no momento\033[m")
else:
    print("\033[36mSite disponível!!\033[m")