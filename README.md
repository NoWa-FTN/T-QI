# T-QI (Tool for Query Investigation)

T-QI est un outil puissant pour mener des investigations sur des utilisateurs, des emails, des IPs, des numéros de téléphone et plus encore. Ce script Python permet de collecter des informations via différentes sources, notamment les réseaux sociaux, les archives web, les résultats d'articles de presse, les scans Shodan, le Dark Web, et bien d'autres.

---

## Fonctionnalités

- **Recherche sur les réseaux sociaux** : Vérifie la présence d'un utilisateur sur plusieurs plateformes comme Twitter, Instagram, Facebook, LinkedIn, GitHub.
- **Articles de presse** : Recherche des articles de presse en ligne associés à un nom ou un pseudo.
- **Recherche d'images** : Effectue une recherche d'images sur Yandex associées à un nom ou un pseudo.
- **Recherche sur le Dark Web** : Recherche d'informations sur le Dark Web via Ahmia.
- **Archives Web** : Recherche dans les archives de sites web via la Wayback Machine.
- **Informations sur une IP** : Récupère des informations géographiques sur une adresse IP.
- **Scan Shodan** : Effectue un scan de l'IP sur Shodan pour récupérer des informations sur les services exposés.
- **Analyse d'un numéro de téléphone** : Utilise PhoneInfoga pour rechercher des informations sur un numéro de téléphone.

---

## Prérequis

Avant d'exécuter ce script, vous devez installer les dépendances suivantes :

### Python 3.x

Si vous ne l'avez pas déjà installé, vous pouvez le télécharger ici : [Python.org](https://www.python.org/downloads/)

### Bibliothèques Python

Exécutez la commande suivante pour installer les bibliothèques nécessaires :

```bash
pip install requests beautifulsoup4 shodan
```

### Outils externes :

- **Sherlock** : [Sherlock GitHub](https://github.com/sherlock-project/sherlock) – Outil pour rechercher un pseudo sur diverses plateformes.
- **Holehe** : [Holehe GitHub](https://github.com/megadose/holehe) – Outil pour trouver les services associés à un email.
- **PhoneInfoga** : [PhoneInfoga GitHub](https://github.com/PhantomEiffel/PhoneInfoga) – Outil pour l'analyse des numéros de téléphone.

---

## Clé API

### Shodan API

Vous devez remplacer la clé `SHODAN_API_KEY` dans le script avec votre propre clé API de Shodan. Vous pouvez en obtenir une en vous inscrivant sur [Shodan.io](https://www.shodan.io/).

---

## Utilisation

1. Clonez le repository ou téléchargez le script Python.

   ```bash
   git clone https://github.com/votre-utilisateur/T-QI.git
   ```

2. Installez les dépendances et outils externes requis.

3. Exécutez le script avec la commande suivante :

   ```bash
   python T-QI.py
   ```

4. Entrez les informations que vous souhaitez rechercher : nom d'utilisateur, email, adresse IP, numéro de téléphone, etc.

Le script effectuera une série de recherches et affichera les résultats dans le terminal. Il générera également un rapport JSON avec les résultats détaillés.

---

## Exemple d'exécution

```bash
$ python T-QI.py
[+] Entrez le nom d'utilisateur à rechercher : truc
[+] Entrez un email (si connu, sinon laissez vide) : truc@example.com
[+] Entrez une adresse IP (si connue, sinon laissez vide) : 192.168.1.1
[+] Entrez un numéro de téléphone (si connu, sinon laissez vide) : +33612345678
[+] Entrez un site web à analyser (ex: exemple.com, sinon laissez vide) : example.com
```

Résultats dans le terminal :

```
[+] Recherche sur les réseaux sociaux
[x] Twitter: https://twitter.com/truc
[x] LinkedIn: https://www.linkedin.com/in/truc
...

[+] Articles de presse & scandales
[x] https://example.com/article-about-truc

[+] Recherche d'images associées
[x] https://yandex.com/images/search?text=truc

[+] Recherche sur le Dark Web
[x] https://ahmia.fi/search/?q=truc
...

[+] Rapport enregistré sous 'truc_report.json'
```

Un fichier `truc_report.json` sera généré contenant toutes les informations collectées.

---

## Avertissement

Ce script est destiné à des fins légales et éthiques uniquement. Utilisez-le de manière responsable et respectez les lois et réglementations locales en matière de collecte de données. Le projet ne peut être tenu responsable des usages abusifs du script.

---

## Contributions

Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet, veuillez soumettre une **Pull Request**. Assurez-vous de suivre les bonnes pratiques de codage et d'inclure des tests si nécessaire.

---

## License

Ce projet est sous licence **MIT**. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
