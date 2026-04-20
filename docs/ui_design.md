# Spécifications Graphiques et UI — Design System E-Commerce Chapellerie

Ce document définit l'identité visuelle et les règles d'interface du projet, mises à jour après la refonte design de mars 2026.

---

## 🎨 1. Charte Graphique — Page d'Accueil (Style 099.supply)

La page d'accueil utilise un design **Dark Brutalist Tech-Luxury**, inspiré du site [099.supply](https://099.supply/).

### Couleurs
| Rôle | Couleur | Valeur |
|------|---------|--------|
| Fond global | Noir pur | `#000000` |
| Fond des cards | Gris très sombre | `#111111` |
| Fond card hero | Gris sombre | `#141414` |
| Fond hover card | Gris légèrement plus clair | `#161616` |
| Texte principal | Blanc pur | `#FFFFFF` |
| Texte secondaire | Blanc atténué | `rgba(255,255,255,0.5)` |
| Texte tertiaire | Blanc très atténué | `rgba(255,255,255,0.25)` |
| Accentuation | Jaune fluo (badge/CTA) | `#D4FF00` |
| Badge carte | Blanc sur noir | `#fff / #000` |

### Typographie
- **Page d'accueil :** `JetBrains Mono` (Google Fonts) — monospace, technique, industriel
  - Tout en minuscules ou small-caps
  - Letter-spacing entre 0.5px et 2px selon le contexte
  - Mimique le design 099.supply (codes produits, labels)
- **Header global (layout.html) :** Garde le style original Topperzstore (pages produits, etc.)
- **Codes produits :** format `C 001`, `B 002`, `K 001`, `S 001` (Lettre catégorie + numéro)

---

## 🔝 2. Header — Page d'Accueil (Spécifique)

Le header de la page d'accueil **remplace visuellement** le header global du layout.

```
[ Menu ≡ ]          [ CHAPELLERIE ]          [ Cart 0 ]
```

- **Position :** Fixed, top 0, full width, fond `rgba(0,0,0,0.85)` + `backdrop-filter: blur(12px)`
- **Hauteur :** 52px
- **Font :** JetBrains Mono
- **Menu :** Overlay latéral animé (slideX -100% → 0%) couvrant tout l'écran
- **Liens menu :** ACCUEIL / CASQUETTES / BONNETS / KÉPIS / SNEAKERS

---

## 🔝 3. Header — Pages Intérieures (Layout Global)

Conservé du design original Topperzstore :
- **Top Bar :** Jaune fluo `#D4FF00`, texte promo (Achetez 3, obtenez 1 GRATUIT)
- **Structure Desktop :** Burger + liens | Logo centered italique gras | 4 icônes (loupe, cœur, compte, panier)
- **Badge panier :** Jaune fluo `#D4FF00`
- **Comportement :** Sticky avec box-shadow au scroll

---

## 🃏 4. Cards Produits — Style 099.supply

Chaque card suit cette structure :

```
┌─────────────────────────────────┐
│ C 002              Nom Produit  │  ← card-header (monospace, atténué)
│                                 │
│            🧢                   │  ← card-image (emoji ou photo PNG)
│                                 │
│ Catégorie          1 200 DZD   │  ← card-footer (prix en blanc)
└─────────────────────────────────┘
```

- **Border-radius :** 18px
- **Fond :** `#111`
- **Hover :** `scale(1.01)` + fond `#161616` + produit `translateY(-6px) scale(1.05)`
- **Badge :** Petit rectangle blanc `NEW` / `BEST` en haut à droite

### Grille
- **Desktop :** 2 colonnes, `gap: 8px`, padding global `10px`
- **Mobile :** 1 colonne

### Hero Grid (haut de page)
- 2 grandes cards côte à côte (1fr / 1.6fr)
- **Gauche :** Card intro brand (texte uniquement, sans image)
- **Droite :** Card Bestseller avec produit en grand

---

## 🔘 5. Filtres Catégorie

```
[ Show All ]  [ Casquettes (C) ]  [ Bonnets (B) ]  [ Képis (K) ]  [ Sneakers (S) ]
```

- **Style inactif :** fond `#111`, texte `rgba(255,255,255,0.6)`, border `rgba(255,255,255,0.08)`
- **Style actif / hover :** fond `#fff`, texte `#000`
- **Comportement :** Filtre les cards de la grille par `data-cat`

---

## 🦶 6. Footer — Pages Intérieures

Conservé du design original Topperzstore :
- **Section hero :** Slogan géant `"WE CARE ABOUT CAPS!"` incliné, fond `#000`, texte blanc
- **3 colonnes :** Assistance | Informations | Contact
- **Mobile :** Accordéons déroulants (+ / -)
- **Réassurance :** Icônes paiement (Visa, Mastercard, Apple Pay, Google Pay, DHL) + réseaux sociaux

---

## 📏 7. Tokens de Design

| Token | Valeur |
|-------|--------|
| `--radius-card` | 18px |
| `--gap-grid` | 8px |
| `--padding-page` | 10px |
| `--header-height` | 52px |
| `--color-bg` | #000 |
| `--color-card` | #111 |
| `--color-text` | #fff |
| `--color-accent` | #D4FF00 |
| `--font-mono` | 'JetBrains Mono', monospace |

---

## 📸 8. Images Produits

- Format : **PNG fond transparent** (détouré)
- Affichage : centré dans la card, `max-height: 240px`, `object-fit: contain`
- Effet hover : `translateY(-6px) scale(1.04)`
- Interim : emojis utilisés en attendant les vraies photos
