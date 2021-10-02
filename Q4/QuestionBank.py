from random import randint

class QuestionBank:
    _questionBank =  [ ['Variable names cannot start with digit', True], \
                        ["x='1'+1 is a valid statement", False], \
                        ['= and == can be used interchangeably', False], \
                        ['logical operator and has higher precedence than or', True], \
                        ['String type is immutable', True], \
                        ['x,y = y, x swaps the values of x and y', True], \
                        ['2=x is a valid statement', False], \
                        ['Variable names can be 50 letters long', True] ]

    def __init__(self) -> None:
        self._index = 0
        self._currentQuestion = 0
        self._correctAnswers = 0
        self._questions = type(self)._questionBank.copy() 

    @classmethod
    def getTotalQuestion(cls) -> int:
        return len(cls._questionBank)

    @property
    def index(self) -> None:
        return self._index
    
    @property
    def currentQuestion(self) -> int:
        return self._currentQuestion

    @property
    def correctAnswers(self) -> int:
        return self._correctAnswers 

    def getNewQuestion(self) -> str:
        self._index += 1
        self._currentQuestion = randint(0, len(self._questions)-1)
        return f'Q{self._index}. ' + str(self._questions[self._currentQuestion][0])

    def getAnswer(self, questionNo: int) -> bool:
        return self._questions[questionNo][1]

    def checkAnswer(self, answer: bool) -> bool:
        self._correctAnswers += 1 if answer == self.getAnswer(self.currentQuestion) else 0
        return answer == self.getAnswer(self.currentQuestion)

    def nextQuestion(self) -> str:
        del self._questions[self._currentQuestion]
        return self.getNewQuestion()

    def reset(self):
        self.__init__()