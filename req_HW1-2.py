import requests
"""Определение самого умного супергероя"""


req_1 = requests.get(url="https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json")
intelligence = {"Hulk": None, "Captain America": None, "Thanos": None}
for k in req_1.json():
    if k["name"] in intelligence:
        intelligence[k["name"]] = k["powerstats"]["intelligence"]

print(f'Самый умный из трех супергероев это {max(intelligence)}')
###########################################################################

"""Загрузка файла на ЯДиск"""

class YaUploader:
    yandex_url = "https://cloud-api.yandex.net"
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)}

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href_response = self._get_upload_link(disk_file_path=disk_file_path)
        href = href_response.get("href", "")
        response = requests.put(url=href, data=open(filename, 'rb'))
        if response.status_code == 201:
            print("Success")
if __name__ == '__main__':
    TOKEN = ""
    ya = YaUploader(token=TOKEN)
    ya._get_upload_link("Netology/test1.txt")
    ya.upload_file_to_disk("Netology/test1.txt", "test.txt")