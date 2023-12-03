import requests
import re
import os

current_dir = os.getcwd()

t = open(current_dir.replace("az", "1.html"), "r", encoding="utf-8").read()

def find_answer(id):
    url = "https://math-ege.sdamgia.ru/problem?id="+str(id)
    pattern = '<div class="answer" style="display:none"><span style="letter-spacing: 2px;">[^<>=:" ]{5}: [a-zA-Z0-9,]*</span></div>'
    r = requests.get(url).text
    res = re.findall(pattern, r)[0].replace('<div class="answer" style="display:none"><span style="letter-spacing: 2px;">', "")[6:].replace("</span></div>", "")
    return res

def get_ans(t)  :  
    k = re.findall("comments[0-9]*", t)
    for i in range(len(k)):
        print(i+1, find_answer(k[i].replace("comments", "")))

get_ans(t)