import requests

data = requests.get('https://api.rootnet.in/covid19-in/stats/atest').json()
length = len(data['data']['regional'])


for i in range(length):

	print("|----------------------------------------|")
	print("\t", data['data']['regional'][i]['loc'])


	print("|----------------------------------------|")
	print("Confirmed Indian Cases ||\t" ,data['data']['regional'][i]['confirmedCasesIndian'])

	print("|----------------------------------------|")
	print("Confirmed Foreigner Cases ||\t" ,data['data']['regional'][i]['confirmedCasesForeign'])


	print("|----------------------------------------|")
	print("Recovered Cases ||\t" ,data['data']['regional'][i]['discharged'])


	print("|----------------------------------------|")
	print("TOTAL DAETHS ||\t" ,data['data']['regional'][i]['deaths'])

	
	