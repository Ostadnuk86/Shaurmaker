import requests
from django.http import HttpResponse
from django.shortcuts import render
import telebot
from telebot import types

from Shaurmaker.settings import token_bot, url_webhoock

token = token_bot
bot = telebot.TeleBot(token_bot)


# Create your views here.
def webhoock(request):
    return None


def setwebhoock(request):
    result = requests.get(f'https://api.telegram.org/bot{token_bot}/setWebhook?url={url_webhoock}')
    return HttpResponse(result)
