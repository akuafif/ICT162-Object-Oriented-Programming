from random import randint

class QuizBank:
    """ A Class that is reposible to store any quiz related data """
    def __init__(self) -> None:
        """ Constructor for QuizBank object """
        self.__currentQuestion = 0
        self.__correctAnswers = 0
        self.__questions =  [ ['Variable names cannot start with digit', True], \
                            ["x='1'+1 is a valid statement", False], \
                            ['= and == can be used interchangeably', False], \
                            ['logical operator and has higher precedence than or', True], \
                            ['String type is immutable', True], \
                            ['x,y = y, x swaps the values of x and y', True], \
                            ['2=x is a valid statement', False], \
                            ['Variable names can be 50 letters long', True] ]
        self.__totalQuestion = len(self.__questions)
    
    @property
    def currentQuestion(self) -> int:
        """ The current index in the question list.

        Returns:
            int: current index in the question list
        """
        return self.__currentQuestion

    @property
    def correctAnswers(self) -> bool:
        """ Returns the amount of question answered correctly

        Returns:
            bool: amount of question answered correctly
        """
        return self.__correctAnswers 
    
    
    def getTotalQuestion(self) -> int:
        """ Gets the total number of question.
        
        Returns:
            int: total number of question in the quiz.
        """
        return self.__totalQuestion 

    def getNewQuestion(self) -> str:
        """ Returns a new question.

        Returns:
            str: new question
        """
        self.__currentQuestion = randint(0, len(self.__questions)-1)
        return self.__questions[self.__currentQuestion][0]

    def checkCureentAnswer(self, answer: bool) -> bool:
        """ Checks and compare the current question answer with the answer in argument.

        Args:
            answer (bool): the answer to check with the correct answer

        Returns:
            bool: True if answer is correct, otherwise False
        """
        self.__correctAnswers += 1 if answer == self.__questions[self.__currentQuestion][1] else 0
        return answer == self.__questions[self.__currentQuestion][1] 

    def nextQuestion(self) -> str:
        """ Gets the next question in the list

        Returns:
            str: new question
        """
        # Remove the current question from the list
        del self.__questions[self.__currentQuestion]
        return self.getNewQuestion()
    
    def totalQuestionsAttemped(self) -> int:
        """ The number of question attempted. 

        Returns:
            int: number of question attempted
        """
        return (self.__totalQuestion - len(self.__questions)) + 1