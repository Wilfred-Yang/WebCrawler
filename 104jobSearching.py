import requests
from bs4 import BeautifulSoup
import prettytable

word = input("請輸入關鍵字: ")

def search(page=1):
    response = requests.get("https://www.104.com.tw/jobs/search/",
                            headers = {"Cookie":"__auc=6fe99e4d1716879a89fbcfd8187; _ga=GA1.3.1525772037.1586595736; _ga_W9X1GB1SVR=GS1.1.1614856951.9.0.1614856951.60; _ga_FJWMQR9J2K=GS1.1.1614856951.8.0.1614856951.60; _hjid=9fad8fa1-4bc2-47c3-956a-8411c4a9ad9b; TS016ab800=01180e452d442259683e2bbb39e883d11aa5b3b539aacc1ab12eb91b9a7ac18af2704fb45b2751b4d2eb7b85a945983fd9fdb2a2309b38c32856320ea31bdf54444b083be8a664034277df0312281c294bcf9a9ef6; lup=1972228329.4623532291991.5035849152215.1.4640712161167; luauid=1972228329; lunp=5035849152215; _gid=GA1.3.1598141899.1614841766; ALGO_EXP_6019=D; job_same_ab=1",
                                       "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"},
                            params= {"ro":"0",
                                     "kwop":"7",
                                     "keyword":str(word),
                                     "order":"15",
                                     "asc":"0",
                                     "page":str(page),
                                     "mode":"s",
                                     "jobsource":"2018indexpoc"})

    t = prettytable.PrettyTable(["職稱", "公司", "地點", "經歷", "學歷"], encoding="utf-8")
    b1 = BeautifulSoup(response.text, "html.parser")
    job_names = b1.find_all("article", {"class":"job-list-item"})
    job_locations = b1.find_all("ul", {"class":"b-list-inline b-clearfix job-list-intro b-content"})

    for i in range(0, len(job_locations)):
        others = job_locations[i].text.split("\n")
        location, experience, school = others[1], others[3], others[5]
        t.add_row([job_names[i].attrs["data-job-name"], job_names[i].attrs["data-cust-name"], location, experience, school])
    print(t)

search()
while True:
    try:
        page = int(input("輸入頁碼: "))
    except:
        print("輸入頁碼錯誤")

    search(page=page)
