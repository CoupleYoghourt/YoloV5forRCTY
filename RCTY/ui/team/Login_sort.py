import requests
import json


class User_part:
    def Login(self, id, pwd):
        url="http://81.68.149.16:8080/user/login"
        data = {
            "account": id,
            "password": pwd
        }
        res = requests.post(url=url, data=data).json()
        print(res)
        if res["message"] == "success":
            return 1
        else:
            return 0

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

    def UPdate_User(self, email, id, pwd, phone, name):
        url = "http://81.68.149.16:8080/user"
        HEADERS = {'Content-Type': 'application/json'}
        user = {
            "email": email,
            "id": id,
            "password": pwd,
            "phone": phone,
            "username": name
        }
        res = requests.put(url=url, data=json.dumps(user), headers=HEADERS).json()
        print(res)
        return 1

    def Find_User(self, id):
        url = "http://81.68.149.16:8080/user"
        HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
            "id": id
        }
        res = requests.get(url=url, params=data, headers=HEADERS).json()
        print(res)
        return 1

    def DEL_User(self, id):
        url = "http://81.68.149.16:8080/user"
        HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
            "id": id
        }
        res = requests.delete(url=url, data=data, headers=HEADERS).json()
        print(res)
        return 1


#a = User_part()
#a.Login('123456',"123456")
# Login('123456','qweqwe123')
# CUsers("411294809@qq.com",123456,"qweqwe123","123111","帅哥")
# UPdate_User("411294809@qq.com",123456,"qweqwe123","123111","帅哥")
# Find_User(12)
# DEL_User('22')
# CR_Res(123,"你是帅哥！","这软件真好！",1)
# Find_Res(1)
# Update_Res(123,"你是帅哥！","这软件真好！",1)
# DEL_Res(22)
# a.CUsers("411294809@qq.com",16,"qweqwe123","123111","帅哥")
# a.Login('123111',"qweqwe123")
# b.Find_Res(123)