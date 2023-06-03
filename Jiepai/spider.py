from urllib.parse import urlencode
from requests.exceptions import RequestException
import requests


def get_page_index(offset,keyword):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': 3
    }
    url = 'https://so.toutiao.com/search?'+urlencode(data)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引页出错')
        return None

def main():
    html= get_page_index(0,'街拍')
    print(html)


if __name__ == '__main__':
    main()
