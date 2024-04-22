import requests

url = "https://tasty.p.rapidapi.com/recipes/auto-complete"

querystring = {"prefix":"chicken breast"}

headers = {
	"X-RapidAPI-Key": "0bccf89588mshcb9bb8398bc676bp1acf33jsn1a95f7f435b4",
	"X-RapidAPI-Host": "tasty.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())