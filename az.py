import requests
import re

def find_answer(n, id):
    url = "https://math-ege.sdamgia.ru/problem?id="+str(id)
    try:
        pattern = '<div class="answer" style="display:none"><span style="letter-spacing: 2px;">[^<>=:" ]{5}: [a-zA-Z0-9,\-]*</span></div>'
        r = requests.get(url).text
        res = re.findall(pattern, r)[0].replace('<div class="answer" style="display:none"><span style="letter-spacing: 2px;">', "")[6:].replace("</span></div>", "")
        if n<10:
            return res + " "*(12-len(res)) + url
        else:
            return res + " "*(11-len(res)) + url
    except Exception:
        return "Unknown"

def get_ans(t)  :  
    retu = {}
    k = re.findall("comments[0-9]*", t)
    for i in range(len(k)):
        retu[i+1] =  find_answer(i+1, k[i].replace("comments", ""))
    return retu
