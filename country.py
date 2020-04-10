import http.client

conn = http.client.HTTPSConnection("covid-19-data.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "c292695aa2msh54c80405779f4a8p1695ddjsn47c37deef73b"
    }
country=input()
conn.request("GET", "/country?format=undefined&name="+country, headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))