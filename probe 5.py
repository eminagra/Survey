def load_survey_data(file_path):
    """Load survey questions and options from a text file."""
    questions_with_options = []
    current_question = None
    current_options = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:  # Skip empty lines
                if line.endswith('?'):
                    if current_question:
                        questions_with_options.append((current_question, current_options))
                        current_options = []  # Reset options for the next question
                    current_question = line
                elif line.startswith('- '):
                    current_options.append(line[2:])  # Exclude the '- ' prefix

    # Append the last question and options
    if current_question:
        questions_with_options.append((current_question, current_options))

    return questions_with_options

def present_survey(questions_with_options):
    """Present survey questions with options to the user."""
    print("Welcome to the Survey!\n")
    answers = []
    for question, options in questions_with_options:
        print(question)
        print("Options:")
        for option in options:
            print(f"- {option}")

        while True:
            answer = input('Your answer: ').strip().capitalize()
            if answer in ["Yes", "No"]:
                answers.append(answer)  # Store user's answer
                print('Thank you for your answer!')
                break
            else:
                print("Your input is invalid. Please enter 'Yes' or 'No'.\n")

    return answers

def main():
    file_path = 'Survey1.txt'  # Path to the file containing survey questions and options
    questions_with_options = load_survey_data(file_path)
    answers = present_survey(questions_with_options)
    print('Answers: ', answers)

if __name__ == "__main__":
    main()
