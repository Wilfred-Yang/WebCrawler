import csv
import prettytable
import json
import os
import requests
word = input("關鍵字: ")
response = requests.get(
	"https://ecshweb.pchome.com.tw/search/v3.3/all/results",
	headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",
	# "Accept-Encoding":"gzip, deflate, br",
	"Cookie": "U=94a5a7b22b03978000ded51756d85f5a9af079c8; ECC=cfc016620735655e8d7f5b3b98889e8f9ce48b30.1586586524; ECWEBSESS=40e2a55831.51bf0136d1220fca1da150abb0b9df7cd4e8e525.1586586524; _gcl_au=1.1.662433951.1586586528; _fbp=fb.2.1586586528263.712100291; _ga=GA1.3.1693574706.1586586528; _gid=GA1.3.1600783732.1586586528; venguid=d7e69841-4a31-4fd0-9f94-22188096b502.wg1-xvxf20200411; vensession=9f062494-f23e-471d-a7d3-21dfa9e920c2.wg1-xvxf20200411.se",
	"Accept-Language":"zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3",

	},
	params = {"q":str(word),"page":"1","sort":"sale/dc"},
)

t = prettytable.PrettyTable(["名稱", "價錢"], encoding = "utf8")
print(type(response.text))
json_to_text = json.loads(response.text)
for i in json_to_text["prods"]:
	t.add_row([i["name"], i['price']])
t.align["名稱"] = "l"

while True:
	print(t)
	try:
		page = int(input("輸入頁碼: "))
	except:
		print("輸入的不是數字")
		break
	response = requests.get(
		"https://ecshweb.pchome.com.tw/search/v3.3/all/results",
		headers = {
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",
		"Cookie": "U=94a5a7b22b03978000ded51756d85f5a9af079c8; ECC=cfc016620735655e8d7f5b3b98889e8f9ce48b30.1586586524; ECWEBSESS=40e2a55831.51bf0136d1220fca1da150abb0b9df7cd4e8e525.1586586524; _gcl_au=1.1.662433951.1586586528; _fbp=fb.2.1586586528263.712100291; _ga=GA1.3.1693574706.1586586528; _gid=GA1.3.1600783732.1586586528; venguid=d7e69841-4a31-4fd0-9f94-22188096b502.wg1-xvxf20200411; vensession=9f062494-f23e-471d-a7d3-21dfa9e920c2.wg1-xvxf20200411.se",
		"Accept-Language":"zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3"
		},
		params = {"q":str(word), "page":str(page), "sort":"sale/dc"},
	)

	t = prettytable.PrettyTable(["名稱", "價錢"], encoding = "utf8")
	json_to_text = json.loads(response.text)
	for i in json_to_text["prods"]:
	    t.add_row([i["name"], i['price']])
	t.align["名稱"] = "l"
	os.system("cls")