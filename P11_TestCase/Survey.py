class AnonymousSurvey:
    """Collect anonymous answers to a survey question"""
    def __init__(self, question):
        '''Store a question and set default None to responses list'''
        self.question = question
        self.responses = []

    def show_question(self):
        '''Show the question'''
        print(f"Your question is: {self.question}")

    def store_results(self, new_result):
            self.responses.append(new_result)

    def show_results(self):
        print(f"Question: {self.question}")
        for response in self.responses:
            print(f"\t{response}")

""" my_question = AnonymousSurvey('Ferrari or Lamborghini?')
my_question.show_question()
print("Write your responses. Press 'q' anytime to quit")
while True:
    response = input("Write something: ")
    if response == 'q':
        break
    my_question.store_results(response)

if my_question.responses:
    print(f"Question: {my_question.question}")
    for res in my_question.responses:
        print(f"\t{res}")
else:
    print(f"Question: {my_question.question} hasn't the answers yet.") """