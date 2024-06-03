my_data = open('Survey1.txt', 'r')
def data_from_file(my_data):
    'Function to return data from text file in a way to recognize lines as either question or options.'
    'Here are used .strip(), endswith() and startswith() functions to put them in respective categories.'
    questions_and_options = []
    current_question = None
    current_options = []

    for line in my_data:
        line = line.strip()
        if line:
            if line.endswith('?'):  # How to get a question
                if current_question:
                    questions_and_options.append((current_question, current_options))  # Adds each question together with its options
                    current_options = []
                current_question = line
            elif line.startswith('- '):  # How to get options
                current_options.append(line[2:])
    if current_question:
        questions_and_options.append((current_question, current_options))

    return questions_and_options

def survey():
    'Function to survey itself.'
    'For this loop is used while True statement to prove if answers are given corectly and to print message depending if input was valid or not. '

    questions_and_options = data_from_file(my_data)

    print('Welcome to this survey!')
    print('Here are the questions: \n')
    answers = []  # Collecting the answers for further analysis
    for question, options in questions_and_options:
        print('Question:', question)
        print('Options:', options)
        for option in options:
            print(f'- {option}')

        while True:
            answer = input('Your answer: \n').strip().capitalize()
            if answer in (options):
                answers.append(answer)

                break
            else:
                print('Your input is not valid! \n')

    print('Thank you for participating in this survey. We will use this data to improve our services! \n')
    return answers

def save_answers():
 # Function to save answers in separate file for further analysis. It will not work and I couldn't debug it :-(
    survey_answers = open('Survey_Answers.txt', 'w')
    for answer in answers:
        my_data.write(answers)

# Run the survey
answers = survey()
print('Answers: ', answers)
saved_answers = save_answers()
print('Answers saved to Survey_Answers.txt')