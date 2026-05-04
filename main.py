import telebot
import random
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import pytz
from flask import Flask
from threading import Thread

TOKEN = '8655347308:AAGGFrzwpW9j9Rh6WicBUMLbgf6FgPVSCXc'
CHAT_ID = '7532512621'
bot = telebot.TeleBot(TOKEN)
casa_tz = pytz.timezone('Africa/Casablanca')

app = Flask('')
@app.route('/')
def home():
    return "Bot khdam"
def run():
  app.run(host='0.0.0.0',port=8080)
def keep_alive():
    t = Thread(target=run)
    t.start()

TEAMS = [
    {"team1": "Real Madrid", "team2": "Barcelona", "shots": 30.2, "corn
