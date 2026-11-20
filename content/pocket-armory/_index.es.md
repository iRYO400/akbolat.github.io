---
title: Pocket Armory
description: Abre cofres en 3D, colecciona armas de dibujos animados y llena tu Armería.
layout: landing
landing: true
landing_css: css/pocket-armory-landing.css

tagline: Loot & Shoot
kind: Juego
icon: images/pa-icon.webp
pitch: Abre cofres en 3D, colecciona armas de dibujos animados y llena tu Armería.

# Store buttons. The App Store link is a placeholder until the page exists.
play_url: https://play.google.com/store/apps/details?id=com.lootonomics.dropfire&hl=es
app_store_url: "#app-store"

hero_screens:
  - {img: images/pa-screen-2.webp, alt: Un cofre que se abre en un escenario 3D}
  - {img: images/pa-screen-3.webp, alt: "Un rifle disparando, con números de golpe crítico"}

# The chest strip: what is inside and where gold comes from (layouts/_partials/loot.html).
loot:
  title: Gira. Descubre. Decide.
  lede: "Cada cofre hace girar una tira de armas y se detiene en la tuya. Gírala en 3D, dispara unas cuantas veces y decide."
  new: ¡Arma nueva!
  paths:
    - {icon: keep, title: Quédatela, text: "Tu Armería guarda todas tus armas en 3D. Las pinturas cambian su aspecto, y una Legendaria puede traer un llavero."}
    - {icon: show, title: Exhíbela, text: "Las armas en las estanterías de la Vitrina ganan oro, incluso cuando no estás."}
    - {icon: sell, title: Véndela, text: "Oro al instante, o entrega armas para pedidos del Taller y sube de nivel."}
  loop_title: El oro abre el siguiente cofre.
  loop_text: "Algunas aperturas son gratis, un anuncio opcional te da un cofre mejor, y los cofres nunca se venden por dinero real."

# The key stack only, shown at the end of the page.
stack:
  - {name: Kotlin Multiplatform, text: "Una sola base de código para Android e iOS: lógica del juego, partidas guardadas y economía."}
  - {name: Compose Multiplatform, text: "Toda la interfaz, compartida por ambas plataformas."}
  - {name: Google Filament, text: "El renderizador físico de Google dibuja la escena 3D en ambas plataformas."}

help:
  - {title: Soporte, text: "¿Encontraste un fallo o perdiste tu progreso? Escríbenos e indica el modelo de tu teléfono.", address: whitesteel400@gmail.com}
  - {title: Privacidad, text: "Qué datos recoge el juego, cómo los usan los anuncios y cómo borrar tus datos.", link_text: Política de privacidad, link: /pocket-armory/privacy/}
---
