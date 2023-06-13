import cv2
import tkinter as tk
from PIL import Image, ImageTk

class WebcamDatasetCreator:
    def __init__(self, root):
        self.root = root
        self.camera = cv2.VideoCapture(0)

        self.photo_count1 = 0
        self.photo_count2 = 0

        self.create_gui()

    def create_gui(self):
        self.root.title("Webcam Dataset Creator")

        # Create buttons
        button1 = tk.Button(self.root, text="Save to Folder 1", command=self.save_to_folder1)
        button1.pack()

        button2 = tk.Button(self.root, text="Save to Folder 2", command=self.save_to_folder2)
        button2.pack()

        # Create image label
        self.image_label = tk.Label(self.root)
        self.image_label.pack()

        self.show_frame()

    def show_frame(self):
        _, frame = self.camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Resize frame to fit in the GUI
        frame = cv2.resize(frame, (640, 480))

        # Convert the frame to ImageTk format
        image = Image.fromarray(frame)
        image_tk = ImageTk.PhotoImage(image)

        # Update the image label
        self.image_label.configure(image=image_tk)
        self.image_label.image = image_tk

        # Repeat the process
        self.root.after(10, self.show_frame)

    def save_to_folder1(self):
        ret, frame = self.camera.read()
        if ret:
            self.photo_count1 += 1
            filename = f"folder1/photo{self.photo_count1}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Saved photo to {filename}")

    def save_to_folder2(self):
        ret, frame = self.camera.read()
        if ret:
            self.photo_count2 += 1
            filename = f"folder2/photo{self.photo_count2}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Saved photo to {filename}")

root = tk.Tk()
app = WebcamDatasetCreator(root)
root.mainloop()
