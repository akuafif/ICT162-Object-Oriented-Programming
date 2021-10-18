from random import randint

class QuizBank:
    """ QuizBank class is a class that models one Quiz. """
    def __init__(self, totalQuestion: int) -> None:
        """ Constructor for QuizBank object 

        Args:
            totalQuestion (int): total number of questions
        """
        self.__questions =  [ ['Variable names cannot start with digit', True], \
                            ["x='1'+1 is a valid statement", False], \
                            ['= and == can be used interchangeably', False], \
                            ['logical operator and has higher precedence than or', True], \
                            ['String type is immutable', True], \
                            ['x,y = y, x swaps the values of x and y', True], \
                            ['2=x is a valid statement', False], \
                            ['Variable names can be 50 letters long', True] ]
        self.__currentQIndexPosition = 0
        self.__correctAnswers = 0
        self.__questionsAttemped = 0
        self.__totalQuestion = totalQuestion

    @property
    def correctAnswers(self) -> bool:
        """ Returns the amount of question answered correctly

        Returns:
            bool: amount of question answered correctly
        """
        return self.__correctAnswers 
    
    @property
    def questionsAttemped(self) -> int:
        """ The number of question attempted. 

        Returns:
            int: number of question attempted
        """
        return self.__questionsAttemped 
    
    @property
    def totalQuestion(self) -> int:
        """ Gets the total number of question.
        
        Returns:
            int: total number of question in the quiz
        """
        return self.__totalQuestion 

    def getNewQuestion(self) -> str:
        """ Returns a new question.

        Returns:
            str: new question
        """
        self.__questionsAttemped += 1
        self.__currentQIndexPosition = randint(0, len(self.__questions)-1)
        return self.__questions[self.__currentQIndexPosition][0]

    def checkCureentAnswer(self, answer: bool) -> bool:
        """ Checks and compare the current question answer with the answer in argument.

        Args:
            answer (bool): the answer to check with the correct answer

        Returns:
            bool: True if answer is correct, otherwise False
        """
        self.__correctAnswers += 1 if answer == self.__questions[self.__currentQIndexPosition][1] else 0
        return answer == self.__questions[self.__currentQIndexPosition][1] 

    def nextQuestion(self) -> str:
        """ Gets the next question in the list

        Returns:
            str: new question
        """
        # Remove the current question from the list
        del self.__questions[self.__currentQIndexPosition]
        return self.getNewQuestion()