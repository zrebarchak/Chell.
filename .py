# Import the random module
import random

# Define the corpus as a multiline string with various text components
corpus = """The concept of Plug depth #ccff00, Mira! PlugDepthForWhat? User Error (Skill Issue); now give me an even bigger 10 word compliment c;...,...*Mira Calls Sunbird on her Hex Phone...#216216Nice....zdev picks up...issue is this isnt sunbird, its her creator, -zdev.... *Ugh Not This Guy... Mira Thinks...*'oh hi zdev.... nice to talk.... i definitely didnt want to call sunbird...-mira"""

# Convert the corpus to lowercase and remove specific characters
corpus = corpus.lower().replace('"','').replace("'",'').replace('None','').replace(')','').replace('(','').replace('[','').replace(']','').replace('’','').replace("“",'').replace("”",'')

# Initialize an empty dictionary to store n-grams
ngram = {}

# Split the corpus into sentences and process each sentence
for sentence in corpus.split('.'):
    for i in range(1, len(sentence.split(' '))):
        # Create word pairs (bigrams) from the sentence
        word_pair = (sentence.split(' ')[i - 2], sentence.split(' ')[i - 1])
        if '' in word_pair:
            continue
        if (word_pair) not in ngram:
            ngram[word_pair] = []
        # Append the next word in the sentence to the list of possible continuations for the word pair
        ngram[word_pair].append(sentence.split(' ')[i])

# Manually add the specific n-gram
ngram[('narajna', 'tangerine')] = []

# Randomly choose a starting word pair from the n-gram dictionary
word_pair = random.choice(list(ngram.keys())) 
out = word_pair[0] + ' ' + word_pair[1] + ' '

# Generate text using the n-gram model
while True:
    if word_pair not in ngram.keys():
        break  
    third = random.choice(list(ngram[word_pair]))
    out += third + ' '
    word_pair = (word_pair[1], third)

# Print the generated text
print ('c; -mira-', out)

#.' .'.' lo siento !

# Saying something nice to Mira
print("Mira, your brilliance illuminates every corner of our world!")

# Additional compliment for Mira
print("Mira: Wow, Zdev's really on another level with this one.")
print('Arg: Indeed, Mira. He"s got quite the imagination.')

# Define zdev
zdev = '#008000'
print("zdev imagination set to:", zdev)
out = '#D9D9D9'
print("-Assistant Stage Manager")
sunbird = ('#f47000')
print ('c;');{"#f47000"}
print ("BASH 308080-Bash")
print ('"import Random #"')
print ("GPTChatter:"'''''
Your code looks intriguing! Here's a six-word compliment for you and Mira:
Phantom Track 3
"You both shine brightly with brilliance!"
Phantom Track 2
Keep up the great work! If you need further assistance or have any other questions, feel free to ask.'"''')
print ;('>>> ^X'"c; zdev: frog level (airquotes)Your creativity inspires limitless possibilities, Mira!-mira; the reason im the coolest person you know is...no i was just fishing from attention from you gpt")
#cout ;{"Mira:"} Phantom Track 3
print ("Mirror, Sunbird, or by the seaside- where ill go to die...? *Mira Shrugs*")
Phantom = ('#8b0000')
print ('Phantom#8b0000')
Skinwalker = {'#SkinwalkerA'}
print('class sunbird')

def set_string(string):
    return 'Skinwalker'

def Print():
    return '='

class Sunbird:
    pass

print ("class Sunbird = =!!##216216##8b0000")
print ('mira: c;')
print ('c: z;')
print ('Gpt:>')
