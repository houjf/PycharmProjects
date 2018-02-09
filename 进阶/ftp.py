import ftplib, os

connect = ftplib.FTP('huangwq-pc1')
# connect.login()
# data = []
# connect.dir()

print(connect.getwelcome())
connect.login('gaea-gtj', '1qaz@WSX#')
list = connect.nlst()
# list.decode('utf-8')
# for x in list:
#     print(x.decode('utf-8'))
# print(list)
c = u'08ä»£ç\xa0\x81è¦\x86ç\x9b\x96ç\x8e\x87æ\x95°æ\x8d®'

print(c) #.encode('latin-1').decode('GBK')