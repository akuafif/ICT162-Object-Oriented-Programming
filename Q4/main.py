import tkinter as tk
from tkinter import messagebox
from tkinter import *
from Question import Question

class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self._questionBank = None
        self._correctAnswer = 0

        self.title('Python Quiz - Done by Muhammad Afif Bin Hashim')

        self._window = Frame(self)
        self._btnStart =  Button(self._window, text="Start",command=self.startQuiz)
        self._btnStart.grid(row=0,column=0, padx=5, pady=5, columnspan=2, sticky="n")
        self._lblQuestion = Label(self._window, text="Question will appear here")
        self._lblQuestion.grid(row=1,column=0, padx=5, columnspan=2, sticky="nwe")

        self._answer = IntVar()
        self._answer.set(0)
        self._radTrue = Radiobutton(self._window, text="Option 1", padx = 20, variable=self._answer, value=1)
        self._radTrue.grid(row=2,column=0, padx=5, pady=5,rowspan=1, columnspan=2,  sticky="n")
        self._radFalse = Radiobutton(self._window, text="Option 2", padx = 20, variable=self._answer, value=2)
        self._radFalse.grid(row=3,column=0, padx=5, pady=5,rowspan=1, columnspan=2,  sticky="n")

        self._btnSubmit = Button(self._window, text="Submit",command=self.submitAnswer)
        self._btnSubmit.grid(row=4,column=0, padx=5, pady=5, sticky="ne") 
        self._btnSubmit['state'] = tk.DISABLED
        self._btnNext = Button(self._window, text="Next",command=self.nextQuestion)
        self._btnNext.grid(row=4,column=1, padx=5, pady=5, sticky="nw") 
        self._btnNext['state'] = tk.DISABLED

        self._textArea = Text(self._window, height = 11, width = 60, state='normal')
        self._textArea.insert(END, f'Click start to begin quiz.\n')
        self._textArea.grid(row=5,column=0, columnspan=2, padx=5, pady=5, sticky="nwe") 
        self._textArea.config(state = DISABLED)

        self._window.grid(row = 0, column = 0, sticky = "n")
        
        self.spawnMiddleScreen()

        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)

    def spawnMiddleScreen(self):
        # Gets the requested values of the height and width.
        windowWidth = self.winfo_reqwidth()
        windowHeight = self.winfo_reqheight()
        
        # Gets both half the screen width/height and window width/height
        positionRight = int(self.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(self.winfo_screenheight()/2 - windowHeight)
        
        # Positions the window in the center of the page.
        self.geometry("+{}+{}".format(positionRight, positionDown))  

    def startQuiz(self):
        """ Disable the Start & Next button and enable Submit button.
        Retrieves a random question """
        self._btnStart.configure(state = DISABLED)
        self._btnSubmit.configure(state = NORMAL)

        self._questionBank = Question()
        self._textArea.config(state = NORMAL)
        self._textArea.delete('1.0', END)
        self._textArea.insert(END, 'Select answer and click submit.\n')
        self._correctAnswer = 0
        self._textArea.config(state = DISABLED)

        self._radTrue.configure(text = 'True')
        self._radFalse.configure(text = 'False')
        
        self._lblQuestion.configure(text = self._questionBank.getQuestion())
        self._answer.set(0)

    def submitAnswer(self):
        self._textArea.config(state = NORMAL)
        if str(self._answer.get()) in '12':
            self._btnSubmit.configure(state = DISABLED)
            self._btnNext.configure(state = NORMAL)

            answer = True if self._answer.get() == 1 else False

            if answer == self._questionBank.getAnswer():
                self._textArea.insert(END, f'Question {self._questionBank.index} correct!\n')
                self._correctAnswer += 1    
            else:
                self._textArea.insert(END, f'Question {self._questionBank.index} incorrect!\n')

            if self._questionBank.index == Question.getTotalQuestion():
                self.endOfQuiz()
        else:
            self._textArea.insert(END, f'Please select answer for question {self._questionBank.index}\n')
                  
        self._textArea.config(state = DISABLED)

    def nextQuestion(self):
        self._btnNext.configure(state = DISABLED)
        self._btnSubmit.configure(state = NORMAL)

        self._lblQuestion.configure(text = self._questionBank.nextQuestion())
        self._answer.set(0)

    def endOfQuiz(self):
        self._btnNext.configure(state = DISABLED)
        self._btnSubmit.configure(state = DISABLED)
        self._btnStart.configure(state = NORMAL)
        
        self._radTrue.configure(text = 'Option 1')
        self._radFalse.configure(text = 'Option 2')
        self._answer.set(0)
        
        self._lblQuestion.configure(text = "Question will appear here")
        
        self._textArea.config(state = NORMAL)
        self._textArea.insert(END, f'Quiz completed. Total {self._correctAnswer} answers correct.\nClick Start to attempt again.\n')
        self._textArea.config(state = DISABLED)

def main():
    app = MainWindow()
    app.mainloop()

if __name__ == "__main__":
    main()