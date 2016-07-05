#!/usr/bin/evn python
# -*- coding: utf-8 -*-

import random
import telebot
from telebot import types

btn_change = u'найти/сменить собеседника'

token = "239760442:AAExW5RMXJRyRCKVpUAITh0brkQswmxSVns"

# global data store, heh :)
ppl = dict()
bot = telebot.TeleBot(token)

def random_ppl(me):
    free = [k for k,v in ppl.iteritems() if not v and k != me]
    if free:
        return random.choice(free)
    else:
        return 0
#

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    cid = message.chat.id
    if not ppl.get(cid):
        ppl[cid] = 0
    #
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(btn_change)
    bot.reply_to(message, "people2people test bot", reply_markup=markup)
#

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    cid = message.chat.id
    text = message.text
    party = ppl.get(cid)

    if text == u"iddqd":
        bot.send_message(cid, str(ppl))
        return
        
    if text == btn_change:
        if party:
            bot.send_message(party, "disconnected ...")
            bot.send_message(cid, "disconnected ...")
            ppl[party] = 0
            ppl[cid] = 0
        else:
            bot.send_message(cid, "seaching...")
            p = random_ppl(cid)
            if p:
                ppl[p] = cid
                ppl[cid] = p
                bot.send_message(cid, "connected!")
                bot.send_message(p,   "connected!")
            else:
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
