import requests
import json
import time
print "Welcome to Thank All Birthd.py"
start =raw_input("\nEnter the time after which all posts need to be liked and thanked.\nStrictly follow this format: dd/mm/yy HH:MM:SS (Use 24 hour format)\n")
start_time = int(time.mktime(time.strptime(start, '%d/%m/%Y %H:%M:%S')))
Token = raw_input("\nGo to https://developers.facebook.com/tools/explorer ,\nclick on get access token,\ncheck on all the permissions in basic and extended permissions \nand paste the access token here\n")
LIMIT = raw_input("\nHow many max posts are supposed to be liked and commented on?\n")
comment = raw_input("\nYour comment here!\n")

def thank():
    query = ("SELECT post_id, actor_id, message FROM stream WHERE "
            "filter_key = 'others' AND source_id = me() AND "
            "created_time > "+str(start_time)+" LIMIT " + str(LIMIT))

    payload = {'q': query, 'access_token': Token}
    r = requests.get('https://graph.facebook.com/fql', params=payload)
    result = json.loads(r.text)
    
    for wallpost in result['data']:
        requests.post("https://graph.facebook.com/" + str(wallpost['post_id'])
                      + "/likes/?access_token=" + Token
                      + "&method=POST")
        requests.post("https://graph.facebook.com/" + str(wallpost['post_id'])
                      + "/comments/?access_token=" + Token
                      + "&message=%s" % comment)
        r = requests.get("https://graph.facebook.com/"+str(wallpost['actor_id']))
        user = json.loads(r.text)
        print user['first_name']+"'s post liked and commented"
        
    print "\nThanked All!"

if __name__ == '__main__':
    thank()
