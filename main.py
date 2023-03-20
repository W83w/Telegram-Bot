import telebot
import webbrowser

bot = telebot.TeleBot('5610828295:AAEaGF8BYKZ13hYiaOy8_Dtv1OIhxtXXuP0')

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
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID:{message.from_user.id}')


bot.polling(none_stop=True)

