import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
                                params={'path': file_path},
                                headers={'Authorization': f'OAuth {token}'})
        href = response.json()['href']
        with open(file_path) as f:
            requests.put(href, files={'file': f})
        return 'Вернуть ответ об успешной загрузке'

if __name__ == '__main__':
    with open('YandexDiskTOKEN.txt') as f:
        token = f.readline()
    uploader = YaUploader(token)
    result = uploader.upload('test_text_to_upload.txt')