my_data = open('Project_Python.txt', 'r')

survey_questions = []
survey_answers = []

#function

def survey_questions():
    for lines in my_data:
        survey_questions.append(lines.strip())
        if lines.endswith('?'):
            lines = survey_questions  # I need to pop one question at a time

def survey_answers():
   for lines in my_data:
    survey_answers.append(lines.strip()) # I need to enumerate answers and to pop one answer at a time
    if enumerate(lines.startswith(1 or 2 or 3 or 4)):
     lines = survey_answers

print(survey_questions)
print(survey_answers)




# Main loop










