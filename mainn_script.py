my_data = open('Project_Python.txt', 'r')


for lines in my_data:
  survey_questions.append(lines.strip())
  if lines.endswith('?'):
     lines = survey_questions # I need to pop one question at a time

  elif lines.startswith('1.' or '2.' or '3.' or '4.'):
      survey_answers.append(lines.strip()) # I need to enumerate answers and to pop one answer at a time



question_1 = input('Are you opting for University degree')
if question_1 == 'Yes':
    print('Please answer also to the next question')
else :
    print('')
#function

def survey_questions():
    for lines in my_data:
        survey_questions.append(lines.strip())
        if lines.endswith('?'):
            lines = survey_questions.pop(lines)  # I need to pop one question at a time

def survey_answers():
   for lines in my_data:
    survey_answers.append(lines.strip()) # I need to enumerate answers and to pop one answer at a time
    if enumerate(lines.startswith(1 or 2 or 3 or 4)):
     lines = survey_answers.pop(lines)


#while not survey_is_done():
    input('Enter your answer here: ')
    #if answer = 'Yes'
    #else
        #print('Not eligibile for survey')
#print(survey_questions)
#print(survey_answers)



# Main loop



# Main loop

