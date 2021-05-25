# Multiple Choice Questions program

class Question:
    """ Question class to model multiple choice question.
    For each question there will be a prompt and answer
    """

    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "A highlight table uses which pre-attentive attribute to identify patterns or correlation in data?\n(a)	Position\n(b) Color\n(c) Size\n(d) Shape\n\n",
    "Putting a continuous pill on columns would draw what on the canvas?\n(a) A color legend\n(b) Field labels\n(c) An axis\n(d) A header\n\n",
    "Which actions are executed AFTER dimension filters in Tableau's order of operations (query pipeline)?\n(a) Data Source Filters\n(b) FIXED Expressions\n(c) Context Filters\n(d) INCLUDE/EXCLUDE Expressions\n\n "
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "d")
]


def run_test(questions):
    """
    Function to run the multiple choice test
    """
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("You got " + str(score) + "/" + str(len(questions)) + " Correct")


if __name__ == '__main__':
    run_test(questions)
