'''
Writen by Viet Bui and only for myself need, this program can be adjusted by
your own need. \￣︶￣*\
use to convert sentences to
cool vibe code by just simply remove 'aeiou'
WATER --> WTR
'''

class RemoveAEIOU:
    def __init__(self, sentence):
        self.sentence = sentence
        self.converted = []
        for letter in self.sentence:
            self.converted.append(letter)
        self.valid = ['a', 'e', 'i', 'o', 'u']
        
    def convert(self):
        for i in range(len(self.converted) -1 , -1, -1):
            if self.converted[i].lower() in self.valid:
                self.converted.remove(self.converted[i])
        self.new = ''
        for letter in self.converted:
            self.new += letter
        return self.new
    def original(self):
        return self.sentence
    def __str__(self):
        return f'{self.new}'

def options():
    print('-------------------------')
    print('What option do you want?:')
    print('  1: Output the sentence')
    print('  2: Output the original')
    print('  3: Input another sentence')
    print('  4: End program')
    print('-------------------------')
    
def getOption():
    validOption = [1,2,3,4]
    option = input('Enter option: ')
    while not int(option) in validOption or int(option) < 1 or int(option) > 4:
        print('Invalid. Try again')
        option = input('Enter option: ')
    return int(option)
    
def main():
    inputSentence = input('Input: ')
    options()
    option = getOption()
    
    while option != 4:
        processedSentence = RemoveAEIOU(inputSentence)
        if option == 1:
            processedSentence.convert()
            if processedSentence == '':
                print('<empty>')
            else:
                print(processedSentence)
        elif option == 2:
            print(processedSentence.original())
        elif option == 3:
            inputSentence = input('Input: ')
        options()
        option = getOption()
        
if __name__ == '__main__':
    main()
    
        