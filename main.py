from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent
from telegram.ext import Updater, CommandHandler, MessageHandler, \
		 InlineQueryHandler, Filters
from telegram.utils.helpers import escape_markdown
from uuid import uuid4
import logging
from wiki import short
import time
import os

TOKEN = os.environ['WIRY_KEY']

def start(update, context):
	s = "say something 2 me and I'll search that on wikipedia 4 you 😊"
	start_time = time.time()
	update.message.reply_text(s)
	end_time = time.time()
	logging.info(f"=== replying start took me {end_time - start_time}s. ===")

def search(update, context):
	start_time = time.time()
	search = update.message.text
	s = short(search)[0]
	end_time = time.time()
	logging.info(f"=== that \"{search}\" search took {end_time - start_time}s. ===")
	update.message.reply_text(s)

def inlinequery(update, context):
	'''Handle the inline query.'''
	query = update.inline_query.query
	'''boilerplate code:
		  
    results = [
        InlineQueryResultArticle(
            id=uuid4(), title="Caps", input_message_content=InputTextMessageContent(query.upper())
		)
	]
	'''
	summary, page_title = short(query)
	results = [
		InlineQueryResultArticle(
			id=uuid4(), title=page_title, description=" _"+summary[:20]+"..._", input_message_content=InputTextMessageContent(summary)
		)
	]
	update.inline_query.answer(results)

def main():
	logger = logging.getLogger(__name__)
	logging.basicConfig(level=logging.INFO,
			#format 	= "%(asctime)s [%(levelname)s] %(message)s")
			#heroku already have a time log.
			format 	= "%(message)s")

	updater = Updater(token=TOKEN, use_context=True)
	dp = updater.dispatcher

	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(MessageHandler(Filters.text & (~Filters.command), search))
	dp.add_handler(InlineQueryHandler(inlinequery))
	
	updater.start_polling()
	logging.info("=== wiry is working hard to help you ===")
	updater.idle()
	logging.info("=== wiry is dead. long live to wiry. ===")

if __name__ == "__main__":
	main()
