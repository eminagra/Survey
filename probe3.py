my_data = open('Survey1.txt', 'r')

def load_survey_data(file):
    """Load survey questions and options from an already opened file."""
    questions_with_options = []
    current_question = None
    current_options = []

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
    for question, options in questions_with_options:
        print(question)
        print("Options:")
        for option in options:
            print(f"- {option}")
        user_answer = input("Your answer: ").strip().capitalize()  # Convert to title case
        print(f"Your answer to '{question}': {user_answer}\n")

def main():
    file_path = 'Survey1.txt'  # Path to the file containing survey questions and options
    with open(file_path, 'r') as file:
        questions_with_options = load_survey_data(file)
    present_survey(questions_with_options)

if __name__ == "__main__":
    main()



