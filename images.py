import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
from PIL import Image


# Button functions
def btnInput_click():
    files = tk.filedialog.askopenfilenames()
    filesString = ','.join(f'"{filepath}"' for filepath in files)
    eInput.delete(0, tk.END)
    eInput.insert(0, filesString)

def btnOutput_click():
    dir = tk.filedialog.askdirectory()
    dirString = f'"{dir}"'
    eOutput.delete(0, tk.END)
    eOutput.insert(0, dirString)

def btnPadImage_click():
    images = eInput.get()
    outputPath = eOutput.get()

    topVal = eTop.get()
    leftVal = eLeft.get()
    rightVal = eRight.get()
    bottomVal = eBottom.get()

    try:
        topVal = int(topVal)
        leftVal = int(leftVal)
        rightVal = int(rightVal)
        bottomVal = int(bottomVal)
    except ValueError:
        tk.messagebox.showerror("Value error", "All values must be whole numbers")

    imagePaths = tuple(images.split(','))
    for path in imagePaths:
        print(path)

    print(outputPath)





# tkinter window
window = tk.Tk()
window.title("Image Padder")

# Files Frame
fFiles = tk.Frame(window)
fFiles.pack()

# Inputs
lblInput = tk.Label(fFiles, text="Images")
eInput = tk.Entry(fFiles)
btnInput = tk.Button(fFiles, text="Select Files", command=btnInput_click)

lblInput.grid(row=1, column=0, sticky="E")
eInput.grid(row=1, column=1)
btnInput.grid(row=1, column=2)

# Output
lblOutput = tk.Label(fFiles, text="Output Folder")
eOutput = tk.Entry(fFiles)
btnInput = tk.Button(fFiles, text="Select Folder", command=btnOutput_click)

lblOutput.grid(row=2, column=0, sticky="E")
eOutput.grid(row=2, column=1)
btnInput.grid(row=2, column=2)

# Padding Values
fPadValues = tk.Frame(window)
# space    |   entry   |   space
# entry    |  square   |   entry
# space    |   entry   |   space
# Entries
eTop = tk.Entry(fPadValues, width=5)
eLeft = tk.Entry(fPadValues, width=5)
eRight = tk.Entry(fPadValues, width=5)
eBottom = tk.Entry(fPadValues, width=5)

eTop.insert(0, 0)
eLeft.insert(0, 0)
eRight.insert(0, 0)
eBottom.insert(0, 0)

canvas = tk.Canvas(fPadValues)
canvas.create_rectangle(0, 0, 90, 90, fill="maroon1")

x1,y1,x2,y2 = canvas.bbox("all")
width = x2-x1
height=y2-y1
canvas.configure(width=width, height=height)

eTop.grid(row=0, column=1)
eLeft.grid(row=1, column=0)
canvas.grid(row=1, column=1)
eRight.grid(row=1, column=2)
eBottom.grid(row=2, column=1)

fPadValues.pack()


# Pad Image Button
fPadButton = tk.Frame(window)

btnPadImage = tk.Button(fPadButton, text="Pad Image", command=btnPadImage_click)
btnPadImage.pack()

fPadButton.pack()






window.mainloop()


# img = Image.open("D:/Chris/Pictures/tom_laughing.jpg")
# img.show()



