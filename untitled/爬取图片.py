import urllib.request, socket, re, sys, os

targetpath = "E://03_dbimages"

def savefile(path):
    if not os.path.isdir(targetpath):
        os.mkdir(targetpath)
    pos = path.rindex('/')
    t = os.path.join(targetpath, path[pos+1:])
    return t

url = "http://www.douban.com/"

req = urllib.request.Request(url)
res = urllib.request.urlopen(req)
data = res.read()

# print(re.findall(r'(http:^img.*?(jpg|png|gif))', str(data)))

for link,t in set(re.findall(r'(https:[^s]*?(jpg|png|gif))', str(data))):
    print(link)
    try:
        urllib.request.urlretrieve(link, savefile(link))
    except:
        print("失败")
