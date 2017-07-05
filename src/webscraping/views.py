from django.shortcuts import render
from django.views import View

# from .function import video_parse, hot_video_parser, search_video_parser
from .function import video_parse

import requests
from bs4 import BeautifulSoup
import re

def test(request):
    video_parse()
    search = request.GET.get("q")
    page = request.GET.get('sp')
    page_link = {}
    show = []
    if page is not None:
        current_page = request.GET.get('current_page')
        value = "q={}".format(search) + "&" + "sp={}".format(page)
        search_req = requests.get("https://www.youtube.com/results?{}".format(value))
        (show, page_link) = video_parse.search_video_parser(search_req)
        page_link = sorted(page_link.items())
        after =0
        for key, value in page_link:
            after = after+1
            if(key > current_page):
                break
        previous = after -1
        return render(request, "webscraping/test2.html", {"obj": show, "q":search, "current_page":current_page,"previous":previous,
                        "after":after, "all_page":page_link})
    elif search :
        search_video = requests.get("https://www.youtube.com/results?search_query={}".format(search))
        (show, page_link) = video_parse.search_video_parser(search_video)
    else :
        show = video_parse.hot_video_parser()

    # for x in range(0, len(show)):
    #     print (show[x])
    #     print('\n')
    return render(request, "webscraping/test2.html", {"obj": show, "q":search,
                            "all_page":sorted(page_link.items())})
