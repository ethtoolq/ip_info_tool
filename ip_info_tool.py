import requests

# запрашиваем IP у пользователя
ip_address = input("Введите IP-адрес: ")

# делаем запрос к ipinfo API
url = f"https://ipinfo.io/{ip_address}/json"
response = requests.get(url)

# если запрос успешен
if response.status_code == 200:
    data = response.json()  # получаем данные в формате json
    # выводим информацию
    print(f"IP: {data.get('ip', 'Неизвестно')}")
    print(f"Страна: {data.get('country', 'Неизвестно')}")
    print(f"Город: {data.get('city', 'Неизвестно')}")
    print(f"Провайдер: {data.get('org', 'Неизвестно')}")
else:
    print("Не удалось получить информацию по этому IP.")
