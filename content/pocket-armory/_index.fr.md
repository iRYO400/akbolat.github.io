---
title: Pocket Armory
description: Ouvre des coffres en 3D, collectionne des armes de dessin animé et remplis ton Arsenal.
layout: landing
landing: true
landing_css: css/pocket-armory-landing.css

tagline: Loot & Shoot
kind: Jeu
icon: images/pa-icon.webp
pitch: Ouvre des coffres en 3D, collectionne des armes de dessin animé et remplis ton Arsenal.

# Store buttons. The App Store link is a placeholder until the page exists.
play_url: https://play.google.com/store/apps/details?id=com.lootonomics.dropfire&hl=fr
app_store_url: "#app-store"

hero_screens:
  - {img: images/pa-screen-2.webp, alt: Un coffre qui s’ouvre sur une scène 3D}
  - {img: images/pa-screen-3.webp, alt: "Un fusil qui tire, avec des chiffres de coup critique"}

# The chest strip: what is inside and where gold comes from (layouts/_partials/loot.html).
loot:
  title: Tourne. Pioche. Choisis.
  lede: "Chaque coffre fait défiler une bande d’armes et s’arrête sur la tienne. Tourne-la en 3D, tire quelques coups, puis tranche."
  new: Nouvelle arme !
  paths:
    - {icon: keep, title: Garde-la, text: "Ton Arsenal garde chaque arme en 3D. Les peintures changent son look, et une Légendaire peut apporter une breloque."}
    - {icon: show, title: Expose-la, text: "Les armes sur les socles de la Vitrine rapportent de l’or, même quand tu n’es pas là."}
    - {icon: sell, title: Vends-la, text: "De l’or tout de suite, ou remets des armes pour les commandes de l’Atelier et monte de niveau."}
  loop_title: L’or ouvre le coffre suivant.
  loop_text: "Quelques ouvertures sont offertes, une pub facultative t’en donne une meilleure, et les coffres ne sont jamais vendus contre de l’argent réel."

# The key stack only, shown at the end of the page.
stack:
  - {name: Kotlin Multiplatform, text: "Une seule base de code pour Android et iOS : logique de jeu, sauvegardes et économie."}
  - {name: Compose Multiplatform, text: "Toute l’interface, partagée par les deux plateformes."}
  - {name: Google Filament, text: "Le moteur de rendu physique de Google dessine la scène 3D sur les deux plateformes."}

help:
  - {title: Assistance, text: "Un bug ou une progression perdue ? Écris-nous en indiquant le modèle de ton téléphone.", address: whitesteel400@gmail.com}
  - {title: Confidentialité, text: "Ce que le jeu collecte, comment les pubs l’utilisent et comment supprimer tes données.", link_text: Politique de confidentialité, link: /pocket-armory/privacy/}
---
