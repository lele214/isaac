# Structure du projet
```bash
isaac/
│
├── data/
│   ├── tboi_all_items.csv.csv          # Données brutes - tous les items
│   ├── tboi_fandom_actifs.csv.csv      # Données brutes - items actifs
│   ├── tboi_fandom_passifs.csv.csv     # Données brutes - items passifs
│   ├── tboi_merged.csv                 # CSV fusionné (généré)
│   └── tboi_items.db                   # Base de données SQLite (généré)
│
├── static/
│   ├── images/                         # Images des items et icônes
│   └── styles.css                      # Feuille de style CSS
│
├── templates/
│   └── index.html                      # Template HTML principal
│
├── install.ps1                         # Script d'installation Windows PowerShell
├── main.py                             # Application Flask principale
│
├── requirements.txt                    # Dépendances Python
└── README.md                           # Documentation du projet
```

# Cloner le repository
```bash
git clone https://github.com/lele214/isaac
cd isaac
```

# Installer et configurer l'environnement
```bash
.\install.ps1
```
