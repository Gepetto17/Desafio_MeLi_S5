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
offset = 0
while True:
    try:
        api_url = f"https://api.mercadolibre.com/sites/{site}/search?q={search}&offset={offset}"
########################## Request ##################################################
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
        with open("dataset.csv","a", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(items_list)
        offset += 50
########################## Error_handle #############################################
    except:
        print(f"Si se produjo un archivo de salida, se alcanzó el límite público de peticiones de la API. Si no, {site} no es un sitio válido.")
        break
########################## End_of_script ############################################
