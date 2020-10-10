#import sys
#import json
#import urllib
#import webbrowser
#import pyperclip
#if len(sys.argv) > 1 :
#	mapAddress = ''.join(sys.argv[1:])
#else :
#	mapAddress = pyperclip.paste()
#webbrowser.open('https://n.cbg.163.com/cbg/query.py?serverid=5&act=search_role'+mapAddress)
import requests
from bs4 import BeautifulSoup
import re
import pymongo

def getContent(target):
# 获取爬取网页的内容
	req = requests.get(url=target)
	rawhtml = req.text
	bf = BeautifulSoup(rawhtml,"html.parser")
	texts = bf.find_all('table',cellspacing ='0')
	#texts = bf.find_all('table','date-serverid' =='5')
	#print(texts)
	return texts

def parseContent(texts):
# 正则需要的账号信息
	pattern = re.compile('<img.*?alt="(.*?)".*?总评分.*?"val">(.*?)</span>.*?修为.*?"val">(.*?)</span>.*?修炼.*?"val">(.*?)</span>.*?装备评分.*?"val">(.*?)</span>.*?基础评分.*?"val">(.*?)</span>.*?"n-highlights".*?<i>(.*?)</td>.*?<td>(.*?)</td>.*?<td>.*?<span>(.*?)</span>.*?mapPriceColor[(](.*?)[)][)]</script>',re.S)
	items = re.findall(pattern,str(texts))
	#items = str(re.findall(pattern,str(texts))).replace('</i>','').replace('<i>','、').replace('\\n','')
	return items
	#print(items)

def saveContent(texts):
	client = pymongo.MongoClient(host='localhost')
	db = client.cbg_homework
	collection = db.zijinzhidian
	valuelist = []
	for text in texts :
		value = {
			'角色昵称':text[0],
			'总评分':text[1],
			'修为':text[2],
			'修炼':text[3],
			'装备评分':text[4],
			'基础评分':text[5],
			'亮点':str(text[6]).replace('</i>','').replace('<i>','、').replace('\n',''),
			'等级':text[7],
			'衣品值':text[8],
			'价格':text[9]
		}
		valuelist.append(value)
	result = collection.insert_many(valuelist)
	#print(valuelist)


def main(page):
	if page == 1 :
		page = ''
	else :
		page = 'page='+str(page)
	target = 'https://n.cbg.163.com/cbg/query.py?serverid=5&'+page+'&order=total_score+DESC&act=search_role'
	texts = getContent(target)
	texts = parseContent(texts)
	saveContent(texts)


if __name__ == '__main__':
	for i in range(10):
		main(i)
	
	
	
	
	

