import re
def word_list(text):
      return list(filter(None, re.split('\W+', text)))
print (word_list("I am going to school"))
