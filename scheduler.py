import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("muskantaj.mt@gmail.com","xxxxxxx")
msg="hi,how are you"
s.sendmail("muskantaj.mt@gmail.com","sumaiyachachiya65@gmail.com",msg)
print("success")
s.close()
