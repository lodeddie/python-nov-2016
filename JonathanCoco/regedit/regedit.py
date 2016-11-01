
import re

def get_matching_words(regex):

    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
    return [word for word in words if re.search(regex, word)]

# All words that contain a "v"
print "all words that contain a v"
print get_matching_words(r'.v')

# all words that contain a double -"s"
print "all words  that contain a double  s"
print get_matching_words(r'.ss')

# all words that starts with a "c"
print "all words that start with a c"
print get_matching_words(r'^c')

# all words that end with an "e"
print "all words that end with an e"
print get_matching_words(r'e$')

# all words that conttain "b" and character, then another "b"
print "all words that contain b any charater, then another b"
print get_matching_words(r'b.b')

print "all words that contain a b another letter than b again"
print get_matching_words(r'b\wb')

print "all words that contain a b any number of characters including 0 then another b"
print get_matching_words(r'b.+b')

# all words that include all five vowels in order
print "all words that include all five vowels in order"
print get_matching_words(r'a+\w*e+\w*i+\w*o\w*u+')

print "all words that only use letters in regular expression"
print get_matching_words(r'[r+]*[e+]*[g+]*[u+]*[l+]*[a+]*[x+]*[p+]*[p+]*')


# all words that include a double letter
print "all words with a double letter"
print get_matching_words(r'\w{2}')
