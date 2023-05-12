import os
from dotenv import load_dotenv
import telebot
import requests
import csv

# TODO: 1.1 Get your environment variables

load_dotenv()
yourkey = os.getenv('key')
bot_id = os.getenv('token')

bot = telebot.TeleBot(bot_id, parse_mode=None)

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')


@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    bot.reply_to(message, 'Getting movie info...')

    # TODO: 1.2 Get movie information from the API

    movie_name = message.text.split(' ', 1)[1]
    url = requests.get(f"http://www.omdbapi.com/?apikey={yourkey}&t&t={movie_name}")
    info = url.json()

    # TODO: 1.3 Show the movie information in the chat window

    if info['Response'] == 'False':
        bot.reply_to(message, 'No movie found!')
    else:
        global title, year, rating, poster, released
        title = info['Title']
        year = info['Year']
        rating = info['imdbRating']
        poster = info['Poster']
        released = info['Released']

        bot.reply_to(message, f'Title: {title}\nYear: {year}\nRated: {rating}\nPoster: {poster}\nReleased: {released}')

    # TODO: 2.1 Create a CSV file and dump the movie information in it

    with open('movies.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([title, year, rating, poster, released])


@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')

    # TODO: 2.2 Send downlodable CSV file to telegram chat

    with open('movies.csv', 'rb') as file:
        bot.send_document(chat_id=message.chat.id, document=file)
        bot.reply_to(message, 'CSV file generated! You can download it now.')


@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')

bot.infinity_polling()
