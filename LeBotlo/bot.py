from telegram.ext import Updater
from telegram.ext import CommandHandler
updater = Updater(token='435556884:AAFTFOQEBYz3nPVvzMn5qDajO7P8es6osJw')
dispatcher = updater.dispatcher

from btc import brl, usd # usd é uma variável, dá pra passar direto, atentar a isso

#brl = btc.brl
#usd = str(btc.usd)

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text= "I'm a bot, please talk to me!")

def olar(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="Porra, essa referência está ficando meio velha né? mas Frozen é bom de mais LIVRE ESTOOOOOOOU LIVRE STOOOUOUOU!")

def maroto(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text= "Diz-se de ou indivíduo de espírito inventivo, cheio de manhas e espertezas; ladino, vivo, malandro, chamado Julius.")

def feira(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text= "Assista essa porra: https://www.youtube.com/watch?v=YYb7Nl8cvSU")

def btc(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text= "Preço do Bitcoin é: R$" + usd)

# Adding the commands to the dispatcher of CommandHandler
start_handler = CommandHandler('start',start)
dispatcher.add_handler(start_handler)
olar_handler = CommandHandler('olar', olar)
dispatcher.add_handler(olar_handler)
maroto_handler = CommandHandler('maroto', maroto)
dispatcher.add_handler(maroto_handler)
feira_handler = CommandHandler('feira', feira)
dispatcher.add_handler(feira_handler)
btc_handler = CommandHandler('btc', btc)
dispatcher.add_handler(btc_handler)

updater.start_polling()
