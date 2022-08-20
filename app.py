from urllib import request
from flask import Flask, render_template
from flask import request
import urllib.parse

app = Flask(__name__)

@app.route('/')

def index():
  return render_template('frame.html')

@app.route("/youtube", methods=["GET"]) 
def frame():
  url1 = request.args['url1']
  text1= urllib.parse.urlparse(url1).query
  text1=text1.replace('v=','')
  url1= 'https://www.youtube.com/embed/'+text1
  url2 = request.args['url2']
  text2= urllib.parse.urlparse(url2).query
  text2=text2.replace('v=','')
  url2= 'https://www.youtube.com/embed/'+text2
  url3 = request.args['url3']
  text3= urllib.parse.urlparse(url3).query
  text3=text3.replace('v=','')
  url3= 'https://www.youtube.com/embed/'+text3
  url4 = request.args['url4']
  text4= urllib.parse.urlparse(url4).query
  text4=text4.replace('v=','')
  url4= 'https://www.youtube.com/embed/'+text4
  url5 = request.args['url5']
  text5= urllib.parse.urlparse(url5).query
  text5=text5.replace('v=','')
  url5= 'https://www.youtube.com/embed/'+text5
  url6 = request.args['url6']
  text6= urllib.parse.urlparse(url6).query
  text6=text6.replace('v=','')
  url6= 'https://www.youtube.com/embed/'+text6

  responce=render_template('youtube.html',url1=url1,url2=url2,url3=url3,url4=url4,url5=url5,url6=url6) 
  return responce


  
## おまじない
if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port=80)