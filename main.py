import telebot
import requests
from telebot import types

bot = telebot.TeleBot("1587462822:AAEXWuWScN9WUlhD4VAe_ezTCaDzBZgfuZM")

response = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5").json()

@bot.message_handler(commands=['start', 'help'])
def add_keyboard(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('USD')
    itembtn2 = types.KeyboardButton('EUR')
    itembtn3 = types.KeyboardButton('RUR')
    itembtn4 = types.KeyboardButton('BTC')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(message.chat.id,"Узнать наличный курс ПриватБанка", reply_markup=markup)
    bot.register_next_step_handler(message, process_coin_step)

def process_coin_step(message):
    for coin in response:
        if (message.text == coin['ccy']):
            bot.send_message(message.chat.id, printCoin(coin['buy'], coin['sale']), parse_mode="Markdown")
    bot.register_next_step_handler(message, process_coin_step)
def printCoin(buy, sale):
    return "💰 *Курс покупки:* " + str(buy) + "\n💰 *Курс продажи:* " + str(sale)



if __name__ == '__main__':
    bot.polling(none_stop=True)