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
	items = str(re.findall(pattern,str(texts))).replace('</i>','').replace('<i>','、').replace('\\n','')
	print(items)

def main(page):
	if page == 1 :
		page = ''
	else :
		page = 'page='+str(page)
	target = 'https://n.cbg.163.com/cbg/query.py?serverid=5&'+page+'&order=total_score+DESC&act=search_role'
	texts = getContent(target)
	parseContent(texts)


if __name__ == '__main__':
	for i in range(1):
		main(i)
	
	
	
	
	

