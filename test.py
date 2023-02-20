from bs4 import BeautifulSoup

html = """<html><head><title>test site</title></head> <body><p><span>test</span><span>test1</span><span>test2</span></p><p>test2</p><p>test3</p></body></html>"""

soup = BeautifulSoup(html,'lxml')

# tag_p = soup.p
tag_p = soup.p.span.string

print(tag_p)
print(type(soup), ',',type(tag_p))

print(tag_p.text)
print(type(tag_p.text))
print(tag_p.string)
print(type(tag_p.string))
# 결과값은 같지만 다르다.
