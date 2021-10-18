import tkinter as tk
from QuizFrame import QuizFrame

def main() -> None:
    """ This method will create a root window and load the frame from QuizGUI and pack it. 
        This approach can help to add borders, frames, menubar without touching the Quiz Frame. """
    root = tk.Tk()
    root.title('Python Quiz - Done by Muhammad Afif Bin Hashim')
    root.resizable(False, False) 
    QuizFrame(root).pack()
    root.mainloop()

if __name__ == "__main__":
    main()