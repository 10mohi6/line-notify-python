import requests


class Line:
    def __init__(self, *, token):
        self.url = "https://notify-api.line.me/api/notify"
        self.headers = {"Authorization": "Bearer " + token}

    def post(self, **kwargs):
        files = kwargs.get("imageFile", None)
        if files is not None:
            files = {"imageFile": open(kwargs["imageFile"], "rb")}
        return requests.post(
            self.url, headers=self.headers, params=kwargs, files=files
        ).json()
