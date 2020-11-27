import imaplib
import re
conn = imaplib.IMAP4_SSL("imap.gmail.com", 993)
gmail_user = 'xxxxx@gmail.com'
gmail_pwd = 'xxxxxx'


ex1= "[a-ba-z0-9]{22}@ismptd0[0-9]{3}[a-z0-9]sendgrid.net"
ex2 = "[a-ba-z0-9]{22}@geopod-ismptd-[1-9]-[1-9]"
patron1="sendgrid.net"
patron2= "geopod"
conn.login(gmail_user, gmail_pwd)
conn.select()
count= 0
#file = open('msgid2.txt', "wb")
status, data = conn.search(None, 'FROM', "contacto@mail.somosmach.com")
for num in data[0].split():
#    print(data[0][1])
    typ, data = conn.fetch(num, '(BODY[HEADER.FIELDS (MESSAGE-ID)])')
#    typ, data2 = conn.fetch(num, '(BODY[HEADER.FIELDS (FROM)])')
#    count = count+1
#    if count >= 29:
#            file.write(data[0][1] + data2[0][1])

msg = data[0][1].decode("utf-8")

x = re.search(patron1, msg)
if x != None:
    print(x)
    print("mensaje legitimo")
else:
    x = re.search(patron2, msg)
    if x != None:
        print(x)
        print("mensaje legitimo")
    else:
        print("es un mensaje falso")





#file.close()
#muestra 20 correos de la direccion asiganada, los muestra desde el mas antiguo al mas nuevo
print(count)
 #al no saber como hace uso de la expresion regular, solo use un patron de de los msg id, y use ese como indicador si era falso o no un correo
