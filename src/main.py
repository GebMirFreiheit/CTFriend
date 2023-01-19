import telebot
import os
from model_training import openai, text_cleaner
from handler import get_response_from_table

telebot.apihelper.ENABLE_MIDDLEWARE = True

# Укажем token полученный при регистрации бота
bot = telebot.TeleBot(os.environ.get('telegram_token'))


# Начнем обработку. Если пользователь запустил бота, ответим
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id,
                     " Здравствуйте. Я бот, который поможет вам начать \
                        ориентироваться в ctf!")


# Если пользователь что-то написал, ответим
@bot.message_handler(func=lambda message: True)
def get_text_messages(message):
    text_clf = openai()

    query = text_cleaner(message.text)

    scores = text_clf.predict_proba([query]).tolist()[0]
    if max(scores) < 0.75:
        resp = get_response_from_table('Fallback')
    else:
        category = text_clf.predict([query])[0]
        resp = get_response_from_table(category)

    # отправим ответ
    bot.send_message(message.from_user.id, resp)

    # выведем в консоль вопрос / ответа
    print("Запрос:", query, " \n\t\tОтвет :", resp)


# Запустим обработку событий бота
bot.infinity_polling(none_stop=True, interval=1)
