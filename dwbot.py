#!/usr/bin/evn python
# -*- coding: utf-8 -*-

import telebot
from telebot import types


btn_change = 'найти/сменить собеседника'

token = "239760442:AAExW5RMXJRyRCKVpUAITh0brkQswmxSVns"

# global data store, heh :)
ppl = dict()
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btn_change)
    bot.reply_to(message, "people2people test bot", reply_markup=markup)
#

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    cid = message.chat.id
    text = message.text
    party = ppl.get(cid)

    if text == btn_change:
        if party:
            bot.send_message(party, "disconnected ...")
            ppl[party] = 0
            ppl[cid] = 0
        else:
            bot.send_message(cid, "seaching...")
            for k,v in ppl.iteritems():
                if not v:
                    ppl[k] = cid
                    ppl[cid] = k
                    bot.send_message(cid, "connected!")
                    bot.send_message(k,   "connected!")
                    return
            #
            bot.send_message(cid, "not found :(")
    else:
        if party:
            bot.send_message(party, text)
        else:
            bot.send_message(cid, "you are alone")
    #
#

bot.polling()

#.
