
from flask import *
import requests
import json
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")





@app.route("/keyword/<keyword>", methods=['GET'])
def getKeywords(keyword):
        URLS = [f"https://duckduckgo.com/ac/?q={keyword}&kl=wt-wt", f"https://search.brave.com/api/suggest?q={keyword}"]


        duck =  f"https://duckduckgo.com/ac/?q={keyword}&kl=wt-wt"
        brave = f"https://search.brave.com/api/suggest?q={keyword}"
        times = 0
        a = requests.get(duck)
        b = requests.get(brave)
        result1 = json.loads(a.content.decode("utf-8"))
        result1 = str(result1)
        result1 = result1.replace("[", "").replace("]", "").replace("'", "").replace(",", "\n").replace("{", "").replace("}", "").replace("google:suggestsubtypes:", "").replace("äòáøú áòìåú", '').replace("phrase: ", "").replace(F" {keyword} ", "").replace(F"{keyword}", "")
        result1 = ''.join([i for i in result1 if not i.isdigit()])
        result = json.loads(b.content.decode("utf-8"))
        result = str(result)
        result = result1.replace("[", "").replace("]", "").replace("'", "").replace(",", "\n").replace("{", "").replace("}", "").replace("google:suggestsubtypes:", "").replace("äòáøú áòìåú", '').replace("phrase: ", "").replace(F" {keyword} ", "").replace(F"{keyword}", "")
        result = ''.join([i for i in result if not i.isdigit()])
        all = result1 + "/n" + result
        return all
        


app.run()