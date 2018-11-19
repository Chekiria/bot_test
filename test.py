import telebot


token = '682332597:AAEeGdsSQtrksabYWlKppH9HfTPeOiqXDnA'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

print('hello')

if __name__ == '__main__':
     bot.polling(none_stop=True)