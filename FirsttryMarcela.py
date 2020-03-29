import os
import pandas 
import requests as marcela
import json
import matplotlib.pyplot as plt

# region configvalues

# endregion

#region request
def geturl();
  baseurl = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/
  # latest_stat_by_country.php?country=italy"
payload = {}
headers = {
  'x-rapidapi-host': 'coronavirus-monitor.p.rapidapi.com',
  'x-rapidapi-key': 'fb3d8d4403mshcb121428bd26369p10aca0jsn773141b4e38b'
}
response = marcela.request("GET", url, headers=headers, data = payload)
#endregion




## aux=response.text.replace(",","")
omarjson= json.loads(response.text)

#df=pandas.DataFrame(omarjson['total_deaths'])
# e=omarjson.get('total_deaths')
t=omarjson['latest_stat_by_country']
for y in t:
  info=y['total_deaths']
for key,value in omarjson.items():
  print(key,value)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = ['C', 'C++', 'Java', 'Python', 'Italy']
info=info.replace(",","")
students = [23,17,35,29,int(info)]
ax.bar(langs,students)
plt.show()