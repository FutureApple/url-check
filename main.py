import requests
import os

urlin = open("url-in.txt")
urlin = str(urlin.read())
urllist = urlin.split()
outurl = []
times = 0
num = len(urllist) -1

def check(url):
    try:
        request = requests.get(url)
        status = request.status_code
    except:
        print('error')
        status=114514
    if status != 200:
        return url
    else:
        return 200

for url in urllist:
    i = check(url)
    if i == 200:
        outurl.append(url)

try:
    os.remove("url-out.txt")
    outfile = open("url-out.txt",mode="w")
except:
    outfile = open("url-out.txt",mode="w")

for i in outurl:
    outfile.write(str(i)+"\n")
outfile.close()
print('ok')