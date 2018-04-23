# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('GuilehmBOT')

conv = ['oi', 'olá', 'olá, bom dia','bom dia', 'bom dia, como vai?',
        'eu vou bem, e você?','comigo tudo ótimo','você estuda?',
        'sim, estudo programação em Python', 'eu estudo JavaScript',
        'como você chama?','me chamo GuilehmBOT', 'como você foi criado?',
        'eu fui criado em Python', 'quais são seus hobbies?',
        'cubo mágico e programação','que legal!', 'sim, eu gosto muito',
        'você trabalha?', 'sim, sou desenvolvedor',
        ]

bot.set_trainer(ListTrainer)
bot.train(conv)

while True:
    quest = input('Você: ')
    response = bot.get_response(quest)
    print('Bot: ', response)