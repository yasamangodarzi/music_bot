import telebot.apihelper
from youtubesearchpython import *
import requests
import pymongo
myclient = pymongo.MongoClient()
mydb = myclient["Music_bot"]
mycol = mydb["songs"]
def compare(a, b):
    return [c for c in a if c.isalpha()] == [c for c in b if c.isalpha()]
def work(input_text):
    user_message=str(input_text).lower()
    #musiclist = mycol.find()
    musiclist = mycol.find({"name":{"$regex":user_message}})
    lid = []
    for x in musiclist:
        if compare(x["name"],user_message):
            print(x["name"] + x["address"])
            return x["address"]
    print("not in mongo")
    response = requests.get("http://api.codebazan.ir/music/?type=search&query={}&page=1".format(user_message)).json()
    print("so we made a request")
    Title = response["Result"]
    answer = ""
    for x in Title:
         y = x["Title"]
         yg = x["Link"]
         mydict = {"name": str(y), "address": str(yg)}
        # print(y)
        # print(yg)
         best=y+"\n"+yg+"\n"
         lid.append(best)
         mycol.insert_one(mydict)
         #answer = answer + y + "\n" + yg + "\n"
    for x in range(3):
        answer = answer + lid[x]

    print(answer)
    return answer
   # print(answer)


