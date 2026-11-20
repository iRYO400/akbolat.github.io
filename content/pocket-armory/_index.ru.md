---
title: Pocket Armory
description: Открывай 3D-сундуки, собирай мультяшное оружие и наполняй Оружейную.
layout: landing
landing: true
landing_css: css/pocket-armory-landing.css

tagline: Loot & Shoot
kind: Игра
icon: images/pa-icon.webp
pitch: Открывай 3D-сундуки, собирай мультяшное оружие и наполняй Оружейную.

# Кнопки магазинов. Ссылка App Store — заглушка, пока страницы нет.
play_url: https://play.google.com/store/apps/details?id=com.lootonomics.dropfire&hl=ru
app_store_url: "#app-store"

hero_screens:
  - {img: images/pa-screen-2.webp, alt: Сундук открывается на 3D-сцене}
  - {img: images/pa-screen-3.webp, alt: "Автомат стреляет, над ним цифры урона"}

loot:
  title: Лента, пушка, твой выбор
  lede: "Каждый сундук прокручивает ленту с пушками и останавливается на твоей. Покрути её в 3D, постреляй и решай, что с ней делать."
  new: Новая пушка!
  paths:
    - {icon: keep, title: Оставить, text: "Оружейная хранит каждую пушку в 3D. Краски меняют её вид, а с легендарной может выпасть брелок."}
    - {icon: show, title: На Витрину, text: "Пушки на Витрине приносят золото, даже когда тебя нет."}
    - {icon: sell, title: Продать, text: "Сразу получить золото или сдать пушки в заказы Мастерской и расти в уровнях."}
  loop_title: Золото открывает следующий сундук.
  loop_text: "Несколько открытий дарим просто так, необязательная реклама даёт сундук получше, а за настоящие деньги сундуки не продаются."


stack:
  - {name: Kotlin Multiplatform, text: "Один код на Android и iOS: логика игры, сохранения и экономика."}
  - {name: Compose Multiplatform, text: "Весь интерфейс, общий для обеих платформ."}
  - {name: Google Filament, text: "Физически корректный рендер от Google рисует 3D-сцену на обеих платформах."}

help:
  - {title: Поддержка, text: "Нашёл ошибку или пропал прогресс? Напиши нам и укажи модель телефона.", address: whitesteel400@gmail.com}
  - {title: Конфиденциальность, text: "Что собирает игра, как это использует реклама и как удалить свои данные.", link_text: Политика конфиденциальности, link: /pocket-armory/privacy/#ru}
---
