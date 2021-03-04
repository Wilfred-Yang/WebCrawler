import requests
from bs4 import BeautifulSoup
import codecs
import json
import prettytable
# response = requests.get(
# 	"https://www.cwb.gov.tw/V8/C/W/TemperatureTop/County_TMax_T.html",
# 	headers = {
# 	        "Accept-Language":"zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3",
# 	        "Cookie":"V8_LANG=C; TS01c55bd7=0107dddfef4634fe7fa8bc4302721e18261cfad648bf2d6caa0a67b139fd739b30aab8ba5a; _ga=GA1.3.1353783014.1586596932; _gid=GA1.3.2124796849.1586739920",
# 	        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"

# 	}
# )
response = requests.get(
	"https://www.cwb.gov.tw/V8/C/W/TemperatureTop/County_TMax_T.html",
	headers = {
	        "Accept": "*/*",
	        "Accept-Encoding":"gzip, deflate",
	        "Accept-Language":"zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3",
	        "Cookie":"V8_LANG=C; TS01c55bd7=0107dddfef4634fe7fa8bc4302721e18261cfad648bf2d6caa0a67b139fd739b30aab8ba5a; _ga=GA1.3.1353783014.1586596932; _gid=GA1.3.2124796849.1586739920",
	        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",
	        "Host": "www.cwb.gov.tw",
	        "Referer": "https://www.cwb.gov.tw/V8/C/W/County_TempTop.html",
	        "TE": "Trailers",
	        "X-Requested-With": "XMLHttpRequest",
	        "Connection": "keep-alive"

	}
)

response.encoding = "utf-8"
b1 = BeautifulSoup(response.text, "html.parser")
cities = b1.find_all("th", {"scope":"row"})
temps = b1.find_all("span", {"class":"tem-C"})

t = prettytable.PrettyTable(["地區", "氣溫"])
for i in range(len(cities)):
	t.add_row([cities[i].text, temps[i].text])
print(t)

