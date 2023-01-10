import re
import urllib.request

data = str(urllib.request.urlopen("https://www.google.com/").read())
data = re.sub( r'<[^>]*>', ' ', data ).strip()
print(data)