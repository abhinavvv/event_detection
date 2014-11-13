import json
import nltk
import re
from nltk.corpus import *
from collections import Counter

raw_data = {}
with open("football_soccer.json") as json_file:
    json_data = json.load(json_file)
    raw_data = json_data


corpus = {}
for each_story in raw_data["data"]["relevantStories"]:
	corpus[each_story["item"]["title"]] = each_story["item"]["rawDescriptionText"]
	

#preprocessing
char_regex = re.compile(r'[^a-zA-Z]+')
stop_words  = set(stopwords.words('english'))

for story in corpus.keys():
	char_alone = char_regex.sub(" ",corpus[story])
	tokenize = nltk.word_tokenize(char_alone)
	lowered_text = [w.lower() for w in tokenize]
	corpus[story] = [w for w in lowered_text if not w in stop_words]


#word counts !!!
#develop on this! :D
for story,tokens in corpus.iteritems():
	print Counter(tokens)
	break





	
		


