import string

#list of words to skip
skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would']

def filter_words(words, skip_words):

    result = []

	#loops through the user input string
    for x in words:
    	#loops the user input through the list of skippable words
        if not (x in skip_words):
        	#adds to the final string if not a skippable word
            result.append(x)

    #returns the formatted list of words
    return result

def remove_punct(text):

	#initialises the variable no_punct as blank
    no_punct = ""
    #loops through all the characters in the user input string
    for char in text:
    	#checks if each character is punctuation or not
        if not (char in string.punctuation):
        	#if the character is not punctuation, it is added to the string no_punct
            no_punct += char

    return no_punct

def remove_numbers(text):
    """
    >>> remove_numbers('12go 3west')
    'go west'
    """
    no_numb = ""

    for char in text:
      if not (char in "1234567890"):
        no_numb += char

    return no_numb

def normalise_input(user_input):

	#runs the function remove_punct as initialises the variable no_punct with the result
  no_number = remove_numbers(user_input)
  no_punct = remove_punct(no_number).lower()

  #initialises the list list_word as blank
  list_word = []
  #breaks up list_word into seperate parts
  for word in no_punct.split():
      list_word.append(word)

  #runs filter_words
  final_words = filter_words(list_word, skip_words)

  #if final_words == "east" or "west" or "south" or "north":
  #    final_words.insert(0, 'go')

  return final_words
