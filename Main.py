

#x = raw_input("Please enter a sentence:   ")


class mySentence:

    def __init__(self , sentence_string):
        self.sentence_string = sentence_string

    def change_string(self):
        self.sentence_string = raw_input()
        return self.sentence_string

    def number_of_chars(self , sentence_string):
        x = len(sentence_string)
        print ("The Sentence has %d characters") % (x)
        return x

    def number_of_consonants (self , sentence_string):
        letter_array = list((sentence_string).lower())
        index = 0
        vowel = 0
        consonant = 0
        space = 0
        while index < len(letter_array):
            if letter_array[index] == 'a':
                vowel += 1
                index += 1
            elif  letter_array[index] == 'e':
                vowel += 1
                index += 1
            elif letter_array[index] == 'i':
                vowel += 1
                index += 1
            elif letter_array[index] == 'o':
                vowel += 1
                index += 1
            elif letter_array[index] == 'u':
                vowel += 1
                index += 1
            elif letter_array[index] == " ":
                index += 1
                space += 1
            else:
                consonant += 1
                index += 1
        print "The number of vowels are %d" % vowel
        print "The number of consonants are %d" % consonant
        print "The number of spaces are %d" % space



S1 = mySentence("Hello")
S1.change_string()
print S1.sentence_string

S1.number_of_chars(S1.sentence_string)
S1.number_of_consonants(S1.sentence_string)














