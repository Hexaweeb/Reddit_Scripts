import requests
import json
import shutil
import os
import time

'''
This code is kinda messy. *shrug*
'''

sub_reddit = raw_input('Subreddit:')
headers = { 'User-Agent': '/u/Username' }

def main():
    url = 'http://reddit.com/r/' + sub_reddit + '.json'
    fetch = requests.get(url, headers=headers)
    data = json.loads(fetch.text)
    children = data['data']['children']
    index = 0
    
    for child in children:
        time.sleep(1)
        index = index + 1
        
        if child['data'].get('preview'):
            preview_img = child['data']['preview']['images'][0]['source']['url']
            dl = requests.get(preview_img, stream=True)
            with open(sub_reddit + str(index) + '.jpg', 'wb') as out_file:
                shutil.copyfileobj(dl.raw, out_file)
            del dl
        if child['data'].get('url'):
            if 'reddit' not in child['data']['url']:
                image = child['data']['url']
                dl = requests.get(image, stream=True)
                
                if '.png' in image:
                    with open(sub_reddit + str(index) + '.png', 'wb') as out_file:
                        shutil.copyfileobj(dl.raw, out_file)
                    del dl
                if '.jpg' in image:
                    with open(sub_reddit + str(index) + '.jpg', 'wb') as out_file:
                        shutil.copyfileobj(dl.raw, out_file)
                    del dl
                
main()