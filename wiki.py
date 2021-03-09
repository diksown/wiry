import wikipedia 

wikipedia.set_lang("en")

def results(search):
	'''
	Lists the pages on wikipedia related to the keyword `search`.
	'''
	return wikipedia.search(search)

def short(search):
	'''
	Searches the keyword `search` on wikipedia and returns a short summary of it.
	'''
	pages = results(search)

	if len(pages) == 0:
		return "I couldn't find anything for you 😭", ""

	else:
		summary = ""
		no_sentences = 1
		remaining_tries = 3

		while len(summary) < 30:
			summary = wikipedia.summary(pages[0], 
					auto_suggest=False, sentences=no_sentences)

			no_sentences += 1
			remaining_tries -= 1

			if remaining_tries == 0:
				break

		return summary, pages[0]

def multiple_shorts(search):
	results_list = results(search)
	shorts = []
	for i in results_list[:3]:
		shorts.append(short(i))
	return shorts
