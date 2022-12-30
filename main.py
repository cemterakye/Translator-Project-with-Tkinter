from tkinter import *
import pandas
import random
from tkinter import messagebox
BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- Data------------------------------- #
try:
    data = pandas.read_csv("words_to_learn.csv",header = 0)
    english = data["English"].to_list()
    turkish = data["Turkish"].to_list()
    zipped_words = list(zip(english,turkish))
    words_to_learn = data.copy()

except FileNotFoundError:
    data = pandas.read_csv("data.csv",header = 0)
    english = data["English"].to_list()
    turkish = data["Turkish"].to_list()
    zipped_words = list(zip(english,turkish))
    if len(zipped_words) == 0:
        messagebox.showinfo("Congrats! You have learned all words!",title = "Well Done!")
    words_to_learn = data.copy()
    words_to_learn.to_csv("words_to_learn.csv")

word_list = ""

# ----------------------------Functions------------------------------- #
def random_english_word_right():
    global word_list,words_to_learn
    if len(word_list) == 0:
        messagebox.showinfo("Congrats! You have learned all words!",title = "Well Done!")
    word_list = random.choice(zipped_words)
    word = word_list[0]
    canvas.itemconfig(image_to_change, image=image)
    canvas.itemconfig(label_word,text = word,fill = "black")
    canvas.itemconfig(label_title, text="English",fill = "black")
    window.after(3000, func=random_turkish_word)

    words_to_learn = words_to_learn[words_to_learn["English"] != word]
    words_to_learn.to_csv("words_to_learn.csv",index = False)


def random_english_word():
    global word_list
    word_list = random.choice(zipped_words)
    word = word_list[0]
    canvas.itemconfig(image_to_change, image=image)
    canvas.itemconfig(label_word,text = word,fill = "black")
    canvas.itemconfig(label_title, text="English",fill = "black")
    window.after(3000, func=random_turkish_word)


def random_english_word_wrong():
    global word_list
    word_list = random.choice(zipped_words)
    word = word_list[0]
    canvas.itemconfig(image_to_change, image=image)
    canvas.itemconfig(label_word,text = word,fill = "black")
    canvas.itemconfig(label_title, text="English",fill = "black")
    window.after(3000, func=random_turkish_word)

def random_turkish_word():
    canvas.itemconfig(image_to_change,image = image2)
    canvas.itemconfig(label_word,text = word_list[1],fill = "white")
    canvas.itemconfig(label_title, text="Turkish",fill = "white")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Translator English-Turkish")
window.config(padx =50, pady = 50,bg = BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526)
image = PhotoImage(file="card_front.png")
image2 = PhotoImage(file="card_back.png")
image_to_change = canvas.create_image(400,263,image=image)
canvas.config(bg = BACKGROUND_COLOR,highlightthickness = 0)
label_title = canvas.create_text(400,150,text = "Title",font = ("Ariel",40,"italic"))
label_word = canvas.create_text(400,263,text = "Word",font = ("Ariel",60,"bold"))
canvas.grid(row = 1,column = 1,columnspan = 2)


#Button1
cross_image = PhotoImage(file = "wrong.png")
button1 = Button(image = cross_image,command = random_english_word_wrong)
button1.grid(row = 2,column = 1)

#Button2
check_image = PhotoImage(file = "right.png")
button2 = Button(image = check_image,command = random_english_word_right)
button2.grid(row = 2,column = 2)

random_english_word()

window.after(3000,func = random_turkish_word)

window.mainloop()