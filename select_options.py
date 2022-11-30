#!/
from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint


style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})


questions = [
    {
        'type': 'checkbox',
        'message': 'Select elements to run',
        'name': 'elements',
        'choices': [
            Separator('= Choices ='),
            {
                'name': 'Pygame visualization'
            },
            {
                'name': 'terminal frame print'
            }
        ],
        'validate': lambda answer: 'Select an element.' \
            if len(answer) == 0 else True
    }
]

answers = prompt(questions, style=style)
#pprint(answers)

#open communication.txt
file = open("communication.txt", "w")
#write the answer in the file
num=0
if 'Pygame visualization' in answers['elements']:
    num+=1
if 'terminal frame print' in answers['elements']:
    num+=2
file.write(str(num))