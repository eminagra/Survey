my_data = open('Project_Python.txt', 'r')

def load_survey_data(file_path):
    """Load survey questions and answers from a text file."""
    questions = []
    answers = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                if line.startswith('Q:'):
                    questions.append(line[2:].strip())  # Remove 'Q:' prefix
                elif line.startswith('A:'):
                    answers.append(line[2:].strip())  # Remove 'A:' prefix
    return questions, answers

def conduct_survey(questions, answers):
    """Conduct a survey."""
    print("Welcome to the Survey!\n")
    for question, answer in zip(questions, answers):
        user_answer = input(f"{question} ")
        if user_answer.strip().lower() == answer.lower():
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is: {answer}")
    print("\nThank you for completing the survey!")

def main():
    file_path = 'Project_Python.txt'  # Path to the file containing survey questions and answers
    questions, answers = load_survey_data(file_path)
    conduct_survey(questions, answers)

if __name__ == "__main__":
    main()