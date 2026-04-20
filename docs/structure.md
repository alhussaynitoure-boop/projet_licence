# Structure et Spécifications du Projet E-Commerce

## 1. Informations Générales
- **Catégories de Produits (Chapellerie) :** Snibak (snapback), Kipi (képis/casquettes classiques/chips), Bonner (bonnets)
- **Devise :** Dinar Algérien (DZD)
- **Fonctionnalités Clés de Recherche :** Filtrage par Prix, Taille et Couleur

## 2. Stack Technique Détaillée

### Backend / Serveur : Flask (Python)
- Framework léger et flexible
- Jinja2 intégré pour le templating
- SQLAlchemy pour l'ORM MySQL
- Flask-Login pour gestion sessions utilisateurs

### Frontend / Templating : Jinja2
- Génération HTML/CSS dynamique côté serveur
- Pas de framework JS frontend (React/Vue) — pure HTML/CSS avec Jinja2
- CSS vanilla ou minimal (pas de Bootstrap lourd)

### Base de Données : MySQL
- Stockage produits, utilisateurs, commandes
- Relations : Catégories, Produits, Variantes (taille/couleur), Utilisateurs, Commandes

### Gestion des Images / Médias : Cloudinary
- Hébergement cloud des photos produits
- Transformation images (redimensionnement, optimisation)
- CDN pour livraison rapide

### Hébergement cible : Render
- Déploiement gratuit pour Flask
- Variables d'environnement pour config
- Base de données MySQL externe (ex: PlanetScale ou Railway)

## 3. Architecture des Fichiers Complète
```
site-ecommerce/
├── CLAUDE.md                  (Architecture, stack, commandes du projet)
├── docs/
│   ├── structure.md           (Décisions de design et d'architecture)
│   └── progression.md         (Suivi de l'avancement de session en session)
├── requirements.txt           (Dépendances Python)
├── src/                       (Code source de l'application Flask)
│   ├── app.py                 (Point d'entrée Flask)
│   ├── config.py              (Configuration DB, Cloudinary, secrets)
│   ├── models/
│   │   ├── __init__.py
│   │   ├── produit.py         (Modèle Produit, Catégorie)
│   │   ├── utilisateur.py     (Modèle User)
│   │   └── commande.py        (Modèle Commande, Panier)
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py            (Connexion, inscription)
│   │   ├── boutique.py        (Liste produits, filtres)
│   │   ├── produit.py         (Détail produit)
│   │   └── panier.py          (Gestion panier, checkout)
│   ├── static/
│   │   ├── css/
│   │   │   ├── main.css       (Styles globaux)
│   │   │   ├── header.css     (Styles header/footer)
│   │   │   └── produits.css   (Styles grille produits)
│   │   ├── js/
│   │   │   ├── filtres.js     (Logique filtres latéraux)
│   │   │   └── panier.js      (AJAX ajout panier)
│   │   └── images/            (Assets statiques)
│   └── templates/
│       ├── base.html          (Template parent)
│       ├── index.html         (Page accueil)
│       ├── boutique.html      (Grille produits + filtres)
│       ├── produit_detail.html (Page détail)
│       ├── panier.html        (Panier)
│       ├── login.html         (Connexion)
│       └── register.html      (Inscription)
```

## 4. Ligne Directrice du Design Frontend (Inspiration : Topperzstore.fr)
Le design global du site sera **moderne, épuré et très orienté sur le produit**. Il utilisera un fort contraste (principalement noir et blanc, avec des touches de couleurs vives comme ocre/jaune fluo) pour diriger l'attention de l'utilisateur vers les articles et les actions d'achat.

### 4.1 La Page Principale (Navigation et Grille Produits)

#### En-tête (Header)
- **Logo :** Centré, écrit en lettres noires grasses légèrement inclinées
- **Menu & Icônes :** À gauche, menu de navigation "burger" classique. À droite, icônes minimalistes : Recherche, Liste d'envies (cœur), Compte client, Panier
- **Bannière promotionnelle :** Juste en dessous du header, fond marquant/contrasté avec offres en cours

#### Filtres et Tri
- **Bouton "FILTRE" :** Ouvre panneau latéral pour affiner (prix, taille, marque, couleur)
- **Menu déroulant :** À droite pour trier (Prix croissant/décroissant, Pertinence)

#### Grille de Produits (Mise en page épurée)
- Grille propre sur fond blanc neutre — fait ressortir les casquettes
- **Carte produit :**
  - Photo haute qualité **détourée** (transparent background)
  - Nom modèle en **majuscules grasses** sous l'image
  - Badge "NOUVEAU" si applicable
  - Prix en **DZD** clairement visible

#### Ligne Esthétique Globale
- Typographie sans-serif moderne, très lisible
- Dominance de majuscules = effet "streetwear" net

### 4.2 La Page de Détail du Produit (PDP)
Objectif : conversion maximale avec réassurance.

#### Galerie Médias (Gauche/Central)
- Image principale = moitié de l'écran
- Miniatures cliquables : face, profil, dos, texture, étiquette, vue intérieure

#### Tunnel d'Achat (Droite)
- **CTA "AJOUTER AU PANIER" :** Bouton imposant, fond noir total, lettres blanches
- **Sélection quantité :** +/- avec nombre
- **Guide des tailles :** Bouton très visible (indispensable chapellerie)

#### Réassurance
- Mini-blocs avantages : "Livraison rapide", "Paiement sécurisé"
- Logos paiement (Visa, Mastercard) visibles mais discrets
- Programme fidélité si applicable

#### Description & Preuve Sociale
- Descriptif technique concis (couronne rigide/souple, broderie flat/3D)
- Widgets "Avis Clients" vérifiés en fin de page

### 4.3 Le Footer (Pied de page)
Design cassant = alerte visuelle fin de visite.

- **Zone Noire :** Fond passe à **noir total** (dark mode brutal)
- **Slogan :** Texte immersif oblique (ex: "WE CARE ABOUT CAPS!")
- **Trois blocs nets :**
  - Assistance (FAQ, Livraison, Retours)
  - Légal (CGV, Mentions légales)
  - Contact (Email, RS)
- **Réseaux sociaux :** Instagram, TikTok de la marque

## 5. Schéma de Base de Données (Proposé)

### Tables principales
```sql
-- Catégories (Snapback, Képi, Bonnet)
categorie(id, nom, slug, description)

-- Produits
produit(id, nom, description, prix, categorie_id, image_principale,
        est_nouveau, date_ajout, marque)

-- Variantes (tailles/couleurs)
variante(id, produit_id, taille, couleur, stock, image_variante)

-- Utilisateurs
utilisateur(id, email, mot_de_passe_hash, nom, prenom, telephone,
            adresse, est_admin, date_inscription)

-- Panier (session ou connecté)
panier(id, utilisateur_id, session_id, date_creation)
panier_item(id, panier_id, variante_id, quantite)

-- Commandes
commande(id, utilisateur_id, statut, total, date_commande,
         adresse_livraison, telephone_contact)
commande_item(id, commande_id, variante_id, quantite, prix_unitaire)
```

## 6. Fonctionnalités Prioritaires

### MVP (Minimum Viable Product)
1. Page liste produits avec grille
2. Filtres par catégorie
3. Page détail produit
4. Panier fonctionnel
5. Commande simple (sans paiement en ligne pour commencer)

### V2 (Après MVP)
1. Filtrage avancé (prix, taille, couleur)
2. Tri (prix, pertinence, nouveauté)
3. Compte utilisateur complet
4. Paiement en ligne (CIB, BaridiMob)
5. Panel admin basique

## 7. Contraintes Techniques

### Performance
- Images optimisées via Cloudinary
- Pas de JS lourd (vanilla uniquement)
- CSS minimal, pas de framework CSS lourd

### Sécurité
- Protection CSRF Flask
- Mots de passe hashés (bcrypt)
- Validations formulaires côté serveur
- Pas de stockage données sensibles en clair

### SEO
- URLs propres (/boutique/snapback/nom-produit)
- Meta tags dynamiques
- Sitemap XML
