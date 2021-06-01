
def message(reciv):
  import os
  import smtplib, ssl
  from replit import db
  port = 465
  smtp_server = "smtp.gmail.com"
  messagey=f"YOUR PASSWORD IS {db[reciv]}.Thank you for playing this game hope you would continue using it"
  context = ssl.create_default_context()
  try:
    with smtplib.SMTP_SSL(smtp_server, port, context=context)as server:
      server.login(os.environ['emailvalue'], os.environ['passvalue'])
      server.sendmail(os.environ['emailvalue'], reciv, messagey)
      return "Check your email"
  except:
    return "Email address you provided is invalid sorry can't recover it."



if __name__=="__main__":
  tr="amail@mail.com"
  message(tr)