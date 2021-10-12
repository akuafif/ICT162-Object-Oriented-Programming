from random import randint

class QuizBank:
    """ A Class that is reposible to store any quiz related data """
    def __init__(self) -> None:
        """ Constructor for QuizBank object """
        self._index = 1
        self._currentQuestion = 0
        self._correctAnswers = 0
        self._questions = [ ['Variable names cannot start with digit', True], \
                        ["x='1'+1 is a valid statement", False], \
                        ['= and == can be used interchangeably', False], \
                        ['logical operator and has higher precedence than or', True], \
                        ['String type is immutable', True], \
                        ['x,y = y, x swaps the values of x and y', True], \
                        ['2=x is a valid statement', False], \
                        ['Variable names can be 50 letters long', True] ]
        self._totalQuestion = len(self._questions)

    @property
    def index(self) -> int:
        """ The number of question attempted. 

        Returns:
            int: the number of question attempted
        """
        return self._index
    
    @property
    def currentQuestion(self) -> int:
        """ The current question index in the list.

        Returns:
            int: the current question index in the question list
        """
        return self._currentQuestion

    @property
    def correctAnswers(self) -> bool:
        """ Returns the amount of question answered correctly

        Returns:
            bool: the amount of question answered correctly
        """
        return self._correctAnswers 
    
    
    def getTotalQuestion(self) -> int:
        """ Gets the total number of question.
        
        Returns:
            int: the number of question in the quiz.
        """
        return self._totalQuestion 

    def getNewQuestion(self) -> str:
        """ Returns a new question.

        Returns:
            str: the new question
        """
        self._currentQuestion = randint(0, len(self._questions)-1)
        return self._questions[self._currentQuestion][0]

    def getAnswer(self, questionNo: int) -> bool:
        """ Get the correct answer based on the question number.

        Args:
            questionNo (int): the question number

        Returns:
            bool: the correct answer of the question number
        """
        return self._questions[questionNo][1]

    def checkCureentAnswer(self, answer: bool) -> bool:
        """ Checks and compare the current question answer with the answer in argument.

        Args:
            answer (bool): the answer to check with the correct answer

        Returns:
            bool: True if answer is correct, otherwise False
        """
        self._correctAnswers += 1 if answer == self.getAnswer(self.currentQuestion) else 0
        return answer == self.getAnswer(self.currentQuestion)

    def nextQuestion(self) -> str:
        """ Gets the next question in the list

        Returns:
            str: the new question
        """
        # Remove the current question from the list
        self._index += 1
        del self._questions[self._currentQuestion]
        return self.getNewQuestion()