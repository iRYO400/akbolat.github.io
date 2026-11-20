---
title: Pocket Armory
description: Öffne 3D-Truhen, sammle Cartoon-Waffen und füll deine Waffenkammer.
layout: landing
landing: true
landing_css: css/pocket-armory-landing.css

tagline: Loot & Shoot
kind: Spiel
icon: images/pa-icon.webp
pitch: Öffne 3D-Truhen, sammle Cartoon-Waffen und füll deine Waffenkammer.

# Store buttons. The App Store link is a placeholder until the page exists.
play_url: https://play.google.com/store/apps/details?id=com.lootonomics.dropfire&hl=de
app_store_url: "#app-store"

hero_screens:
  - {img: images/pa-screen-2.webp, alt: Eine Truhe öffnet sich auf einer 3D-Bühne}
  - {img: images/pa-screen-3.webp, alt: "Ein Gewehr feuert, mit Zahlen für kritische Treffer"}

# The chest strip: what is inside and where gold comes from (layouts/_partials/loot.html).
loot:
  title: Dreh. Zieh. Entscheide.
  lede: "Jede Truhe lässt ein Band voller Waffen durchlaufen und stoppt bei deiner. Dreh sie in 3D, gib ein paar Schüsse ab und entscheide."
  new: Neue Waffe!
  paths:
    - {icon: keep, title: Behalt sie, text: "Deine Waffenkammer zeigt jede Waffe in 3D. Lackierungen ändern ihr Aussehen, und eine Legendäre kann einen Anhänger bringen."}
    - {icon: show, title: Stell sie aus, text: "Waffen auf den Ständern der Vitrine bringen Gold, auch wenn du nicht da bist."}
    - {icon: sell, title: Verkauf sie, text: "Sofort Gold, oder gib Waffen für Aufträge der Werkstatt ab und steig auf."}
  loop_title: Gold öffnet die nächste Truhe.
  loop_text: "Ein paar Öffnungen gehen aufs Haus, eine freiwillige Werbung bringt eine bessere, und Truhen gibt es nie für echtes Geld."

# The key stack only, shown at the end of the page.
stack:
  - {name: Kotlin Multiplatform, text: "Eine Codebasis für Android und iOS: Spiellogik, Spielstände und Wirtschaft."}
  - {name: Compose Multiplatform, text: "Die ganze Oberfläche, auf beiden Plattformen geteilt."}
  - {name: Google Filament, text: "Googles physikalisch basierter Renderer zeichnet die 3D-Szene auf beiden Plattformen."}

help:
  - {title: Support, text: "Bug gefunden oder Fortschritt verloren? Schreib uns und nenn dein Handymodell.", address: whitesteel400@gmail.com}
  - {title: Datenschutz, text: "Was das Spiel erfasst, wie Werbung es nutzt und wie du deine Daten löschst.", link_text: Datenschutzerklärung, link: /pocket-armory/privacy/}
---
