import requests
import itchat  # 这是一个用于微信回复的库

KEY = '36a95e022d994128a20620bc245accb2'  # 这个key可以直接拿来用


# 向api发送请求
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'Monkey',
    }
    while True:
        try:
            r = requests.post(apiUrl, data=data).json()
            return r.get('text')
        except:
            return


# 注册方法
itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    # 为了保证在图灵K出现问题的时候仍旧可以回复，这里设置一个默认回复
    defaultReply = 'I received: ' + msg['Text']
    # 如果图灵Key出现问题，那么reply将会是None
    reply = get_response(msg['Text'])
    # a or b的意思是，如果a有内容，那么返回a，否则返回b
    return reply or defaultReply


# 为了让修改程序不用多次扫码,使用热启动
itchat.auto_login(hotReload=True)
itchat.run()