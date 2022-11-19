import smtplib
from email.mime.text import MIMEText

mailto_list=["emailrobot@sina.com","kate080512@sina.com"]    
mail_host="smtp.sina.com"                   #发送服务器的地址
mail_user="kate080512@sina.com"             #发信人账号
mail_pass="xxxxxx"                          #密码

msg = MIMEText('这是我用程序发送的一封电子邮件。')   #邮件内容
msg['Subject'] = '用程序发送的电子邮件'              #设置主题  
msg['From'] = '<'+mail_user+'>'                      #发件人  
msg['To'] = ";".join(mailto_list)                    #收件人


#开始发送
try:  
    s = smtplib.SMTP()                                        
    s.connect(mail_host)  
    s.login(mail_user,mail_pass)  
    s.sendmail(mail_user, mailto_list, msg.as_string())  
    s.close()  
    print ("发送成功"  )
except Exception as e:  
    print(str(e) )
    print ("发送失败"  )
    
        
