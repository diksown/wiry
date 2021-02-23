import wikipedia 
import re

wikipedia.set_lang("pt")

def results(search):
	return wikipedia.search(search)

def summary(page_name):
	return wikipedia.page(page_name).summary

def lucky(search):
	return summary(results(search)[0])

def short(search):
	temp_summary = lucky(search)
	# not a perfect way to find a sentence, 
	# but the best I could think of.
	m = re.search("\. [A-Z]", temp_summary) 
	if m:
		return temp_summary[:m.start()+1]
	else:
		return temp_summary
