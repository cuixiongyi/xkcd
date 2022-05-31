import requests
import os

json_url_template='https://xkcd.com/{}/info.0.json'

def download(idx, dest_dir):
    json_url=json_url_template.format(idx)
    resp = requests.get(json_url,'GET')

    img_url = resp.json()['img']
    resp2 = requests.get(img_url,'GET')
    img_name = img_url.split('/')[-1]
    with open(os.path.join(dest_dir,img_name), 'wb') as f:
        f.write(resp2.content)

if __name__ == '__main__':

    for i in range(300):
        download(i+1,'xkcd_imgs')


