from urllib.request import urlopen
import re
page = urllib.request.urlopen("https://www.bloomberg.com/").read()
re.findall("Bitcoin",page)
page.find("Bitcoin")
