from urllib.request import urlopen
import urllib
import re

def get_html(url):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html


def Announcements_Check():
    url = "https://iu.edu.sa/announcements"
    reg_items = "<li>(.*?)</li>"
    reg_title = "\">(.*)<span"
    reg_link = "<a href=\"(.*?)\">"
    img_reg = "<img src=\"(.*?)\" alt"
    html=get_html(url)
    begin = html.find("<ul class=\"fac-ads-list spec-list\">")
    html = html[begin:]
    end = html.find("</ul>")
    html = html[:end]
    items = re.findall(reg_items, html)
    Announcements=[]
    for item in items:
        link=re.findall(reg_link, item)[0]
        title=re.findall(reg_title, item)[0]
        title=str(title).replace("&quot","\"")
        link_for_img="https://iu.edu.sa" + link
        img_html=get_html(link_for_img)
        img_link = (re.findall(img_reg, img_html)[-1])
        if img_link.startswith("/"):
            img_link = "iu.edu.sa" + img_link
        if img_link == "iu.edu.sa/images/pdf.png":
            img_link="iu.edu.sa/images/logo.png"
        Announcements.append((link,title,img_link))



    return Announcements

def News_check():
    url = "https://iu.edu.sa/all_news"
    html=get_html(url)
    begin = html.find("listwrapper grid")
    html = html[begin:]
    html = html.replace("\r", "")
    html = html.replace("\n", "")
    html=html.replace("&quot","\"")
    reg_link = "<div class=\"img-container img-eff\">.*?<a href=\"(.*?)\""
    reg_title = "<div class=\"caption\">.*?<a href=.*?>(.*?)</a>"
    Title = (re.findall(reg_title, html))
    Link = (re.findall(reg_link, html))
    News=list(zip(Link,Title))
    return News


