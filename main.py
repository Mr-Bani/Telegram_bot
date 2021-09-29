from urllib.request import urlopen
from Functions import *

Announcements=Announcements_Check()
News=News_check()

while True:
    try:
        AnnounceCheck=Announcements_Check()
        if Announcements!=AnnounceCheck:
            i=AnnounceCheck[0]
            link = i[0]
            title = i[1]
            img_link = i[2]
            caption = urllib.parse.quote("🔵#اعلان" + "\n\n" + title + "\n\n\nhttps://iu.edu.sa" + link)
            urlopen(
                "https://api.telegram.org/bot2022812772:AAEjZa3mqn3FMcNjIcB5LiRikLD_XFUagnA/sendPhoto?chat_id=@iumedina&photo={}&caption={}".format(
                    img_link, caption))
    except:
        pass

    try:
        NewsCheck=News_check()
        if News!=NewsCheck:
            link = i[0]
            img_link = "iu.edu.sa/uploads/news/" + i[0].split("/")[2] + ".jpg"
            title = i[1]
            caption = urllib.parse.quote("🔴#الخبر" + "\n\n" + title + "\n\n\nhttps://iu.edu.sa" + link)
            urlopen(
                "https://api.telegram.org/bot2022812772:AAEjZa3mqn3FMcNjIcB5LiRikLD_XFUagnA/sendPhoto?chat_id=@iumedina&photo={}&caption={}".format(
                    img_link, caption))
    except:
        pass
