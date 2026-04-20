# Progression du Projet — E-Commerce Chapellerie

## Statut global
- [x] En démarrage
- [x] En développement
- [ ] Phase de test
- [ ] Terminé

---

## 📅 Dernière session — 2026-03-24 (nuit)

**Durée :** Session de refonte complète UI (Design System 099.supply)

### Ce qu'on a fait :

**Refonte visuelle de la page d'accueil**
- Remplacement du Flipbook 3D (GSAP) par un nouveau design "Dark Brutalist Tech-Luxury"
- Inspiration directe : [099.supply](https://099.supply/?ref=godly) analysé visuellement vidéo + captures
- Réécriture complète de `src/templates/index.html`

**Éléments du nouveau design implémentés :**
- 🖤 **Fond noir pur** (`#000000`) comme sur 099.supply
- 🖥️ **Header monospace fixe** : `Menu ≡ | CHAPELLERIE | Cart 0`
- 🟫 **Hero grid 2 colonnes** : carte intro brand + carte Bestseller (Snapback C 001)
- 🔘 **Filtres catégorie** : `Show All | Casquettes (C) | Bonnets (B) | Képis (K) | Sneakers (S)`
- 🃏 **Grille 6 cards produits** arrondies (border-radius 18px, fond `#111`)
- 🏷️ **Codes produit** style 099 : `C 002`, `B 001`, `K 001`, `S 001`…
- ⭐ **Badges** `NEW` / `BEST` en blanc sur fond noir sur les cards
- 🖱️ **Hover** : scale + emoji produit qui monte (translateY)
- 📋 **Menu overlay latéral** animé (translateX) avec tous les liens de navigation
- 🔤 **Typographie JetBrains Mono** (Google Fonts) — style technique/industriel

**Itérations passées (remplacées) :**
1. Version 1 — Grille produits statique classique
2. Version 2 — Flipbook 3D avec GSAP + pages qui tournent via slider
3. Version 3 — Flipbook 3D fidèle à la référence (drag & drop + animation intro GSAP)
4. ✅ **Version 4 (actuelle)** — Style 099.supply dark brutalist monospace

---

## Fonctions / Modules terminés ✅
| # | Nom | Fichier | Notes |
|---|-----|---------|-------|
| 1 | Dépendances | `requirements.txt` | Flask, SQLAlchemy, PyMySQL, Cloudinary, python-dotenv |
| 2 | Point d'entrée Flask | `src/app.py` | render_template, debug mode, host 0.0.0.0 |
| 3 | Template Layout | `src/templates/layout.html` | Header sticky + Footer style Topperzstore |
| 4 | Page Accueil | `src/templates/index.html` | Design 099.supply — dark cards, monospace, filtres |

---

## En cours 🔄
- **Phase :** Design de la page d'accueil terminé (visuel statique)
- **Prochains fichiers :** Pages catégories, détail produit
- **Point d'arrêt :** Serveur Flask arrêté à 03h35 – design validé visuellement par l'utilisateur

---

## Session du 2026-03-23 — Accomplissements ✅
- ✅ Templates Jinja2 créés et fonctionnels
- ✅ Header style Topperzstore (top bar jaune, sticky, icônes)
- ✅ Footer style Topperzstore (slogan, 3 colonnes, accordéons mobile)
- ✅ JavaScript pour interactions (scroll, accordéons)
- ✅ Test mobile sur (IP: 10.209.151.173:5000)

---

## Prochaine étape ⏭️
- [ ] Créer les pages catégories (`/casquettes`, `/bonnets`, `/kepis`, `/sneakers`) avec le même style 099
- [ ] Remplacer les emojis par de vraies photos de produits (PNG fond transparent)
- [ ] Connecter les boutons "Voir la boutique" aux routes Flask
- [ ] Configurer la base de données MySQL (modèles SQLAlchemy)
- [ ] Rendre le panier fonctionnel

---

## Backlog (fonctionnalités prévues)
- [ ] Page liste produits avec grille (style 099 – même design)
- [ ] Page détail produit
- [ ] Panier fonctionnel
- [ ] Commande simple
- [ ] Filtrage avancé (prix, taille, couleur)
- [ ] Compte utilisateur
- [ ] Paiement en ligne

---

## Notes techniques 📝
- Devise : DZD (Dinar Algérien)
- Images produits : doivent être détourées (PNG fond transparent)
- Guide des tailles : indispensable pour chapellerie
- Responsive : grille 2 colonnes desktop → 1 colonne mobile
- Serveur : `python src/app.py` — accessible sur `10.209.151.173:5000`
