# structure of classes


from bs4 import BeautifulSoup, PageElement
import re

html = ""
with open("raw/simple_dataset.html", "rb") as raw_dataset:
    html = raw_dataset.read()

soupified = BeautifulSoup(html, "html.parser")
class_rows_table_id = "ACE_$ICField$4$$0"
class_rows_table = soupified.find(id = class_rows_table_id)
rows = class_rows_table.find_all("tr")[1:]#min(10, len(class_rows_table)-1)]

row: PageElement
for row in rows:
    holder = row.find("tr")
    course_info = holder
    if course_info:
        print(re.sub(r'\s+', ' ', course_info.get_text()))

# row = rows[0]
# info = row.find("tr")
# # print(re.sub(r'\s+', ' ', info.get_text()))
# print(info.get_text())