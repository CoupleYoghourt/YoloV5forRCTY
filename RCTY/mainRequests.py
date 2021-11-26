import requests
import json

class VideoPart:
    def getVideo(self):
        url="http://81.68.149.16:8080/video/all"
        res = requests.get(url=url).json()
        if res["message"] == "success":
            for i,v in enumerate(res['data']):
                print(v)

    def CUsers(self, email, id, pwd, phone, name):
        url = "http://81.68.149.16:8080/user"
        HEADERS = {'Content-Type': 'application/json'}
        user = {
            "email": email,
            "id": id,
            "password": pwd,
            "phone": phone,
            "username": name
        }
        res = requests.post(url=url, data=json.dumps(user), headers=HEADERS).json()
        print(res)
        if res["message"] == "success":
            return 1
        else:
            return 0

a = VideoPart()
a.getVideo()