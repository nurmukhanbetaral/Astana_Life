# keyboards.py
from telebot import types

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn2 = types.KeyboardButton("Куда можно сходить:")
    btn3 = types.KeyboardButton("🔥 Ближайшие события")
    btn_info = types.KeyboardButton("🤖 О боте")
    markup.add(btn3)
    markup.add(btn2)
    markup.add(btn_info)
    return markup

def events_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton("🎭 Спектакль в Астана Opera")
    btn2 = types.KeyboardButton("🏀 Матч в Барыс Арене")
    btn3 = types.KeyboardButton("🎨 Выставка в Нацмузее")
    btn_back = types.KeyboardButton("⬅️ Назад в меню ")
    markup.add(btn1, btn2, btn3, btn_back)
    return markup

def places_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("🌲 Парки и зоны отдыха")
    btn2 = types.KeyboardButton("🍕 Поесть (Кафе и рестораны)")
    btn3 = types.KeyboardButton("📸 Достопримечательности")
    btn4 = types.KeyboardButton("🛍️ Шопинг и кино")
    btn5 = types.KeyboardButton("🎭 Культура и искусство")
    btn6 = types.KeyboardButton("🎮 Развлечения и досуг")
    btn_back = types.KeyboardButton("⬅️ Назад")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    markup.add(btn_back) # Кнопка назад красивой строкой внизу
    return markup
def entertainment_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton("Каток «Алау» ⛸️")
    btn2 = types.KeyboardButton("Квест-румы 🗝️")
    btn3 = types.KeyboardButton("Караоке 🎤")
    btn_back = types.KeyboardButton("⬅️ Назад в меню")
    markup.add(btn1, btn2, btn3, btn_back)
    return markup
def parks_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton("🌳 Президентский парк")
    btn2 = types.KeyboardButton("🚶‍♂️Линейный парк")
    btn3 = types.KeyboardButton("🌿 Ботанический сад")
    btn4 = types.KeyboardButton("🌊 Набережная Есиль")
    btn_back = types.KeyboardButton("⬅️ Назад в меню")
    markup.add(btn1, btn2, btn3, btn4, btn_back)
    return markup
def culture_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton("Астана Опера 🎻")
    btn2 = types.KeyboardButton("Национальный музей 🏺")
    btn3 = types.KeyboardButton("Ailand 🐠")
    btn4 = types.KeyboardButton("Астана Балет 🩰")
    btn_back = types.KeyboardButton("⬅️ Назад в меню")
    markup.add(btn1, btn2, btn3, btn4, btn_back)
    return markup
def eat_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton("Sandyq 🥘")
    btn2 = types.KeyboardButton("Rafe ☕")
    btn3 = types.KeyboardButton("Selfie 🥂")
    btn4 = types.KeyboardButton("Crepe Cafe 🥞")
    btn_back = types.KeyboardButton("⬅️ Назад в меню")
    markup.add(btn1, btn2, btn3, btn4, btn_back)
    return markup

def attractions_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton("Байтерек 🗼")
    btn2 = types.KeyboardButton("Сфера «Нур Алем» 🔮")
    btn3 = types.KeyboardButton("Пирамида 📐")
    btn4 = types.KeyboardButton("Мечеть Хазрет Султан 🕌")
    btn_back = types.KeyboardButton("⬅️ Назад в меню")
    markup.add(btn1, btn2, btn3, btn4, btn_back)
    return markup
def shopping_center_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton("Хан Шатыр 🎪")
    btn2 = types.KeyboardButton("Mega Silk Way 🛍️")
    btn3 = types.KeyboardButton("Abu Dhabi Plaza 🏢")
    btn4 = types.KeyboardButton("Kinopark / Chaplin")
    btn_back = types.KeyboardButton("⬅️ Назад в меню")
    markup.add(btn1, btn2, btn3, btn4, btn_back)
    return markup

def get_2gis_button(url):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text="Открыть в 2GIS 📍", url=url)
    markup.add(btn)
    return markup
