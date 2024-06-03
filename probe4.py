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
    for question, options in questions_with_options:
        print(question)
        print("Options:")
        for option in options:
            print(f"- {option}")

        while True:
            answer = input('Your answer: ').strip().capitalize()
            if question == "Question 1: Are you above the age of 18?":
                if answer == "Yes":
                    print("Please proceed to the next question.\n")

                elif answer == "No":
                    print("You are not eligible for this survey.\n")
                    break
                else:
                    print("Your input is invalid.\n")
            elif question == "Question 2: Are you opting for University degree?":
                if answer == "Yes":
                    print("Please answer the next question.\n")

                elif answer == "No":
                    print("You are not eligible for this survey.\n")
                    break
                else:
                    print("Your input is invalid.\n")
            elif question == "Question 3: Have you considered College of Medicine as an option for you":
                if answer == "Yes" or answer == "No":
                    print("Thank you for participating. College of Medicine will use this data to prepare its facilities for newcomers.\n")
                    break
                else:
                    print("Your input is invalid.\n")
                    # No need to break here as we want to keep prompting for a valid input

def main():
    file_path = 'Survey1.txt'  # Path to the file containing survey questions and options
    questions_with_options = load_survey_data(file_path)
    present_survey(questions_with_options)

if __name__ == "__main__":
    main()
