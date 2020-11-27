import imaplib
import re
conn = imaplib.IMAP4_SSL("imap.gmail.com", 993)
gmail_user = 'xxxxxxxx@gmail.com'
gmail_pwd = 'xxxxxxx'


conn.login(gmail_user, gmail_pwd)
conn.select()
count= 0
file = open('msgid.txt', "wb")
status, data = conn.search(None, 'FROM', "contacto@mail.somosmach.com")
for num in data[0].split():
    print(data[0][1])
    typ, data = conn.fetch(num, '(BODY[HEADER.FIELDS (MESSAGE-ID)])')
    typ, data2 = conn.fetch(num, '(BODY[HEADER.FIELDS (FROM)])')
    count = count+1
    if count >= 29:
            file.write(data[0][1] + data2[0][1])


file.close()
#muestra 20 correos de la direccion asiganada, los muestra desde el mas antiguo al mas nuevo
print(count)
