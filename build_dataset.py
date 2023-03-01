########################## Libraries ################################################
import requests
import urllib.parse
import csv
########################## Global_variables #########################################
site = "MLA"
search = "tv 4k"
search = urllib.parse.quote(search)
api_url = f"https://api.mercadolibre.com/sites/{site}/search?q={search}"
########################## Request ##################################################
response = requests.get(api_url)
json = response.json()
########################## Items_sortation ##########################################
items_list = []
for resultado in json["results"]:
    aux = 0
    while resultado["attributes"][aux]["id"] != "BRAND":
        aux += 1
    items_list.append([resultado["id"], resultado["title"], resultado["price"], resultado["domain_id"], resultado["attributes"][aux]["value_name"]])
########################## Format_and_exportation ###################################
with open("dataset.csv","w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(items_list)
########################## End of script ############################################
