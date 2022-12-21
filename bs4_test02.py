

import re
from bs4 import BeautifulSoup

myencoding = 'utf-8'
myparser = 'html.parser'
filename = 'cartoon.html'

html = open(filename, encoding=myencoding)
soup = BeautifulSoup(html, myparser)

#string 속성 : 해당 요소의 글자 부분을 추출함
# > : 현재 대상의 바로 하위 child를 찾음, 여러번 중첩하여 사용 가능함.
h1 = soup.select_one("div#cartoon > h1").string
print("h1 = ", h1)
print("h1 type = ",type(h1))
# 객체.select(<선택자>) : css 선택자로 여러 요소를 리스트로 추출함.
li_list = soup.select("div#cartoon > ul.elements > li")

for li in li_list:
    print("li = ", li.string)

print()

for a in li_list:
    print(a.string)


print('-' * 30)
chioce = lambda  x : print(soup.select_one(x).string)

print('\nchioce("#item5") : ', end='')
chioce("#item5")

print('\nchioce("li#item4") : ', end='')
chioce("li#item4")

print('\nchioce("ul#itemlist > li#item3") : ', end='')
chioce("ul#itemlist > li#item3")

print('\nchioce("#itemlist #item2") : ', end='')
chioce("#itemlist #item2")

print('\nchioce("ul#itemlist > li#item2") : ', end='')
chioce("ul#itemlist > li#item2")

print()
print('\nsoup.select("li")[1].string : ', end='')
print(soup.select("li")[1].string)

# find_all(tag, attributes, limit=숫자) : 조건에 맞는 HTML 태그를 전부 찾아준다.
print('\nsoup.find_all("li")[3].string : ', end='')
print(soup.find_all("li")[3].string)

print('-' * 30)

# class 속성 us인 1번째 요소
print(soup.select("#vegetables > li[class='us']")[0].string)
print(soup.select("#vegetables > li.us")[1].string)

print()

# ^= : ~으로 시작하는, $= : ~으로 끝나는
result = soup.select('a[href$=".com"]')
for item in result:
    print(item['href'])

print()
# *= : ~을 포함하고 있는
result = soup.select('a[href*="daum"]')
for item in result:
    print(item['href'])