import os
import re
import time

import requests

directory = "gifs"
api = "https://tiktok-info.p.rapidapi.com/dl/"

headers = {
    'x-rapidapi-host': "tiktok-info.p.rapidapi.com",
    'x-rapidapi-key': "f9d65af755msh3c8cac23b52a5eep108a33jsnbf7de971bb72"
}


def download_video(url: str):
    link = re.findall(r'\bhttps?://.*[(tiktok)]\S+', url)[0].split("?")[0]

    params = {
        "link": link
    }

    _path = os.getcwd() + f"/{directory}/" + str(int(time.time())) + '.gif'
    r = requests.get(api, params=params, headers=headers).json()['videoLinks']['download']
    with requests.get(r, timeout=(50, 10000), stream=True) as req:
        if 200 <= req.status_code < 300:
            try:
                os.mkdir(directory)
            except FileExistsError:
                pass
            with open(_path, 'wb') as f:
                f.write(req.content)

            return _path
        return "Video doesn't exist"


if __name__ == '__main__':
    url = "https://www.tiktok.com/@bellapoarch/video/6862153058223197445?is_copy_url=1&is_from_webapp=v1&lang=en"
    print(download_video(url))
