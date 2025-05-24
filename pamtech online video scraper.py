import requests


import requests

def get_page_id(page_username, access_token):
    url = f'https://graph.facebook.com/v12.0/{page_username}?fields=id&access_token={access_token}'
    response = requests.get(url)
    data = response.json()
    page_id = data.get('id')
    return page_id


# Replace these with your page username and access token
page_username = 'Pamtech'
access_token = 'EAAUPaZAWJoI8BAMZCtP3SC8kZB1NDLeZADfYP93BLQ3eG5qdZC0EI29dmqZBV7RsB9L2jP0vgrLzmEqxZCOO6jSGtJSDm1TxFzqKZBTkESmA4GOjHZA738ky4vauNefQd0MNY0k1no2mMg40fRDAUW0ihIP2DRUoA9RnjRmyT1poUOysl4NZANOY2v'

page_id = get_page_id(page_username, access_token)
print(f"Page ID: {page_id}")

# Make a GET request to fetch the videos from the page
url = f'https://graph.facebook.com/{page_id}/videos?access_token={access_token}'
response = requests.get(url)
data = response.json()



def get_page_videos(page_id, access_token):
    url = f'https://graph.facebook.com/{page_id}/videos?fields=permalink_url&access_token={access_token}'
    response = requests.get(url)
    data = response.json()
    videos = data.get('data', [])

    video_links = []
    for video in videos:
        video_link = video.get('permalink_url')
        if video_link:
            video_links.append(video_link)

    return video_links

video_links = get_page_videos(page_id, access_token)
for link in video_links:
    print(link)


