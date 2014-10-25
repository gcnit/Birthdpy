import requests
import json
import time
print "Welcome to Thank All Birthd.py"
start =raw_input("\nEnter the time after which all posts need to be liked and thanked.\nStrictly follow this format: dd/mm/yy HH:MM:SS (Use 24 hour format)\n")
start_time = int(time.mktime(time.strptime(start, '%d/%m/%Y %H:%M:%S')))
Token = raw_input("\nGo to https://developers.facebook.com/tools/explorer ,\nclick on get access token,\ncheck on all the permissions in basic and extended permissions \nand paste the access token here\n")
LIMIT = raw_input("\nHow many max posts are supposed to be liked and commented on?\n")
comment = raw_input("\nYour comment here!\n")

wishes = ["birthday", "bday", "b'day", "bdy", "returns"]
self_id = json.loads(requests.get("https://graph.facebook.com/me?access_token=" + Token).text)['id']

def thank():
    r = requests.get("https://graph.facebook.com/me/feed?since=" + str(start_time) + "&limit=" + str(LIMIT) + "&access_token=" + str(Token))
    result = json.loads(r.text)
    for wallpost in result['data']:
        if str(wallpost['from']['id']) == self_id:
            continue
        for wish in wishes:
            if wish in str(wallpost['message']).lower():
                requests.post("https://graph.facebook.com/" + str(wallpost['id']) + "/likes/?access_token=" + str(Token) + "&method=POST")
                requests.post("https://graph.facebook.com/" + str(wallpost['id']) + "/comments/?access_token=" + str(Token) + "&message=" + str(comment))
                user = wallpost['from']['name']
                print user+"'s post liked and commented"
                break
        
    print "\nThanked All!"

if __name__ == '__main__':
    thank()
