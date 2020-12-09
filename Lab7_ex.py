import requests
import re

r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
data = r.text
data = re.sub(r'<.*?>', '', data)  # remove <string> in string data
text = data.split('\n')
while "" in text:
    text.remove("")
print(text)
