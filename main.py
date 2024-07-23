# Libraries
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy as np
from keras.models import load_model

# Load your model
model = load_model('traffic_classifier.h5')  # Path to your model

# Classes of trafic signs
classes = { 0:'Speed limit (20km/h)',
            1:'Speed limit (30km/h)',
            2:'Speed limit (50km/h)',
            3:'Speed limit (60km/h)',
            4:'Speed limit (70km/h)',
            5:'Speed limit (80km/h)',
            6:'End of speed limit (80km/h)',
            7:'Speed limit (100km/h)',
            8:'Speed limit (120km/h)',
            9:'No passing',
            10:'No passing veh over 3.5 tons',
            11:'Right-of-way at intersection',
            12:'Priority road',
            13:'Yield',
            14:'Stop',
            15:'No vehicles',
            16:'Veh > 3.5 tons prohibited',
            17:'No entry',
            18:'General caution',
            19:'Dangerous curve left',
            20:'Dangerous curve right',
            21:'Double curve',
            22:'Bumpy road',
            23:'Slippery road',
            24:'Road narrows on the right',
            25:'Road work',
            26:'Traffic signals',
            27:'Pedestrians',
            28:'Children crossing',
            29:'Bicycles crossing',
            30:'Beware of ice/snow',
            31:'Wild animals crossing',
            32:'End speed + passing limits',
            33:'Turn right ahead',
            34:'Turn left ahead',
            35:'Ahead only',
            36:'Go straight or right',
            37:'Go straight or left',
            38:'Keep right',
            39:'Keep left',
            40:'Roundabout mandatory',
            41:'End of no passing',
            42:'End no passing veh > 3.5 tons' }

# Initialise GUI
top = tk.Tk()
# Window dimensions (800x600)
top.geometry('800x600')
# Window title
top.title('Traffic sign classification')
# Window background color
top.configure(background='#CDCDCD')
# Window label
label = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))
# Sign image
sign_image = Label(top)


# Function to classify image
def classify(file_path):
    global label_packed
    # Open the image file path
    image = Image.open(file_path)
    # Resize the image
    image = image.resize((30, 30))
    # Inserts a new axis that will appear at the axis position in the expanded array shape
    image = np.expand_dims(image, axis=0)
    # Convert to np array
    image = np.array(image)
    # Make prediction
    pred = model.predict([image])[0]
    pred_index = np.argmax(pred)
    sign = classes[pred_index]
    print(sign)
    label.configure(foreground='#011638', text=sign)

# Function to show the "classify" button
def show_classify_button(file_path):
    # Create the button
    classify_b = Button(top, text="Classify Image", command=lambda: classify(file_path), padx=10, pady=5)
    # Configure button colors
    classify_b.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
    # Configure button place (location)
    classify_b.place(relx=0.79, rely=0.46)


# Function to upload image
def upload_image():
    try:
        # Path of the image
        file_path = filedialog.askopenfilename()
        # Open file path
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() * 2.25), (top.winfo_height() * 2.25)))
        im = ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass


# Create "Upload" button
upload = Button(top, text="Upload an image", command=upload_image, padx=10, pady=5)
# "Upload" button colors and font
upload.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
# Button location
upload.pack(side=BOTTOM, pady=50)
sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)
# Window title text
heading = Label(top, text="Know Your Traffic Sign", pady=20, font=('arial', 20, 'bold'))
# Window colors
heading.configure(background='#CDCDCD', foreground='#364156')
heading.pack()
top.mainloop()