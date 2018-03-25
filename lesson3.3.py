from urllib.parse import urlencode
import requests
import json

app_id = 6423437
auth_url = "https://oauth.vk.com/authorize"
params = {
    "client_id": app_id,
    "display": "page",
    "scope": "friends",
    "response_type": "token",
    "v": "5.73"
}
response = requests.get("?".join([auth_url, urlencode(params)]))
print(("?".join([auth_url, urlencode(params)])))


def find_mutual_friends(source_user_id, target_id):
    api_url = "https://api.vk.com/method/"
    token = "8af6fa7f9eb2a3d0c4e2d378582667549987e6988d2c6e48d23497732a813e9d904959b747c5c67ef62b4"

    res = requests.get(api_url + "friends.getMutual", params={
        "target_uid": int(target_id),
        "source_id": int(source_user_id),
        "access_token": token,
        "v": "5.73"
    })
    mutual_friends_list = json.loads(res.text)["response"]
    mutual_friend_list_url = map(lambda x: "vk.com/id" + str(x), mutual_friends_list)
    print("Список общих друзей:")
    for num, friend in enumerate(mutual_friend_list_url):
        print(f"{num+1}. {friend}")

find_mutual_friends(2118307,54228217)
