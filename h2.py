import requests
import os

class YaUploader:

    host = 'https://cloud-api.yandex.net:443/'

    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""

        headers = {
                  "Authorization": token
                    }
        url = 'v1/disk/resources/upload/'
        request_url = self.host + url
        params = {'path': 'file.jpg', 'overwrite': True}
        resp = requests.get(request_url, headers=headers, params=params).json()
        upload_link = resp.get('href')
        response = requests.put(upload_link, data=open(path_to_file, 'rb'), headers=headers)
        print(response.status_code)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = os.path.abspath('20200713_185555.jpg')
    token = 
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
