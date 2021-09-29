from urllib.request import urlopen
from Functions import *

Announcements=Announcements_Check()
News=News_check()

while True:
    try:
        if Announcements!=Announcements_Check():
            tmp=Announcements_Check()

    except:
        pass

    try:
        urlopen("https://api.telegram.org/bot2022812772:AAEjZa3mqn3FMcNjIcB5LiRikLD_XFUagnA/sendPhoto?chat_id=@testtest19129&caption=mammad&photo=https://iu.edu.sa/uploads/news/103020.jpg")
    except:
        pass
