import requests

url = "https://api.nal.usda.gov/fdc/v1/foods/search"
api_key = "YOUR-API"

search_term = input("\nDigite o nome do alimento que você deseja pesquisar: ")

params = {
   "api_key": api_key,
   "query": search_term,
   "pageSize": 10,
   "dataType": ["Branded", "Survey (FNDDS)"]
}

response = requests.get(url, params=params)

if response.status_code == 200:
   data = response.json()
   if data["totalHits"] == 0:
       print("Nenhum resultado encontrado para a pesquisa: ", search_term)
   else:
        for food in data["foods"]:
           print(food["description"])
           if "servingSize" in food and "servingSizeUnit" in food:
               print("Tamanho da porção:", food["servingSize"], food["servingSizeUnit"])
           print("Nutrientes:")
           for nutrient in food["foodNutrients"]:
               print(nutrient["nutrientName"], nutrient["value"], nutrient["unitName"])
           print("--------")
else:
   print("Erro na solicitação: ", response.status_code)
