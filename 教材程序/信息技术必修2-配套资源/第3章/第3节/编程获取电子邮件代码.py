import poplib # 引入处理协议的库
from email import parser
from email.header import decode_header

server= poplib.POP3_SSL("xx.XXX.XXX') 
# PoPv3服务器
server.user(xxxx)
# 用户名
server.pass_(xxxx)
#密码
resp,mails,octets=server.list()
#获取邮件列表
print("共有‰d封邮件." %1en( mails))

for index in range(len(mails))：
    resp,lines,octets=server.retr(index+1)
    msg_content =b'\r\n'.join(lines).decode('utf-8')
    msg=parser.Parser().parsestr(msg_content)
    emailbase={}
for line in msg.items()：
    header=line[0]
    if header in ['From，'Subject，'Date：
item=decode header(line[1])[-1]
code=item[1 if item[1！=None else 'ascii
if isinstance(item[o]， bytes)：value= str(item[0]， code)
else value item[0]
emailbase[header]value
print("-------0%d/%d-------%( index+1，len(mai1s)))
print("发信信箱："+ emailbase["From'])
print("信件主题："+ emailbase' Subject'])
print("发信时间："+ emailbase"Date"]
server. quit()