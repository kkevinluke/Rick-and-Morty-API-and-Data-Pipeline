import requests
import pandas as pd

url = "https://rickandmortyapi.com/api/character"

rnm = pd.DataFrame()

def main_response(url, x):
    response = requests.get(url+f"?page{x}")
    return response.json()

def page_info(response):
    return response["info"]["pages"]

def parse_json(response):
    charlist = []
    for item in response["results"]:
        char = {
            "id" : (item["id"]),
            "name" : (item["name"]),
            "status" : (item["status"]),
            "species" : (item["species"]),
            "type_" : (item["type"]),
            "gender" : (item["gender"]),
            "origin" : (item["origin"]["name"]),
            "location" : (item["location"]["name"]),
            "appearances" : (len(item["episode"])),
            "image" : (item["image"])
        }
        charlist.append(char)
    return charlist

main_list = []
data = main_response(url,1)
for x in range(1, page_info(data)+1):
    main_list.extend(parse_json(main_response(url,x)))

rnm = pd.DataFrame(main_list)
print(len(main_list))

rnm.to_csv("D:\My_Projects\Rick and Morty API and Pipeline\Rick_and_Morty.csv", index=False)

