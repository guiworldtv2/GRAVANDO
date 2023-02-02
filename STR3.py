import requests
from bs4 import BeautifulSoup
import datetime
import streamlink

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

m3u8_file = open("lista3str3.m3u", "w")

url = "https://www.youtube.com/results?search_query=aula&sp=CAISBBABGAI%253D"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

video_titles = [item.text for item in soup.find_all("yt-formatted-string", class_="style-scope ytd-video-renderer")]
video_images = [item["src"] for item in soup.find_all("img", class_="yt-core-image")]
video_links = [f"https://www.youtube.com{item['href']}" for item in soup.find_all("a", class_="yt-simple-endpoint")]


for title, image, link in zip(video_titles, video_images, video_links):
    now = datetime.datetime.now()
    timestamp = now.strftime("%m%d%H%M%S")
    video_url = streamlink.streams(link)["best"].url if streamlink.streams(link) else None
    video_link = soup.find("a", class_="goto_media")['yt-simple-endpoint']
    item = soup.find("href", class_="a", href=link)
    try:
        image_url = item["style"].split("url(")[1].split(")")[0]
    except Exception as e:
        print(f"Error: {e}")
        image_url = "https://cdn.rtve.es/resources/png/2/0/1607938114762.png"
    if video_url:
        m3u8_file.write(f"#EXTINF:-1 tvg-group=\"RTVE La 1\" tvg-logo=\"{image_url}\",{title}\n{video_url}\n")
        m3u8_file.write("\n")

m3u8_file.close()
