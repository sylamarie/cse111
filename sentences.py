import random

def get_determiner(quantity):
    if quantity == 1:
        words = ['a', 'one', 'the']
    else:
        words = ['some', 'many', 'the']
    word = random.choice(words)
    return word

def get_noun(quantity):
    if quantity == 1:
        words = ['bird', 'boy', 'car', 'cat', 'child', 'dog',
                 'girl', 'man', 'rabbit', 'woman']
    else:
        words = ['birds', 'boys', 'cars', 'cats', 'children',
                 'dogs', 'girls', 'men', 'rabbits', 'women']
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    if tense == 'past':
        words = ['drank', 'ate', 'grew', 'laughed', 'thought',
                 'ran', 'slept', 'talked', 'walked', 'wrote']
    elif tense == 'present':
        if quantity == 1:
            words = ['drinks', 'eats', 'grows', 'laughs', 'thinks',
                    'runs', 'sleeps', 'talks', 'walks', 'writes']
        else:
            words = ['drink', 'eat', 'grow', 'laugh', 'think',
                     'run', 'sleep', 'talk', 'walk', 'write']
    elif tense == 'future':
        words = ['will drink', 'will eat', 'will grow', 'will laugh', 'will think',
                 'will run', 'will sleep', 'will talk', 'will walk', 'will write']
    else:
        return None 
  
    word = random.choice(words)
    return word

def get_preposition():
    words = ['about', 'above', 'across', 'after', 'along',
    'around', 'at', 'before', 'behind', 'below',
    'beyond', 'by', 'despite', 'except', 'for',
    'from', 'in', 'into', 'near', 'of',
    'off', 'on', 'onto', 'out', 'over',
    'past', 'to', 'under', 'with', 'without']

    word = random.choice(words)
    return word 

def get_adjective():
    words = ['happy', 'sad', 'tall', 'short',
            'angry', 'brave', 'calm', 'eager', 'fierce', 'gentle']
    
    word = random.choice(words)
    return word

def get_adverb():
    words = ['quickly', 'slowly', 'happily',
            'sadly', 'angrily', 'bravely', 'calmly', 'eagerly', 'fiercely', 'gently']
    
    word = random.choice(words)
    return word

def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    prepositional_phrase = f'{preposition} {determiner} {noun}'
    return prepositional_phrase

def make_sentence(quantity, tense):
    determiner1 = get_determiner(quantity)
    adjective1 = get_adjective()
    noun1 = get_noun(quantity)
    prepositional_phrase1 = get_prepositional_phrase(quantity)
    adverb = get_adverb()
    verb = get_verb(quantity, tense)
    determiner2 = get_determiner(quantity)
    adjective2 = get_adjective()
    noun2 = get_noun(quantity)
    prepositional_phrase2 = get_prepositional_phrase(quantity)

    sentence = f'{determiner1.capitalize()} {adjective1} {noun1} {prepositional_phrase1} {adverb} {verb} {determiner2} {adjective2} {noun2} {prepositional_phrase2}.'
    return sentence

print(make_sentence(1, 'past'))
print(make_sentence(1, 'present'))
print(make_sentence(1, 'future'))
print(make_sentence(2, 'past'))
print(make_sentence(2, 'present'))
print(make_sentence(2, 'future'))