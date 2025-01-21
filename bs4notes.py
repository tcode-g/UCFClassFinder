

html = """
<p>Head
    <p>Mid
        <p>Last</p>
    </p>
</p>

"""

from bs4 import BeautifulSoup as soup

s = soup(html, "html.parser")
for e in s("p"):
    print(e)
