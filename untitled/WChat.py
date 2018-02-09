import itchat
from echarts import Echart,Legend,Pie

itchat.auto_login(hotReload=True)
itchat.dump_login_status()

# itchat.send(u'hello 侯志峰', 'filehelper')
friends = itchat.get_friends(update=True)[0:]
# print(friends)
male = female = other = 0
for i in friends[1:]:
    sex = i['Sex']
    if sex == 1:
        male+=1
    elif sex == 2:
        female+=1
    else:
        other +=1

total = len(friends[1:])

# print (u"男性好友：%.2f%%" % (float(male) / total * 100))
# print (u"女性好友：%.2f%%" % (float(female) / total * 100))
# print (u"其他：%.2f%%" % (float(other) / total * 100))

chart = Echart(u'%s的微信好有性别比例' %(friends[0]['NickName']), 'from WeChat')
chart.use(Pie('WeChatt',
              [{'value': male, 'name': u'男性 %.2f%%' % (float(male) / total * 100)},
               {'value': female, 'name': u'女性 %.2f%%' % (float(female) / total * 100)},
               {'value': other, 'name': u'其他 %.2f%%' % (float(other) / total * 100)}],
              radius=["50%", "70%"]))

chart.use(Legend(["male", "female", "other"]))
del chart.json["xAxis"]
del chart.json["yAxis"]
chart.plot()