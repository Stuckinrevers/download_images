import requests
from bs4 import BeautifulSoup


url = input('enter the url to get images\n')
headers = {
    'user-agent': 'YOUR_USER_AGENT'
}

def extract_links(url):
    html = requests.get(url, headers=headers)
    bs = BeautifulSoup(html.text, 'html5lib')
    images = []
    for img in bs.find_all('img'):
        src = str(img.get('src'))
        images.append(src)

    return images

def filter_images(images_list=[]):
    for link in images_list:
        if 'http' not in link:
            images_list.remove(link)
    return images



def download_pics_in_url(images_list=[]):
    i =1
    for image in images_list:
        img_name = 'media'+str(i)
        if '.jpg' in image:
            final_img_name = img_name+'.jpg'
            print('downloading ',image)
            open(final_img_name, 'wb').write(requests.get(image).content)
        elif '.png' in image:
            final_img_name = img_name+'.png'
            print('downloading ', image)
            open(final_img_name, 'wb').write(requests.get(image).content)
        i+=1


images = extract_links(url)
filter_images(images)
print(images)
download_pics_in_url(images)







