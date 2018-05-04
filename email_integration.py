import parse_mail
import helpers
class data():
    title=''
    times=set([])
    dates=set([])
    reg=0
    venue=''
    links=[]

def get_data():
    from backports import ssl
    from imapclient import IMAPClient
    import getpass
    import pyzmail
    import re
    
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    imapObj = IMAPClient('imap.iitb.ac.in', ssl=True, ssl_context=context)
    username='170070015'#input("Enter username")
    password='anshar$2000'#getpass.getpass("Enter password")
    imapObj.login(username,password)
    imapObj.select_folder("INBOX.Python script","r")
    date=helpers.getdate()
    UIDs=imapObj.search(date)
    add_this=set([])
    
    for i in UIDs:
        
        Mail=imapObj.fetch([i],['BODY[]','FLAGS'])
       # print(Mail)
        message = pyzmail.PyzMessage.factory(Mail[i][b'BODY[]'])
        sub=message.get_subject()
        
        text=(parse_mail.clean_up(message.text_part.get_payload().decode(message.text_part.charset)))
        #call parser functions
        if(len(parse_mail.get_title(sub))):
            ret=data()
            ret.title=parse_mail.get_title(sub)
            ret.times=parse_mail.get_time(text)
            ret.dates=parse_mail.get_date(text)
            ret.reg=parse_mail.check_reg(text)
            ret.links=parse_mail.get_links(text)
            ret.venue=parse_mail.get_venue(text)
            add_this.add(ret)

    return add_this


