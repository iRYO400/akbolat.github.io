---
title: Pocket Armory
description: Crack open 3D chests, collect cartoon guns and fill your armory.
layout: landing
landing: true
landing_css: css/pocket-armory-landing.css

tagline: Loot & Shoot
kind: Game
icon: images/pa-icon.webp
pitch: Crack open 3D chests, collect cartoon guns and fill your armory.

# Store buttons. The App Store link is a placeholder until the page exists.
play_url: https://play.google.com/store/apps/details?id=com.lootonomics.dropfire
app_store_url: "#app-store"

hero_screens:
  - {img: images/pa-screen-2.webp, alt: A chest opening on a 3D stage}
  - {img: images/pa-screen-3.webp, alt: "A rifle firing, with critical hit numbers"}

# The chest strip: what is inside and where gold comes from (layouts/_partials/loot.html).
loot:
  title: Spin. Drop. Decide.
  lede: "Every chest spins a strip of guns and stops on yours. Turn it in 3D, fire a few shots, then make the call."
  new: New gun!
  paths:
    - {icon: keep, title: Keep it, text: "Your Armory holds every gun in 3D. Paints change its look, and a Legendary can bring a charm."}
    - {icon: show, title: Show it, text: "Guns on Showcase stands earn gold, even while you are away."}
    - {icon: sell, title: Sell it, text: "Gold right away, or hand guns in for Workshop orders and level up."}
  loop_title: Gold opens the next chest.
  loop_text: "A few opens are on the house, an optional ad gets you a better one, and chests are never sold for real money."

# The key stack only, shown at the end of the page.
stack:
  - {name: Kotlin Multiplatform, text: "One codebase for Android and iOS: game logic, saves and economy."}
  - {name: Compose Multiplatform, text: "The whole interface, shared by both platforms."}
  - {name: Google Filament, text: "Google’s physically based renderer draws the 3D scene on both platforms."}

help:
  - {title: Support, text: "Found a bug or lost progress? Write to us and mention your phone model.", address: whitesteel400@gmail.com}
  - {title: Privacy, text: "What the game collects, how ads use it and how to delete your data.", link_text: Privacy policy, link: /pocket-armory/privacy/}
---
