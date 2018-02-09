import urllib.request

def savefile(data):
    path = "C://01_douban.out"
    f = open(path, 'wb')
    f.write(data)
    f.close()

url = "http://www.douban.com/"
# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)' 'Chrome/55.0.2883.87 Safari/537.36'}
heade = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)' 'Chrome/63.0.3239.132 Safari/537.36'}
req = urllib.request.Request(url)
res = urllib.request.urlopen(req)
data = res.read()

savefile(data)

data = data.decode('utf-8')

print(data)
print(type(res))
print(res.geturl())
print(res.info())
print(res.getcode())
