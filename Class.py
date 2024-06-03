
my_data = open('Survey1.txt', 'r')

def survey(questions_and_options)
    print('Welcome to this Survey on Education Path')

  answer = input('Are you above the age of 18? Answer with Yes or No! ')
  if answer == 'Yes':
     print('Thank you for taking part in this survey')
  elif answer == 'No':
     print('Sorry, you are not eligible to take this survey!')
  else:
     print('Your input is not valid')


def question_two():
    answer = input('Are you opting for University degree? Answer with Yes or No ')
    if answer == 'Yes':
        print('Please answer the next question!')
    elif answer == 'No':
        print('Sorry, you can not answer the next question!')
    else:
        print('Your input is not valid')

def question_three():
    answer = []

print(question_one)
print(question_two)

