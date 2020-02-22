import requests

# scope=friends

TOKEN = ''  # insert your token here


class VKUser:
    def __init__(self, uid):
        self.uid = uid

    def __str__(self):
        return f'https://vk.com/id{self.uid}'

    def __and__(self, other):
        if isinstance(self, VKUser) and isinstance(other, VKUser):
            return self._get_mutual(self.uid, other.uid)
        else:
            return NotImplemented

    def _get_mutual(self, source_uid, target_uid):
        URL = 'https://api.vk.com/method/friends.getMutual'
        params = {
            'v': '5.52',
            'access_token': TOKEN,
            'source_uid': source_uid,
            'target_uid': target_uid
        }
        response = requests.get(URL, params=params)
        try:
            response.raise_for_status()
            if 'response' in response.json().keys():
                return [VKUser(uid) for uid in response.json()['response']]
            else:
                raise requests.exceptions.HTTPError(response.status_code, response.json()['error']['error_msg'])
        except requests.exceptions.HTTPError as error:
            print(error)
            return []


if __name__ == '__main__':
    users = VKUser('3476646') & VKUser('133238226')
    for user in users:
        print(user)
