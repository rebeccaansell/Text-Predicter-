import nltk
# objective is to display next word suggestions from both of the texts
# Model 1 = Dorian Gray
# Model 2 = Wuthering Heights

def freqRankList(tokens):
    freqs = {}
    for token in tokens:
        if token in freqs:
            freqs[token] += 1
        else:
            freqs[token] = 1
    freqs = sorted(freqs.items(),
                   reverse = True,
                   key = lambda x: x[1])
    return [word for word, _ in freqs[:5]]

def createModel1(filename):
    with open(filename, 'r', encoding='utf8') as f:
        text = f.read().lower()
    tokenizer = nltk.tokenize.RegexpTokenizer(r'[-\'A-Za-z]+')
    tokens = tokenizer.tokenize(text)
    model1 = {}
    # Let's use empty string as the key for unigram
    # frequencies (given no or unknown input).
    model1[''] = tokens
    # For a bigram "W V", I'd like to collect
    # and rank all the possible Vs that follow W.
    for w1, w2 in nltk.ngrams(tokens, 2):
        if w1 in model1:
            model1[w1].append(w2)
        else:
            model1[w1] = [w2]
    # For trigrams, key off a two-word sequence
    # that then associates with a list of ranked
    # words in the third position. Use punctuation
    # to create the key, like "mr|wentworth"
    # Rank all the word lists
    for key, words in model1.items():
        model1[key] = freqRankList(words)
    return model1

def createModel2(filename):
    with open(filename, 'r', encoding='utf8') as f:
        text = f.read().lower()
    tokenizer = nltk.tokenize.RegexpTokenizer(r'[-\'A-Za-z]+')
    tokens = tokenizer.tokenize(text)
    model1 = {}
    # Let's use empty string as the key for unigram
    # frequencies (given no or unknown input).
    model1[''] = tokens
    # For a bigram "W V", I'd like to collect
    # and rank all the possible Vs that follow W.
    for w1, w2 in nltk.ngrams(tokens, 2):
        if w1 in model1:
            model1[w1].append(w2)
        else:
            model1[w1] = [w2]
    # For trigrams, key off a two-word sequence
    # that then associates with a list of ranked
    # words in the third position. Use punctuation
    # to create the key, like "mr|wentworth"
    # Rank all the word lists
    for key, words in model1.items():
        model1[key] = freqRankList(words)
    return model1

def autoSuggestWords1(model1, textSoFar):
    try:
        return model1[textSoFar[-1]]
    except (IndexError, KeyError):
        return model1['']
# function to use model to determine next word for DG 

def autoSuggestWords2(model2, textSoFar):
    try:
        return model2[textSoFar[-1]]
    except (IndexError, KeyError):
        return model2['']
# function to use model to determine next word for WH 

def main():
    model1 = createModel1('Dorian_Gray.txt')
    # training model1 is based off of the book: The Picture of Dorian Gray
    model2 = createModel2('wuthering_heights.txt')
    # training model1 is based off of the book: Wuthering Heights
    textSoFar = []
    # empty text input so far

    while True:
        print("Draft:", ' '.join(textSoFar)) # prints current sentence

        suggestions1 = autoSuggestWords1(model1, textSoFar) 
        # calls function to: add suggestions for next word based off of text so far: for DG 
        print("Suggestions according to Dorian Gray:", ' '.join(
            [f"{i+1}:{word}" for i, word
             in enumerate(suggestions1)]
            )) # prints out suggestions

        suggestions2 = autoSuggestWords2(model2, textSoFar) 
        # calls function to: add suggestions for next word based off of text so far: for WH 
        print("Suggestions according to Wuthering Heights:", ' '.join(
            [f"{i+1}:{word}" for i, word
             in enumerate(suggestions2)]
            )) # prints out suggestions


        word = input("Next word? ") # gets input for next word 
        if word == ".":
            print("Your final sentence is:", ' '.join(textSoFar),'.')
            break 
            # sentence is ended by a period and final sentence is displayed
        else:
            try:
                i = int(word)-1
                word = suggestions[i]
            except ValueError:
                pass
                
        textSoFar.append(word) # adds word to sentence if not a period
        

if __name__ == "__main__":
    main()
