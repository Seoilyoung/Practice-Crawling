from bs4 import BeautifulSoup

html = """<html><head><title>test site</title></head> <body><p><span>test</span><span>test1</span><span>test2</span></p><p>test2</p><p>test3</p></body></html>"""

soup = BeautifulSoup(html,'lxml')

# tag_p_children = soup.p.contents
# print(tag_p_children)

# tag_p_children2 = soup.p.children
# print(tag_p_children2)
# for child in tag_p_children2:
#     print(child)
# # list iterator object 형태로 가져오므로 보려면 반복문 사용.

# tag_span = soup.span
# tag_title = soup.title

# # span_parent = tag_span.parent
# # title_parent = tag_title.parent
# # print(tag_span)
# # print(span_parent)
# # print(tag_title)
# # print(title_parent)

# span_parents = tag_span.parents
# title_parents = tag_title.parents
# print(tag_span)
# print(span_parents)
# print(tag_title)
# print(title_parents)
# # children 과 비슷하지만 generator object로 가져온다. 반복문 사용. 최상위 태그까지 단계별로 모두 출력.

# tag_span = soup.span

# a = tag_span.next_sibling
# b = a.previous_sibling

# print(a)
# print(b)
# # sibling next, previous로 형제 태그 접근 가능. siblings쓰면 generator objects로 쭉 가져옴. 
# # element를 사용하면 태그가 아니라 요소로 접근 가능.(요소 : 태그,자식태그,문자) elements도 사용 가능. 탐색 방식은 dfs

