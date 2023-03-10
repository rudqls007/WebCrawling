


from bs4 import BeautifulSoup

# Beautiful Soup 라이브러리를 이용한 태그 속성을 다루고 있다.
html = open("fruits.html", "r", encoding="utf-8")
soup = BeautifulSoup(html, "html.parser")

# 태그 셀렉트
body = soup.select_one("body")                 # 객체.select_one(<선택자>) : CSS 선택자로 요소 하나를 추출함
ptag = body.find('p')                                 # 객체.find(tag, [attributes]) : tag라는 태그 중 조건에 맞는 1번째 태그를 찾아줌

print('1번째 p 태그 : ', ptag)
print('1번째 p 태그 : ', ptag['class'])

ptag['class'][1] = 'white'

print('1번째 white로 바뀐 p 태그 : ', ptag['class'])

ptag['id'] = 'apple'

print('1번째 p 태그의 id 속성 : ', ptag['id'])

print()
# <body> 태그 내의 모든 요소의 목록이 출력된다.
bodytag = soup.find('body')
print(bodytag)

print()

idx = 0
# 객체.children : 해당 태그의 하위 태그들을 리스트 목록으로 반환한다.
print('childrean 속성으로 하위 항목 보기')
for child in bodytag.children:
    idx += 1
    print(str(idx) + ' 번째 요소 ', child)

print()
mydiv = soup.find('div')
print(mydiv)

print()
# 객체.parent : 해당 객체의 부묘 요소를 찾아 준다.

print('div 태그의 부모 태그는 ?')
print(mydiv.parent)

print()
# 객체.find_parents() : 현재 태그의 상위에 있는 모든 태그를 찾아준다.
print('mydiv 태그의 모든 상위 부모 태그들의 이름 : ')
parents = mydiv.find_parents()
for p in parents:
    print(p.name)

