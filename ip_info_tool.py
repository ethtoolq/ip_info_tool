import requests
import re

def validate_ip(ip_address):
    """проверяет корректность ip"""
    ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    
    if re.match(ipv4_pattern, ip_address):
        parts = ip_address.split('.')
        return all(0 <= int(part) <= 255 for part in parts)
    return False

def get_ip_info(ip_address):
    """получает информацию об ip через ipinfo.io"""
    if not validate_ip(ip_address):
        print(f"❌ некорректный ip\n")
        return
    
    try:
        url = f"https://ipinfo.io/{ip_address}/json"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        data = response.json()
        
        if 'error' in data:
            print(f"❌ ошибка: {data['error']['message']}\n")
            return
        
        print(f"\n{'='*40}")
        print(f"IP: {ip_address}")
        print(f"{'='*40}")
        print(f"Страна:    {data.get('country', 'N/A')}")
        print(f"Город:     {data.get('city', 'N/A')}")
        print(f"Регион:    {data.get('region', 'N/A')}")
        print(f"Провайдер: {data.get('org', 'N/A')}")
        print(f"Координаты: {data.get('loc', 'N/A')}")
        print(f"Часовой пояс: {data.get('timezone', 'N/A')}")
        print(f"{'='*40}\n")
        
    except requests.exceptions.Timeout:
        print("❌ таймаут\n")
    except requests.exceptions.RequestException as e:
        print(f"❌ ошибка: {e}\n")

def main():
    """основной цикл программы"""
    print("\n📍 IP Info Tool\n")
    
    while True:
        ip = input("введи ip (выход для выхода): ").strip()
        
        if ip.lower() in ['выход', 'exit']:
            print("👋\n")
            break
        
        if not ip:
            continue
        
        get_ip_info(ip)

if __name__ == "__main__":
    main()
