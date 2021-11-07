#!/usr/bin/python

import os
import sys
import telebot
from telebot import types

def text_search(message):
    line_number = 0
    drugs = []
    substr = message.lower()
    with open('wada.txt', 'r') as file:
        for line in file:
            line_number += 1
            if line.lower().find(substr) != -1:
                drugs.append(line.rstrip(''))
    listToStr = ' '.join(map(str, drugs))
    if drugs:
        return "Don't do drugs, folks!\n\nI found drugs in list:\n\n" + listToStr
    else:
        return "No drug found"


bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "WADA prohibited list search. Please enter the drug name")

@bot.message_handler(content_types=['text'])
@bot.message_handler(func=lambda message: len(message.text) > 3)
def get_text_messages(message):
    bot.reply_to(message, text_search(message.text))


bot.infinity_polling()


