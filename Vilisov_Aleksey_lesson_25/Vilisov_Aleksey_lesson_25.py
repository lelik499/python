
#ДЗ на вторник:
# Добавить функционал боту:
# Кнопки:
#     Хочу анекдот - показывает текстовый анекдот
#     Хочу спать
#     Прощание с ботом
#     Приветствие бота


# tokin='5772844504:AAGEGggWEhRddVcqHeXgZox-zFURYA2ZWu8'


import telebot
from telebot import types
tokin='5772844504:AAGEGggWEhRddVcqHeXgZox-zFURYA2ZWu8'

bot = telebot.TeleBot(tokin)

def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    bot_hello=types.InlineKeyboardButton(text='Привет бот',callback_data='0')
    drink_btn = types.InlineKeyboardButton(text='Хочу пить', callback_data='1')
    eat_btn = types.InlineKeyboardButton(text='Хочу есть', callback_data='2')
    anekdot_btn=types.InlineKeyboardButton(text='Хочю анектот',callback_data='3')
    sleep_bot=types.InlineKeyboardButton(text='Спокойной ночи',callback_data='4')
    good_bye=types.InlineKeyboardButton(text='Пока бот',callback_data='5')

    keyboard.add(bot_hello,drink_btn, eat_btn,anekdot_btn,sleep_bot,good_bye)
    return keyboard

@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, 'Приветствую. Выберите, что вы хотите: ', reply_markup=create_keyboard())


@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.message:
        if call.data == '0':
            img = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTr1665085OpVjVjGS0_R0vpgeO94Q9TzR0G3fzcYx7kKkrfuZsJRJaWvXVVnTO7N-6JoY&usqp=CAU'
            bot.send_photo(chat_id=call.message.chat.id, photo=img, caption='Картинка с приветствием',reply_markup=create_keyboard())

        if call.data == '1':
            img = 'https://upload.wikimedia.org/wikipedia/commons/c/c0/Water_drop_impact_on_a_water-surface_-_%282%29.jpg'
            bot.send_photo(chat_id=call.message.chat.id,photo=img,caption='Картинка воды', reply_markup=create_keyboard())
        if call.data == '2':
            img = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRkqaSMQoYITp4XzPmB590Xp7LZtd2pgA1jpA&usqp=CAU'
            bot.send_photo(chat_id=call.message.chat.id, photo=img, caption='Картинка еды',reply_markup=create_keyboard())
        if call.data=='3':
            img='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwuYwh-hBkrLIPAD5gfEVTEYMTVTwif1umSLRXTcDZxA&s'
            bot.send_photo(chat_id=call.message.chat.id, photo=img, caption='Картинка с анекдотом', reply_markup=create_keyboard())
        if call.data=='4':
            img='https://otkrit-ka.ru/uploads/posts/2021-07/foto-i-kartinki-spat-pora-2.gif'
            bot.send_photo(chat_id=call.message.chat.id, photo=img, caption='Картинка со сном',reply_markup=create_keyboard())
        if call.data =='5':
            img = 'https://avatars.mds.yandex.net/i?id=029e100e4c469ce279191af4212f59465ab5d840-8372844-images-thumbs&n=13'
            bot.send_photo(chat_id=call.message.chat.id, photo=img, caption='Картинка со прощанием',
                           reply_markup=create_keyboard())



bot.polling(none_stop=True)


#ДЗ на вторник:
# Добавить функционал боту:
# Кнопки:
#     Хочу анекдот - показывает текстовый анекдот
#     Хочу спать
#     Прощание с ботом
#     Приветствие бота
