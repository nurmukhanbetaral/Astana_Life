# main.py
import telebot
import keyboards
import places_data  # Твой новый файл с данными!
from telebot import types

TOKEN = '8732624237:AAG4_2n07jaE1aG9uFg66t1JlruaIcxbniw'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        f"Салам, {message.from_user.first_name}! Это Астана Лайф. Выбирай:",
        reply_markup=keyboards.main_menu()
    )


@bot.message_handler(content_types=['text'])
def handle_messages(message):
    # --- ГЛАВНЫЕ РАЗДЕЛЫ ---
    if message.text == "🔥 Ближайшие события":
        bot.send_message(message.chat.id, "Выбери мероприятие:", reply_markup=keyboards.events_menu())

    elif message.text == "🤖 О боте":
        about_text = (
            "🌟 **Астана Лайф** — твой персональный гид по столице!\n\n"
            "**Что я умею:**\n"
            "✅ Показывать крутые места для прогулок.\n"
            "✅ Советовать, где в Астане самая вкусная еда.\n"
            "✅ Рассказывать о главных событиях города.\n\n"
            "Просто нажимай на кнопки в меню, и я всё покажу! 🚀"
        )
        bot.send_message(message.chat.id, about_text, parse_mode='Markdown')

    elif message.text == "Куда можно сходить:":
        bot.send_message(message.chat.id, "Выбери куда хочешь сходить", reply_markup=keyboards.places_menu())

    # --- КАТЕГОРИИ МЕСТ ---
    elif message.text == "🌲 Парки и зоны отдыха":
        bot.send_message(message.chat.id, "В Астане много классных парков. Какой именно тебя интересует?",
                         reply_markup=keyboards.parks_menu())

    elif message.text == "🍕 Поесть (Кафе и рестораны)":
        bot.send_message(message.chat.id,
                         "«В Астане столько крутых заведений открылось. Пойдем протестируем какое-нибудь?» 🍔",
                         reply_markup=keyboards.eat_menu())

    elif message.text == "📸 Достопримечательности":
        bot.send_message(message.chat.id, "«Хочешь увидеть символы столицы? У меня есть подборка мест!» 🏛️",
                         reply_markup=keyboards.attractions_menu())
    elif message.text == "🛍️ Шопинг и кино":
        bot.send_message(message.chat.id, "«Хочешь обновить гардероб или зацепить новинки кино на большом экране? Выбирай лучший ТРЦ города!» 🛍️",
                         reply_markup=keyboards.shopping_center_menu())
    elif message.text == "🎭 Культура и искусство":
        bot.send_message(message.chat.id, "«Хочешь прикоснуться к прекрасному? В Астане потрясающие театры и музеи. Выбирай, куда купить билет!» 🎭",
                         reply_markup=keyboards.culture_menu())
    elif message.text == "🎮 Развлечения и досуг":
        bot.send_message(message.chat.id,"«Скучать сегодня точно не придется! В Астане много мест для активного отдыха. Что выберешь?» 🎮",
                         reply_markup=keyboards.entertainment_menu())
        # --- УНИВЕРСАЛЬНЫЙ ОБРАБОТЧИК МЕСТ ИЗ ДАННЫХ ---
    elif message.text in places_data.PLACES:
        info = places_data.PLACES[message.text]

        try:
            # Открываем локальный файл картинки в бинарном режиме ('rb')
            with open(info["img"], 'rb') as photo:
                bot.send_photo(
                    message.chat.id,
                    photo,  # Отправляем сам файл, а не ссылку
                    caption=info["text"],
                    parse_mode='Markdown',
                    reply_markup=keyboards.get_2gis_button(info["2gis"])
                )
        except FileNotFoundError:
            # Если ты забыл положить картинку в папку images, бот не упадет, а предупредит тебя
            bot.send_message(
                message.chat.id,
                f"Ошибка: Не удалось найти файл картинки по пути `{info['img']}`. Проверь папку images!",
                parse_mode='Markdown'
            )
    # --- КНОПКА НАЗАД ---
    elif message.text == "⬅️ Назад в меню":
        # Возвращаем пользователя к выбору категорий
        bot.send_message(message.chat.id, "Выбирай категорию:", reply_markup=keyboards.places_menu())
    elif message.text == "⬅️ Назад":
        bot.send_message(
            message.chat.id,
            f"Салам, {message.from_user.first_name}! Это Астана Лайф. Выбирай:",
            reply_markup=keyboards.main_menu()
        )


# Безопасный запуск бота
if __name__ == '__main__':
    print("Бот успешно запущен и работает...")
    try:
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except Exception as e:
        print(f"Замечена заминка в сети, но я продолжаю работать! Ошибка: {e}")