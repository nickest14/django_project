import requests
from bs4 import BeautifulSoup
import re

class video_parse():
    print('')
    def hot_video_parser():
        url = 'https://www.youtube.com/feed/trending'
        youtube_hot = requests.get(url)
        youtube_hot_soup = BeautifulSoup(youtube_hot.text, 'html.parser')
        # youtube_hot_list = youtube_hot_soup.findAll('div', {'id': 'item-section-239140', 'class':'item-section'})
        youtube_hot_list = youtube_hot_soup.findAll('div', {'id': '', 'class':'item-section'})
        youtube_hot_list2 = youtube_hot_soup.findAll('li', {'class': 'expanded-shelf-content-item-wrapper'})
        show = []

        for hot_list in youtube_hot_list2:
            obj = {}
            information = hot_list.findAll('a', {'class': 'yt-uix-tile-link'})
            obj['time'] = hot_list.findAll('span', {'class':'video-time'})[0].text
            obj['imagelink'] = hot_list.findAll('img',{"alt": True, "width": True, "height": True, "onload": True, "data-ytimg": True})[0]['src']
            obj['title'] = information[0]['title']
            obj['link'] = information[0]['href']
            show.append(obj)
            if len(show) > 5 :
                break
        return show

    def search_video_parser(search_video):
        content = search_video.content
        search_video_soup = BeautifulSoup(content, 'html.parser')
        show = []
        page = {}
        for page_value in search_video_soup.find_all('a', {"class": True, "data-visibility-tracking": True, "data-sessionlink": True,
                                          "aria-label": True, }):
             page['{}'.format(page_value.text)] = page_value.get('href')
        i = 0
        for element in search_video_soup.find_all('a', {"rel": "spf-prefetch"}):
            obj = {}
            obj['title'] = element['title']
            obj['link'] = element['href']
            obj['imagelink'] = '12345'
            img_value = element.get('href').split("=")[1]
            all_img = search_video_soup.find_all('img', {"alt": True, "width": True, "height": True, "onload": True, "data-ytimg": True})
            img = str(re.findall("https://i.ytimg.com/vi/{}/[\S]+".format(img_value), str(all_img))).strip("[\"\']")
            obj['imagelink'] = img.replace("&amp;", "&")

            # url = "https://www.youtube.com/" +element['href']
            # search_video_soup = BeautifulSoup(content, 'html.parser')
            # views_req = requests.get(url)
            # views_soup = BeautifulSoup(views_req.content, 'html.parser')
            # views = views_soup.find_all('div', {"class": "watch-view-count"})
            # obj['views'] = views[0].text
            # print( views[0].text)  #花費太多時間

            show.append(obj)
        for time in search_video_soup.find_all('span', {"class": "video-time"}):
            show[i]['time'] = time.text
            i = i+1
        test = '12345'
        return (show, page)
