import telebot
import requests
import json


bot = telebot.TeleBot('5610828295:AAEaGF8BYKZ13hYiaOy8_Dtv1OIhxtXXuP0')
API = '58e403fde2e7f0d054901efe19f66665'

def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города ')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data['main']['temp']
        bot.reply_to(message, f'Сейчас погода: {temp}')

        image = 'Чисто.png' if temp > 5.0 else 'Пасмурно.png'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, f'Город указан не верно')



bot.polling(none_stop=True)
