
# calculating using python: 
example_string = 'doesn\'t'
mult = 4 * 'asdf'




def fizzbuzz():
    for i in range(1, 100):
        if i%3 == 0 and i%5 == 0: 
            print('fizzbuzz')
        elif i%3 == 0:
            print('fizz')
        elif i%5 == 0: 
            print('buzz')
        else:
            print(i)
            
words = ['cat', 'mouse', 'dog', 'cow']
for word in words:
    print(word, len(word))
