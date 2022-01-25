import requests
import pymongo
myclient = pymongo.MongoClient()
mydb = myclient["Music_bot"]
mycollection = mydb["songs"]
def compare(a, b):
    return [c for c in a if c.isalpha()] == [c for c in b if c.isalpha()]
def work(input_text):
    user_message=str(input_text).lower()
    music_list_db = mycollection.find({"name" : {"$regex":user_message}})

    list_show = []
    for x in music_list_db:
        print(x["name"])
        return x["address"]
        if compare(x["name"],user_message):
            print(x["name"] + x["address"])
            return x["address"]
    print("not in mongo")
    response = requests.get("http://api.codebazan.ir/music/?type=search&query={}&page=1".format(user_message)).json()
    print("so we made a request")
    Title = response["Result"]
    answer = ""
    for x in Title:
         titer = x["Title"]
         url = x["Link"]
         my_dictionary = {"name": str(titer), "address": str(url)}
         find_name_song=titer+"\n"+url+"\n"
         list_show.append(find_name_song)
         mycollection.insert_one(my_dictionary)
    for x in range(3):
        answer = answer + list_show[x]
    print(answer)
    if answer=="":
     return "we can not find the song you are looking for..."
    return answer
