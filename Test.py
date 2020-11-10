import requests

resp = requests.post("http://localhost:5000/upload",
                     files={"file": open('../_static/img/fishy.jpg','rb')})
print(resp.json())