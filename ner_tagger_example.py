# -*- coding: utf-8 -*-

from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

st = StanfordNERTagger('/usr/share/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
					   '/usr/share/stanford-ner/stanford-ner.jar',
					   encoding='utf-8')

text = 'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.'

tokenized_text = word_tokenize(text)
classified_text = st.tag(tokenized_text)

print(classified_text)

## Change the path according to your system
stanford_classifier = 'D:\StanfordParser\stanford-ner-2015-12-09\classifiers\english.all.3class.distsim.crf.ser.gz'
stanford_ner_path = 'D:\StanfordParser\stanford-ner-2015-12-09\stanford-ner.jar'

# Creating Tagger Object
st = StanfordNERTagger(stanford_classifier, stanford_ner_path, encoding='utf-8')
