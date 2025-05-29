import requests

# 🔑 Sua chave da API vai aqui
API_KEY = "SUA_API_KEY_AQUI"

# Coordenadas de São Paulo - brasil
latitude = -23.5505
longitude = -46.6333

# URL da API
url = (
    f"https://api.openweathermap.org/data/2.5/weather?"
    f"lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric&lang=pt_br"
)

# Fazendo a requisição
resposta = requests.get(url)
dados = resposta.json()

# Extraindo os dados principais
temperatura = dados["main"]["temp"]
descricao_clima = dados["weather"][0]["description"]
umidade = dados["main"]["humidity"]


print(f"A temperatura é {temperatura}°C, o clima é '{descricao_clima}' e a umidade é {umidade}%.")
