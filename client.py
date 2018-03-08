import requests

URL = "vcm-3577.vm.duke.edu"


name = requests.get(URL + "/name")
print(name.json())


hello = requests.get(URL + "/hello/Suyash")
print(hello.json())


data = {
    "a": [2, 4],
    "b": [5, 6]
}
p = requests.post(URL + "/distance", json=data)
print(p.json())

