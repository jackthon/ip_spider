import pandas as pd
import requests
import time

baseurl = 'http://ip.taobao.com/service/getIpInfo.php?ip='
df = pd.read_csv('survey_26991-ip.txt', sep='\t')[411:]

def get(url):
	try:
		data = requests.get(url).json()['data']
	except:
		data = get(url)
	return data

with open('1.txt', 'a', encoding='utf-8') as ff:
	for index,row in df.iterrows():
		url = baseurl + row['ip']
		data = get(url)
		time.sleep(1)
		try:
			print(str(row['id']) + '\t' + row['ip'] + '\t' + data['region'] + '\t' + data['city'] + '\n')
			ff.write(str(row['id']) + '\t' + row['ip'] + '\t' + data['region'] + '\t' + data['city'] + '\n')
		except:
			data = get(url)
			time.sleep(2)
			print(row)
			ff.write(str(row['id']) + '\t' + row['ip'] + '\t' + data['region'] + '\t' + data['city'] + '\n')