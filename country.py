import http.client
import json
conn = http.client.HTTPSConnection("covid-193.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "c292695aa2msh54c80405779f4a8p1695ddjsn47c37deef73b"
    }
country = input()
conn.request("GET", "/statistics?country="+country, headers=headers)

res = conn.getresponse()
data = res.read()
content = json.loads(data)['response'][0]
print(str(content['country'])+'\n'+'cases:'+str(content['cases'])+'\n'+'deaths:'+str(content['deaths'])+'\n'+'tests:'+str(content['tests'])+'\n'+'time:'+str(content['day']))