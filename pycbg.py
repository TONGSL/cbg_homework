import sys
import json
import urllib
import webbrowser
import pyperclip
if len(sys.argv) > 1 :
	mapAddress = ''.join(sys.argv[1:])
else :
	mapAddress = pyperclip.paste()
#webbrowser.open('https://n.cbg.163.com/cbg/query.py?serverid=5&act=search_role'+mapAddress)
import requests

if __name__ == '__main__':
	target = 'https://n.cbg.163.com/cbg/query.py?serverid=5&order=total_score+DESC&act=search_role'
	req = requests.get(url=target)
	print(req.text)