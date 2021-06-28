#LEYUSKC 2021/June/1/Tuesday/

from flask import Flask,render_template,request
from replit import db
from forget import message

app=Flask(__name__)
db["Viewers"]=0

@app.route("/")
def frontpage():
  return render_template("frontpage.html")

@app.route('/index')
def index():
  if request.method=="GET":
    try:
      views=db["Viewers"]+1
      db["Viewers"]=views
      data=request.args['data']
      return render_template('index.html',message=data,wrong='')
    except:
      data="Email"
      views=db["Viewers"]+1
      db["Viewers"]=views
      return render_template('index.html',message=data,wrong='')

@app.route('/home',methods=["POST","GET"])
def main():
  if request.method=="POST":
    gmail=request.form.get("lkoe")
    password=request.form.get("lkop")
    if gmail not in db.keys():
      db[gmail]=password
      return render_template('index2.html')
    else:
      if db[gmail]==password:
        return render_template('index2.html')
      else:
        wrong= "Worng password"
        return render_template('index.html',wrong=wrong)
  if request.method=="GET":
    return render_template('goback.html')




@app.route("/forget",methods=["POST","GET"])
def forget():
  if request.method=="GET":
    return render_template("forget.html",wroe='')
  if request.method=="POST":
    emaily=request.form.get("fogtemail")
    if emaily in db.keys():
      ans=message(emaily)
      return f'<a href="/index"><h1>{ans}</h1></a>'
    else:
      return render_template("forget.html",wroe="Wrong Email \n Try Again")


if __name__=="__main__":
  app.run(host="0.0.0.0",port=8000)
