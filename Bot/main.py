import pathlib

import telebot
import webbrowser
from telebot import types
import sys
import sqlite3
from funcshen import sqlfunc


bot = telebot.TeleBot('5610828295:AAEaGF8BYKZ13hYiaOy8_Dtv1OIhxtXXuP0')

D1 = 'Перейти на сайт'
@bot.message_handler(commands=['start']) #обрабатываю запуск бота
def start(message):


    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Перейти на сайт")
    markup.row(btn1)
    btn2 = types.KeyboardButton('Удалить фото')
    btn3 = types.KeyboardButton('Изменить текст')
    markup.row(btn2, btn3)
    file = open('./Robot.png', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    bot.register_next_step_handler(message, on_click)
    sqlfunc()



def on_click(message):
    if message.text == "Перейти на сайт":
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'Delete')

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://github.com/W83w?tab=repositories')

@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <u>information:</u> <em>Он пустой</em>', parse_mode='html')

@bot.message_handler()
def info(message):
    last_user = message.from_user.last_name
    if last_user != True: # Проверка на пустую фамилию
        last_user = ''
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {last_user}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID:{message.from_user.id}')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://google.com')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.add(btn2, btn3)
    bot.reply_to(message, 'Какое красивое фото!', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)

bot.polling(none_stop=True)

