---
title: Pocket Armory
description: Abra baús em 3D, colecione armas de desenho animado e encha seu Arsenal.
layout: landing
landing: true
landing_css: css/pocket-armory-landing.css

tagline: Loot & Shoot
kind: Jogo
icon: images/pa-icon.webp
pitch: Abra baús em 3D, colecione armas de desenho animado e encha seu Arsenal.

# Store buttons. The App Store link is a placeholder until the page exists.
play_url: https://play.google.com/store/apps/details?id=com.lootonomics.dropfire&hl=pt-BR
app_store_url: "#app-store"

hero_screens:
  - {img: images/pa-screen-2.webp, alt: Um baú abrindo em um palco 3D}
  - {img: images/pa-screen-3.webp, alt: "Um fuzil atirando, com números de acerto crítico"}

# The chest strip: what is inside and where gold comes from (layouts/_partials/loot.html).
loot:
  title: Gire. Ganhe. Decida.
  lede: "Cada baú gira uma faixa de armas e para na sua. Gire em 3D, dê alguns tiros e faça a escolha."
  new: Arma nova!
  paths:
    - {icon: keep, title: Fique com ela, text: "Seu Arsenal guarda todas as armas em 3D. As tintas mudam o visual, e uma Lendária pode vir com um chaveiro."}
    - {icon: show, title: Exiba, text: "Armas nos suportes da Vitrine rendem ouro, mesmo quando você está fora."}
    - {icon: sell, title: Venda, text: "Ouro na hora, ou entregue armas para pedidos da Oficina e suba de nível."}
  loop_title: O ouro abre o próximo baú.
  loop_text: "Algumas aberturas são de graça, um anúncio opcional traz um baú melhor, e baús nunca são vendidos por dinheiro de verdade."

# The key stack only, shown at the end of the page.
stack:
  - {name: Kotlin Multiplatform, text: "Uma única base de código para Android e iOS: lógica do jogo, saves e economia."}
  - {name: Compose Multiplatform, text: "Toda a interface, compartilhada pelas duas plataformas."}
  - {name: Google Filament, text: "O renderizador físico do Google desenha a cena 3D nas duas plataformas."}

help:
  - {title: Suporte, text: "Achou um bug ou perdeu seu progresso? Escreva para nós e informe o modelo do seu celular.", address: whitesteel400@gmail.com}
  - {title: Privacidade, text: "Quais dados o jogo coleta, como os anúncios os usam e como apagar seus dados.", link_text: Política de privacidade, link: /pocket-armory/privacy/}
---
