class answer_check:
    def __init__(self,question,options,correct_answer):
        self.question       = question
        self.options        = options
        self.correct_answer = correct_answer
    def answer_evaluation(self,answer):
        return self.correct_answer==answer

class main:
    def __init__(self,list):
        self.list              = list
        self.score             = 0
        self.numberOfQuestions = 0
    def show_question(self):
        return self.list[self.numberOfQuestions]
    def main_func(self):
        p = self.show_question()
        print(f'Question {self.numberOfQuestions+1}-) {p.question}')

        for i in p.options:
            print("-",i)
        answer = input('Enter Your Answer: ')
        self.check(answer)
        self.NumberOfQuestions()
    def check(self,answer):
        k = self.show_question()
        if k.answer_evaluation(answer):
            self.score+=1
        self.numberOfQuestions+=1
    def NumberOfQuestions(self):
        if self.numberOfQuestions==len(self.list):
            self.show_score()
        else:
            print(f"{50*'*'}{self.numberOfQuestions+1}/{len(self.list)}{50*'*'}")
            self.main_func()
            
            
    def show_score(self):
        print(f'Game Over... Score: {self.score}')
        
q1=answer_check('How many legs do cats have ?',['1','2','3','4'],'4')
q2=answer_check('Which fruit is red in color?',['Lemon','Strawberry','Mandarin','Melon'],'strawberry')
q3=answer_check('Which Is The World\'s Largest Mountain?',['Mount Ararat','Olympios','Everest','Alps'],'everest')


question_list=[q1,q2,q3]
p=main(question_list)
p.NumberOfQuestions()