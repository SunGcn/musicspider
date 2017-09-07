import requests
from PIL import Image
from bs4 import BeautifulSoup

//
url1 = 'http://my.hlju.edu.cn/captchaGenerate.portal?'
url2 = 'http://my.hlju.edu.cn/userPasswordValidate.portal'
url3 = 'http://my.hlju.edu.cn/index.portal'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}
s = requests.session()
response = s.get(url1, headers=headers)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
with open('img\code.jpg', 'wb') as f:
    f.write(response.content)
img = Image.open('img\code.jpg')
img.show()
