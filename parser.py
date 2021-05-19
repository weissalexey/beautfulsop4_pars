#pip install BeautifulSoup4 lxml

from bs4 import BeautifulSoup

with open("works/index.html") as file:
    src=file.read()

#print (src)
soup = BeautifulSoup(src, "lxml")

#title = soup.title
#print(title.tetx)

find_all_spans_in_user_info = soup.find(class= "user_info").find_all("span")
print (find_all_spans_in_user_info)

for item in find_all_spans_in_user_info:
    print(item.text)
    
