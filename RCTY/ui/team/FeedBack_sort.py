import requests
import json

class Suggest_part:
    def CR_Res(self, id, text, title, type):
        url = "http://81.68.149.16:8080/reply"
        HEADERS = {'Content-Type': 'application/json'}
        data = {
            "id": id,
            "text": text,
            "title": title,
            "type": type
        }
        res = requests.post(url=url, data=json.dumps(data), headers=HEADERS).json()
        if res["message"] == "success":
            return 1
        else:
            return 0

    def Find_Res(self, id):
        url = "http://81.68.149.16:8080/reply"
        HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
            "id": id
        }
        res = requests.get(url=url, params=data, headers=HEADERS).json()
        print(res)
        return 1

    def Update_Res(self, id, text, title, type):
        url = "http://81.68.149.16:8080/reply"
        HEADERS = {'Content-Type': 'application/json'}
        data = {
            "id": id,
            "text": text,
            "title": title,
            "type": type
        }
        res = requests.put(url=url, data=json.dumps(data), headers=HEADERS).json()
        print(res)
        return 1

    def DEL_Res(self, id):
        url = "http://81.68.149.16:8080/reply"
        HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
            "id": id
        }
        res = requests.delete(url=url, data=data, headers=HEADERS).json()
        print(res)
        return 1