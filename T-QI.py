import requests
import json
import subprocess
import shodan
import os
import shutil
from bs4 import BeautifulSoup

SHODAN_API_KEY = 'nkGd8uVE4oryfUVvioprswdKGmA5InzZ'

GOOGLE_NEWS_URL = "https://www.google.com/search?q={}&tbm=nws"
YANDEX_IMAGE_SEARCH = "https://yandex.com/images/search?text={}"
WAYBACK_MACHINE = "http://web.archive.org/cdx/search/cdx?url={}&output=json"
DARK_WEB_SEARCH_URL = "https://ahmia.fi/search/?q={}"

SOCIAL_MEDIA = {
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "Facebook": "https://www.facebook.com/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "GitHub": "https://github.com/{}",
}

def print_section(title):
    print("\n" + "=" * 60)
    print(f"[+] {title}")
    print("=" * 60)

def check_social_media(username):
    results = {}
    for platform, url in SOCIAL_MEDIA.items():
        full_url = url.format(username)
        try:
            response = requests.get(full_url, timeout=5)
            if response.status_code == 200:
                results[platform] = full_url
        except requests.RequestException:
            pass
    return results

def google_news_search(name):
    url = GOOGLE_NEWS_URL.format(name.replace(" ", "+"))
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code != 200:
            return ["[-] Aucune info trouvée"]

        soup = BeautifulSoup(response.text, "html.parser")
        articles = []
        
        for link in soup.find_all("a", href=True):
            if "/url?q=" in link["href"]:
                article_url = link["href"].split("/url?q=")[1].split("&")[0]
                articles.append(article_url)

        return articles if articles else ["[-] Aucune info trouvée"]
    
    except requests.RequestException:
        return ["[x] Erreur lors de la recherche"]

def image_search(username):
    return YANDEX_IMAGE_SEARCH.format(username)

def dark_web_search(query):
    return DARK_WEB_SEARCH_URL.format(query)

def wayback_search(domain):
    url = WAYBACK_MACHINE.format(domain)
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200 or not response.json():
            return ["[-] Aucune archive trouvée"]
        
        archives = response.json()[1:]
        return [f"https://web.archive.org/web/{entry[1]}/{entry[2]}" for entry in archives]
    
    except requests.RequestException:
        return ["[x] Erreur lors de la recherche"]

def get_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}"
    try:
        response = requests.get(url, timeout=5).json()
        if response.get("status") == "fail":
            return "[-] IP invalide ou inconnue."

        return {
            "Pays": response.get("country"),
            "Région": response.get("regionName"),
            "Ville": response.get("city"),
            "Fournisseur": response.get("isp"),
            "Latitude": response.get("lat"),
            "Longitude": response.get("lon"),
            "Google Maps": f"https://www.google.com/maps?q={response.get('lat')},{response.get('lon')}"
        }
    
    except requests.RequestException:
        return "[x] Erreur lors de la recherche d’IP"

def shodan_scan(ip):
    api = shodan.Shodan(SHODAN_API_KEY)
    try:
        result = api.host(ip)
        return result
    except shodan.APIError as e:
        return f"[x] Erreur Shodan: {str(e)}"

def phone_lookup(phone):
    output_file = f"{phone}_phoneinfoga.txt"
    
    if not shutil.which("phoneinfoga"):
        return "[x] PhoneInfoga n'est pas installé"

    try:
        with open(output_file, "w") as f:
            subprocess.run(["phoneinfoga", "scan", "-n", phone], stdout=f, timeout=10)
        return output_file if os.path.exists(output_file) else "[-] Aucune donnée trouvée"
    
    except subprocess.TimeoutExpired:
        return "[x] Analyse du numéro trop longue"

def main():
    username = input("[+] Entrez le nom d'utilisateur à rechercher : ").strip()
    email = input("[+] Entrez un email (si connu, sinon laissez vide) : ").strip()
    ip = input("[+] Entrez une adresse IP (si connue, sinon laissez vide) : ").strip()
    phone = input("[+] Entrez un numéro de téléphone (si connu, sinon laissez vide) : ").strip()
    domain = input("[+] Entrez un site web à analyser (ex: exemple.com, sinon laissez vide) : ").strip()

    report = {"username": username}

    print_section("Recherche sur les réseaux sociaux")
    social_results = check_social_media(username)
    for platform, link in social_results.items():
        print(f"[+] {platform}: {link}")
    report["social_profiles"] = social_results

    print_section("Articles de presse & scandales")
    news_results = google_news_search(username)
    for article in news_results:
        print(f"[+] {article}")
    report["news_articles"] = news_results

    print_section("Recherche d’images associées")
    print(f"[+] {image_search(username)}")
    report["image_search"] = image_search(username)

    print_section("Recherche sur le Dark Web")
    print(f"[+] {dark_web_search(username)}")
    report["dark_web_search"] = dark_web_search(username)

    if domain:
        print_section("Archives du site web")
        archive_results = wayback_search(domain)
        for archive in archive_results:
            print(f"[+] {archive}")
        report["archives"] = archive_results

    if ip:
        print_section("Informations sur l'IP")
        ip_info = get_ip_info(ip)
        if isinstance(ip_info, dict):
            for key, value in ip_info.items():
                print(f"[+] {key}: {value}")
        else:
            print(ip_info)
        report["ip_info"] = ip_info

    if phone:
        print_section("Analyse du numéro de téléphone")
        phone_file = phone_lookup(phone)
        print(f"[+] Résultats enregistrés dans {phone_file}")
        report["phone_info"] = phone_file

    report_filename = f"{username}_report.json"
    with open(report_filename, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)

    print(f"\n[+] Rapport enregistré sous '{report_filename}'")

if __name__ == "__main__":
    main()
