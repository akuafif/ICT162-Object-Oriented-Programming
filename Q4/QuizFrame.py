from tkinter import Event, Frame, IntVar, Radiobutton, Button, Label
from tkinter.scrolledtext import ScrolledText
from tkinter.constants import DISABLED, NORMAL, END, WORD
from QuizBank import QuizBank

class QuizFrame(Frame):
    """ QuizGUI is a subclass  of Frame class that contains all the UI functionality and logic of the quiz """
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.createWidgets()
        self.grid(row=0,column=0)

    def createWidgets(self) -> None:
        """ Loads the widget to the GUI. """        
        # Creating start Button and Labels        
        self.__frHeader = Frame(self)
        self.__btnStart =  Button(self.__frHeader, text='Start',command=self.startQuiz)
        self.__btnStart.bind('<Button-1>', self.startQuiz)
        self.__lblQuestion = Label(self.__frHeader, text='Question will appear here')
        self.__btnStart.grid(row=0,column=0)
        self.__lblQuestion.grid(row=1,column=0)
        
        # Creating radio buttons for answers Frame
        self.__frBodyRbtn = Frame(self)
        self.__answer = IntVar()
        self.__answer.set(2)
        self.__rbtnTrue = Radiobutton(self.__frBodyRbtn, text='Option 1', variable=self.__answer, value=1)
        self.__rbtnFalse = Radiobutton(self.__frBodyRbtn, text='Option 2', variable=self.__answer, value=0)
        self.__rbtnTrue.grid(row=0,column=0, pady=2)
        self.__rbtnFalse.grid(row=1,column=0, pady=2)
        
        # Creating Submit and Next button Frame
        self.__frBodyBtn = Frame(self)
        self.__btnSubmit = Button(self.__frBodyBtn, text='Submit')
        self.__btnSubmit.bind('<Button-1>', self.submitAnswer)
        self.__btnSubmit.config(state=DISABLED)
        self.__btnNext = Button(self.__frBodyBtn, text='Next',command=self.nextQuestion)
        self.__btnNext.bind('<Button-1>', self.nextQuestion)
        self.__btnNext.config(state=DISABLED)
        self.__btnSubmit.grid(row=0,column=0)
        self.__btnNext.grid(row=0,column=1)

        # Creating a Scrollable Text widget Frame
        self.__frBodyScl = Frame(self)
        self.__sclOutput = ScrolledText(self.__frBodyScl, width=50, height=7, wrap=WORD, state=NORMAL)
        self.__sclOutput.insert(END, f'Click start to begin quiz.')
        self.__sclOutput.config(state = DISABLED)
        self.__sclOutput.grid(row=0,column=0)

        # Positioning Frame in the grid 
        self.__frHeader.grid(row=0,column=0, pady=2)
        self.__frBodyRbtn.grid(row=1,column=0, pady=2)
        self.__frBodyBtn.grid(row=2,column=0)
        self.__frBodyScl.grid(row=3,column=0, pady=5, padx=5)
        
    def displayOutput(self, message: str, clearAll: bool) -> None:
        """ Prints the message to the scrollable text widget

        Args:
            message (str): the string to print
            clearAll (bool): True to clear the textbox before displaying the message, otherwise false
        """
        self.__sclOutput.config(state = NORMAL)
        if clearAll:
            self.__sclOutput.delete(1.0,END)
        self.__sclOutput.insert(END, message + '\n')
        self.__sclOutput.see(END)
        self.__sclOutput.config(state = DISABLED) 

    def startQuiz(self, event: Event) -> None:
        """ Starts the quiz and retrieve a random question.\n
            Disable the Start & Next button and enable Submit button. """
        if not DISABLED in event.widget.config('state'):
            self.__btnStart.configure(state = DISABLED)
            self.__btnSubmit.configure(state = NORMAL)
            self.__rbtnTrue.configure(text = 'True')
            self.__rbtnFalse.configure(text = 'False')

            self.__questionBank = QuizBank(totalQuestion=4)
            newQuestion = self.__questionBank.getNewQuestion()
            self.__lblQuestion.configure(text = f'Q{self.__questionBank.questionsAttemped}. {newQuestion}')
            self.displayOutput('Select answer and click submit.', True)
            
            self.__answer.set(2)

    def submitAnswer(self, event: Event) -> None:
        """ Checks the answer for the current question and display the result in the scrollable text area ."""
        if not DISABLED in event.widget.config('state'):
            if str(self.__answer.get()) in '01':
                self.__btnSubmit.configure(state = DISABLED)
                self.__btnNext.configure(state = NORMAL)

                # Python interpreter written in C. Using self.__answer.get(), 1 = true, 0 = false
                self.displayOutput(f'Question {self.__questionBank.questionsAttemped} {"correct!" if self.__questionBank.checkCureentAnswer(bool(self.__answer.get())) else "incorrect!"}', False)
            else:
                self.displayOutput(f'Please select answer for question {self.__questionBank.questionsAttemped}', False)

    def nextQuestion(self, event: Event) -> None:
        """ Retrieves a random question from the QuizBank object.\n
            After 4 questions, it will end the quiz. """
        if not DISABLED in event.widget.config('state'):
            if self.__questionBank.questionsAttemped == self.__questionBank.totalQuestion:
                    self.endOfQuiz()
            else:        
                self.__btnNext.configure(state = DISABLED)
                self.__btnSubmit.configure(state = NORMAL)

                newQ = self.__questionBank.nextQuestion()
                self.__lblQuestion.configure(text = f'Q{self.__questionBank.questionsAttemped}. ' + newQ)
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
        self.displayOutput(f'Quiz complete. Total {self.__questionBank.correctAnswers} answers correct.\nClick Start to attempt quiz again.', False)