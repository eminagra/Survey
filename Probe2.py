my_data = open('Survey.txt', 'r')
def questions(survey):
    """Extract questions from a survey file."""
    questions = []
    for line in survey:
        questions.append(line.strip())
    return questions


def main():
    file_path = 'Survey.txt'  # Path to the survey file
    with open(file_path, 'r') as survey_file:
        survey_questions = questions(survey_file)

    # Print the questions for testing
    for idx, question in enumerate(survey_questions, 1):
        print(f"Question {idx}: {question}")


if __name__ == "__main__":
    main()
