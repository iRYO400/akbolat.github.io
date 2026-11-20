---
title: Pocket Armory
description: 3D sandıkları aç, çizgi film silahları topla ve Cephanelik’ini doldur.
layout: landing
landing: true
landing_css: css/pocket-armory-landing.css

tagline: Loot & Shoot
kind: Oyun
icon: images/pa-icon.webp
pitch: 3D sandıkları aç, çizgi film silahları topla ve Cephanelik’ini doldur.

# Store buttons. The App Store link is a placeholder until the page exists.
play_url: https://play.google.com/store/apps/details?id=com.lootonomics.dropfire&hl=tr
app_store_url: "#app-store"

hero_screens:
  - {img: images/pa-screen-2.webp, alt: 3D bir sahnede açılan sandık}
  - {img: images/pa-screen-3.webp, alt: "Ateş eden bir tüfek ve kritik vuruş sayıları"}

# The chest strip: what is inside and where gold comes from (layouts/_partials/loot.html).
loot:
  title: Çevir. Kazan. Seç.
  lede: "Her sandık bir silah şeridini döndürür ve seninkinde durur. 3D’de çevir, birkaç el ateş et, sonra kararını ver."
  new: Yeni silah!
  paths:
    - {icon: keep, title: Sakla, text: "Cephanelik’in her silahı 3D olarak tutar. Boyalar görünümünü değiştirir, bir Efsanevi silah da bir anahtarlıkla gelebilir."}
    - {icon: show, title: Sergile, text: "Vitrin standlarındaki silahlar sen yokken bile altın kazandırır."}
    - {icon: sell, title: Sat, text: "Hemen altın al, ya da silahları Atölye siparişlerine ver ve seviye atla."}
  loop_title: Altın sıradaki sandığı açar.
  loop_text: "Birkaç açılış bizden, isteğe bağlı bir reklam daha iyisini getirir ve sandıklar asla gerçek parayla satılmaz."

# The key stack only, shown at the end of the page.
stack:
  - {name: Kotlin Multiplatform, text: "Android ve iOS için tek kod tabanı: oyun mantığı, kayıtlar ve ekonomi."}
  - {name: Compose Multiplatform, text: "Arayüzün tamamı, iki platformda ortak."}
  - {name: Google Filament, text: "Google’ın fiziksel tabanlı render motoru 3D sahneyi iki platformda da çizer."}

help:
  - {title: Destek, text: "Hata mı buldun ya da ilerlemeni mi kaybettin? Bize yaz ve telefon modelini belirt.", address: whitesteel400@gmail.com}
  - {title: Gizlilik, text: "Oyunun neleri topladığı, reklamların bunları nasıl kullandığı ve verilerini nasıl sileceğin.", link_text: Gizlilik politikası, link: /pocket-armory/privacy/}
---
