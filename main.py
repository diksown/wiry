from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
import logging
from wiki import short
import time
import os

TOKEN = open('token').read()[:-1]

def start(update, context):
	s = "say something 2 me and I'll search that on wikipedia 4 you 😊"
	start_time = time.time()
	update.message.reply_text(s)
	end_time = time.time()
	logging.info(f"=== replying start took me {end_time - start_time}s. ===")

def search(update, context):
	start_time = time.time()
	search = update.message.text
	s = short(search)
	end_time = time.time()
	logging.info(f"=== that \"{search}\" search took {end_time - start_time}s. ===")
	update.message.reply_text(s)

def main():
	logger = logging.getLogger(__name__)
	logging.basicConfig(level=logging.INFO,
			format 	= "%(asctime)s [%(levelname)s] %(message)s")

	updater = Updater(token=TOKEN, use_context=True)
	dp = updater.dispatcher

	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(MessageHandler(Filters.text & (~Filters.command), search))
	
	updater.start_polling()
	logging.info("=== wiry is working hard to help you ===")
	updater.idle()
	logging.info("=== wiry is dead. long live to wiry. ===")

if __name__ == "__main__":
	main()
