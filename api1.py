import requests
import pprint
api_key='54e9761a8280768330886ca60de50064'
movie_id=500
api_version=3
query="Endgame"
api_url=f"https://api.themoviedb.org/{api_version}"
endpoint_path=f"/movie/{movie_id}"
endpoint=f"{api_url}{endpoint_path}?api_key={api_key}&query={query}"
response=requests.get(endpoint)
print(response.status_code)
pprint.pprint(response.json())
data = response.json()
f=data["genres"]
g_id=[]
g_full=[]
for g in f:
    g_id.append(g["id"])
    g_full.append(g)
for k  in range(len(g_id)):
    print(g_id[k],g_full[k])
