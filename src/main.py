import telebot
import os

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
    query = message.text

    if 'крипто' in query:
        answer = 'Материалы по криптографии:' \
            ' \n https://kmb.cybber.ru/crypto/main.html \n Задания на' \
            ' криптографию: \n https://cryptopals.com/'
    elif 'xss' in query:
        answer = 'Материалы по XSS:' \
            ' \n https://portswigger.net/web-security/cross-site-scripting \n'\
            ' Задания на XSS: \n http://xss.school.sibears.ru/easy/0'
    else:
        answer = 'Пока не знаю, как помочь, но могу посоветовать источники!' \
            'http://itsecwiki.org/index.php/Заглавная_страница'

    # отправим ответ
    bot.send_message(message.from_user.id, answer)

    # выведем в консоль вопрос / ответа
    print("Запрос:", query, " \n\t\tОтвет :", answer)


# Запустим обработку событий бота
bot.infinity_polling(none_stop=True, interval=1)
