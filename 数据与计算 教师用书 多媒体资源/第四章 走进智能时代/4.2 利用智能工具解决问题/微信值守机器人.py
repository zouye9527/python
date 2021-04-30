import itchat
import sinomaps
KEY='4d1273276b3448ea89c32121ee4cadd8'

@itchat.msg_register(itchat.content.TEXT)

def tuling_reply(msg):
    defaultReply='我收到：'+msg['Text']
    reply=sinomaps.get_response(msg['Text'],KEY)
    if reply:
        return reply
    else:
        return defaultReply
itchat.auto_login(hotReload=True)
itchat.run()
    
