import poplib  

from email import parser
from email.header import decode_header

host = 'pop.sina.com'  
username = 'xxxxxx@sina.com'  
password = 'xxxxxx'    
server = poplib.POP3_SSL(host)  
server.user(username)  
server.pass_(password)

#获取邮件列表
resp, mails, octets = server.list()
print("共有 %d 封邮件." % len(mails))

for index in range(len(mails)):
    resp, lines, octets = server.retr(index+1)
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    msg = parser.Parser().parsestr(msg_content)
    emailbase={}

    for line in msg.items():
        header=line[0]
        if header in ['From','Subject']:
            item=decode_header(line[1])[-1]                
            code=item[1] if item[1]!=None else 'ascii'
            if isinstance(item[0], bytes) :value= str(item[0],code)
            else :value=item[0]
            emailbase[header]=value
    
    print("-----------%d/%d-----------"%(index+1,len(mails)))
    print("发信信箱:"+emailbase['From'])
    print("信件主题:"+emailbase['Subject'])

server.quit()
