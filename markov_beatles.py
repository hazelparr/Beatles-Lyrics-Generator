# Beatles Lyrics Generator
# A Markov Chain implementation in Python

import random
from collections import defaultdict

class LyricsGenerator(object):
	




	# split source data into a list
	def source_data(self, text, order = 2):
		data_split = text.split()
		return data_split

	#read from source doc
	def data_file(self):
		source = open("source", "r")
		data = source.read()
		source.close
		return data


	def first_word(self, text, order):
		data_list = self.source_data(text, order)
		index = random.randint(0, len(data_list))
		return data_list[index]


	def lyrics_model(self, text, order):
		model = defaultdict(list)
		data_list = self.source_data(text, order)
		lyrics = []
		for i in range (0, len(data_list) - order):
			lyrics.append(tuple(data_list[i:i+order]))
		for word, next_word in lyrics:
			model[word].append(next_word)
		return model


	def generate_lyrics(self, text, order):
		output = []
		prev_word = self.first_word(text, order)
		lyrics = self.lyrics_model(text, order)
		output.append(prev_word)
		for i in range(34):
			next_word = random.choice(lyrics[prev_word])
			output.append(next_word)
			prev_word = next_word
		new_output = [output[i:i+5] for i in range (0, len(output), 5)]
		for row in new_output:
			space = " "
			stanza = print(space.join(row))
		return stanza

print("BEATLES LYRICS GENERATOR")
print("ENTER 'Y' TO GENERATE LYRICS OR ANY KEY TO EXIT")
choice = input("Generate Lyrics?")
choice = choice.lower()

while choice == "y":
	print("\n")
	t = LyricsGenerator()
	t.generate_lyrics(t.data_file(), 2)

	choice = input("\n\nGenerate Lyrics? (Y/N)")