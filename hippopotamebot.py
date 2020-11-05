#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 13:13:43 2020

@author: a1
"""

import telebot
import os
from flask import Flask, request

server = Flask(__name__)

token = '1305589892:AAEyYeL6k9CIxFrv5E88pSO19plsxiUecKY'
bot = telebot.TeleBot(token)

kb1 = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
kb1.row('Боли', 'Раздражительность')
kb1.row('Бессоница', 'Плохой аппетит', 'Усталость')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте, что вас беспокоит?', 
                     reply_markup=kb1)
    
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'боли':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMQX5lQ3rxT5YW9UvKTLKMkXsqPq5gAAhcCAALPX4sH54asnNGoawwbBA')
    elif message.text.lower() == 'раздражительность':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMOX5lP7WkTWkq7kn5EUEL6X7npIq4AAiACAALPX4sHNAABBQJL68vOGwQ')
    elif message.text.lower() == 'бессоница':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMSX5lRQbOpnoMBYVmHYBmja-LgCmIAAi4CAALPX4sHSZBblU9rmfkbBA')
    elif message.text.lower() == 'плохой аппетит':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMPX5lQb7gk6-iXhmrsRVtSlTOHGEsAAjICAALPX4sHgo0Z-0l-QC0bBA')
    elif message.text.lower() == 'усталость':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMRX5lQ_0R0UVXuy2nELNbn89rVu9oAAiICAALPX4sHOkfVfa4YzYwbBA')

#bot.polling()
@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://warm-headland-90063.herokuapp.com/' + tokenBot.TOKEN)
    return "!", 200

if __name__ == '__main__':
    server.debug = True
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
