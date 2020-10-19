quizzes = [ #collection (of dictionaries)
    {
    'question': 'Cho co may chan?',
    'choices': [
    '1 chan', 
    '4 chan', 
    '3 chan', 
    '2 chan'
    ],
    'rightChoice': 1
},
{
    'question': 'Ga co may chan?',
    'choices': [
    '1 chan', 
    '4 chan', 
    '3 chan', 
    '2 chan'
    ],
    'rightChoice': 3
},
{
    'question': 'Vit co may chan?',
    'choices': [
    '1 chan', 
    '4 chan', 
    '3 chan', 
    '2 chan'
    ],
    'rightChoice': 3
}
]
count = 0
for quiz in quizzes:
    def print_quiz():
        print(quiz['question'])
        for choice in range(len(quiz['choices'])):
            print(f'{choice+1}. {quiz["choices"][choice]}')

    choices = quiz["choices"]
    print_quiz()
    yourchoice = int(input('Enter your choice: ')) - 1
    if yourchoice == quiz['rightChoice']:
        print('Correct!')
        count +=1
    else:
        print('Wrong :(')
        your_result = count*100/len(quizzes)
        print('Your result: ', your_result, " %")



