########################## Libraries ################################################
import sys
import requests
import urllib.parse
import csv
########################## Global_variables #########################################
site = str(sys.argv[1])
try:
    search = str(sys.argv[2])
except:
    search = "tv 4k"
search = urllib.parse.quote(search)
api_url = f"https://api.mercadolibre.com/sites/{site}/search?q={search}"
########################## Request ##################################################
try:
    response = requests.get(api_url)
    json = response.json()
######################### Items_sortation ###########################################
    items_list = []
    #print(len(json["results"]))
    for resultado in json["results"]:
        if resultado["condition"] == "new":
            aux = 0
            while resultado["attributes"][aux]["id"] != "BRAND":
                aux += 1
            items_list.append([resultado["id"], resultado["title"], resultado["price"], resultado["domain_id"], resultado["attributes"][aux]["value_name"]])
########################## Format_and_exportation ###################################
    with open("dataset.csv","w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(items_list)
########################## Error_handle #############################################
except:
    print(site, "no es un sitio válido.")
########################## End_of_script ############################################
