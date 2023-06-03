import urllib
from urllib import request

if __name__ == '__main__':
    url = "https://www.baidu.com"

    request = urllib.request.Request(url)
    # fp = request.urlopen("http://www.nuc.edu.cn")
    # print(requests.getcode())
    print("=====================================")
    # print(fp.read())
