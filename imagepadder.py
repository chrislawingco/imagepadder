import os
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
from PIL import Image

## FUNCTIONS ---------------------------------------------------------------------------
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
    images = eInput.get().replace('"', "")
    outputPath = eOutput.get().replace('"', "")

    if (images.strip() == "" and outputPath.strip() == ""):
        tk.messagebox.showerror("Empty input/output error", "Make sure you have selected input files and an output folder.")
        return
    elif (images.strip() == ""):
        tk.messagebox.showerror("Empty input error", "Make sure you have selected input files.")
        return
    elif (outputPath.strip() == ""):
        tk.messagebox.showerror("Empty output error", "Make sure you have selected an output folder.")
        return


    topVal = eTop.get()
    leftVal = eLeft.get()
    rightVal = eRight.get()
    bottomVal = eBottom.get()

    # Make sure all values are integers
    try:
        topVal = int(topVal)
        leftVal = int(leftVal)
        rightVal = int(rightVal)
        bottomVal = int(bottomVal)
    except ValueError:
        tk.messagebox.showerror("Value error", "All values must be whole numbers.")
        return

    # Split list of images into their individual paths
    imagePaths = tuple(images.split(','))

    # Pad each image
    for path in imagePaths:
        padImage(path, outputPath, topVal, leftVal, rightVal, bottomVal)

    tk.messagebox.showinfo("Success", f"Your images have been saved to {outputPath}.")


# Utility functions
def padImage(imagePath, outputPath, top, left, right, bottom):
    # Open image and add the height/width that needs to be padded
    image = Image.open(imagePath)
    newHeight = image.height + top + bottom
    newWidth = image.width + left + right

    # Creating a new transparent image with the padding added
    paddedImage = Image.new("RGBA", (newWidth, newHeight), (0, 0, 0, 0))

    # Pasting the image to the padded image starting from the where the left and top padding end
    paddedImage.paste(image,(left, top))

    # Creating the save path and save the image
    try:
        baseFileName = os.path.basename(image.filename).split(".")[0]
        savePath = f"{outputPath}/{baseFileName}.png"
        paddedImage.save(savePath)
    except:
        tk.messagebox.showerror("Saving error", "There was an error saving your image.")
        return



## INTERFACE ---------------------------------------------------------------------------
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



