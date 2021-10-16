from tkinter import Tk, Frame, IntVar, Radiobutton, Button, Label
from tkinter.scrolledtext import ScrolledText
from tkinter.constants import DISABLED, NORMAL, END, WORD
from QuizBank import QuizBank

class QuizGUI(Tk):
    """ MainWindow is a class that contains all the UI functionality and logic of the quiz """
    def __init__(self) -> None:
        Tk.__init__(self)
        
        self.createWidgets()
        self.spawnMiddleScreen()
        
        self.mainloop()

    def createWidgets(self) -> None:
        """ Loads the widget to the GUI. """
        self.title('Python Quiz - Done by Muhammad Afif Bin Hashim')

        # Creating start Button and Labels
        self.__tf = Frame(self)
        self.__btnStart =  Button(self.__tf, text='Start',command=self.startQuiz)
        self.__lblQuestion = Label(self.__tf, text='Question will appear here')
        
        # Creating radio buttons for answers
        self.__answer = IntVar()
        self.__answer.set(2)
        self.__rbtnTrue = Radiobutton(self.__tf, text='Option 1', padx = 20, variable=self.__answer, value=1)
        self.__rbtnFalse = Radiobutton(self.__tf, text='Option 2', padx = 20, variable=self.__answer, value=0)

        # Creating a Frame to be placed inside self.__tf
        # This frame is required to create more columns for the Submit and Next button
        self.__bf = Frame(self.__tf)
        self.__btnSubmit = Button(self.__bf, text='Submit',command=self.submitAnswer)
        self.__btnSubmit.config(state=DISABLED)
        self.__btnNext = Button(self.__bf, text='Next',command=self.nextQuestion)
        self.__btnNext.config(state=DISABLED)
        
        # Positioning the radio button in the grid of self.__br
        self.__btnSubmit.grid(row=0,column=0, padx=2, pady=2)
        self.__btnNext.grid(row=0,column=1, padx=2, pady=2)

        # Creating a Scrollable Text widget
        self.__sclOutput = ScrolledText(self.__tf, width=55, height=8, wrap=WORD, state=NORMAL)
        self.__sclOutput.insert(END, f'Click start to begin quiz.')
        self.__sclOutput.config(state = DISABLED)
        
        # Positioning widget in the grid
        self.__btnStart.grid(row=0,column=0, padx=5, pady=5)
        self.__lblQuestion.grid(row=1,column=0, padx=5)
        self.__rbtnTrue.grid(row=2,column=0, padx=5, pady=2)
        self.__rbtnFalse.grid(row=3,column=0, padx=5, pady=2)
        self.__bf.grid(row=4,column=0)
        self.__sclOutput.grid(row=5,column=0, padx=5, pady=5)
        
        # Pack them and set resizable to false
        self.__tf.pack()
        self.resizable(False, False) 

    def spawnMiddleScreen(self) -> None:
        """ Reposition the window to the middle of the screen """
        
        # Gets the requested values of the height and width.
        windowWidth = self.winfo_reqwidth()
        windowHeight = self.winfo_reqheight()
        
        # Gets both half the screen width/height and window width/height
        positionRight = int(self.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(self.winfo_screenheight()/2 - windowHeight)
        
        # Positions the window in the center of the page.
        self.geometry("+{}+{}".format(positionRight, positionDown))  
        
    def displayOutput(self, message: str, clearAll: bool) -> None:
        """ Prints the message to the scrollable text widget

        Args:
            message (str): the string to print
            clearAll (bool): True to clear the textbox, otherwise false
        """
        self.__sclOutput.config(state = NORMAL)
        if clearAll:
            self.__sclOutput.delete(1.0,END)
        self.__sclOutput.insert(END, message + '\n')
        self.__sclOutput.see(END)
        self.__sclOutput.config(state = DISABLED)

    def startQuiz(self) -> None:
        """ Starts the quiz and retrieve a random question.\nDisable the Start & Next button and enable Submit button. """
        self.__questionBank = QuizBank()
        
        self.__btnStart.configure(state = DISABLED)
        self.__btnSubmit.configure(state = NORMAL)
        self.__rbtnTrue.configure(text = 'True')
        self.__rbtnFalse.configure(text = 'False')

        self.__lblQuestion.configure(text = f'Q{self.__questionBank.totalQuestionsAttemped()}. ' + self.__questionBank.getNewQuestion())
        self.displayOutput('Select answer and click submit.', True)
        
        self.__answer.set(2)
        self._correctAnswer = 0

    def submitAnswer(self) -> None:
        """ Checks the answer for the current question and display the result in the scrollable text area ."""
        if str(self.__answer.get()) in '01':
            self.__btnSubmit.configure(state = DISABLED)
            self.__btnNext.configure(state = NORMAL)
            
            # Python is written in C. self.__answer.get() if 1 = true, 0 = false
            if self.__questionBank.checkCureentAnswer(bool(self.__answer.get())):
                self.displayOutput(f'Question {self.__questionBank.totalQuestionsAttemped()} correct!', False)
            else:
                self.displayOutput(f'Question {self.__questionBank.totalQuestionsAttemped()} incorrect!', False)

            if self.__questionBank.totalQuestionsAttemped() == self.__questionBank.getTotalQuestion():
                self.endOfQuiz()
        else:
            self.displayOutput(f'Please select answer for question {self.__questionBank.totalQuestionsAttemped()}', False)

    def nextQuestion(self) -> None:
        """ Retrieves a random question from the QuizBank object. """
        self.__btnNext.configure(state = DISABLED)
        self.__btnSubmit.configure(state = NORMAL)

        newQ = self.__questionBank.nextQuestion()
        self.__lblQuestion.configure(text = f'Q{self.__questionBank.totalQuestionsAttemped()}. ' + newQ)
        self.__answer.set(2)

    def endOfQuiz(self) -> None:
        """ End the quiz and reset the UI. """
        self.__btnNext.configure(state = DISABLED)
        self.__btnSubmit.configure(state = DISABLED)
        self.__btnStart.configure(state = NORMAL)
        
        self.__rbtnTrue.configure(text = 'Option 1')
        self.__rbtnFalse.configure(text = 'Option 2')
        self.__answer.set(2)
        
        self.__lblQuestion.configure(text = 'Question will appear here')
        self.displayOutput(f'Quiz completed. Total {self.__questionBank.correctAnswers} answers correct.\nClick Start to attempt again.', False)