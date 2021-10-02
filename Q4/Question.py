from random import randint

class Question:
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

        self._questions = type(self)._questionBank.copy() 

    @classmethod
    def getTotalQuestion(cls) -> int:
        return len(cls._questionBank)

    @property
    def index(self) -> None:
        return self._index

    def getQuestion(self) -> str:
        self._index += 1
        self._currentQuestion = randint(0, len(self._questions)-1)
        return f'Q{self._index}. ' + str( self._questions[self._currentQuestion][0] )

    def getAnswer(self) -> bool:
        return self._questions[self._currentQuestion][1]

    def nextQuestion(self) -> str:
        del self._questions[self._currentQuestion]
        return self.getQuestion()
