import http.client

def readData(champ):
    conn = http.client.HTTPSConnection("ddragon.leagueoflegends.com")
    payload = ''
    headers = {}
    conn.request("GET", f"/cdn/11.23.1/data/en_US/champion/{champ}.json", payload, headers)
    res = conn.getresponse()
    data = res.read()
    with open("stats.json", "w") as f:
        f.write(data.decode("utf-8"))
    f.close()