import csv
import os

from PIL import Image, ImageTk
from rapidfuzz import fuzz, process
from tkinter import Tk, Canvas, Label

def find_matches(tags_file, query, max_matches):
    with open(tags_file, 'r') as f:
        collection = list(csv.reader(f))
    collection_tags = [x[1] for x in collection]

    matches = process.extract(
        query=query,
        choices=collection_tags,
        scorer=fuzz.partial_ratio,
        limit=max_matches
    )

    matching_files = [collection[match[2]][0] for match in matches]
    scores = [match[1] for match in matches]

    return list(zip(matching_files, scores))

def display_matches(matches, num_cols):
    num_rows = len(matches) // num_cols

    root = Tk()

    canvas = Canvas(root, width=800, height=2400)
    # Ideally canvas would not be hard-coded:
    # - canvas to fit window
    # - vertical scrollbar
    canvas.pack()

    canvas_width = float(canvas.config('width')[4])
    image_width = canvas_width / num_cols

    for index, match in enumerate(matches):
        image_path, image_score = match

        col = index % num_cols
        row = index // num_cols

        image = Image.open(image_path)
        image = image.reduce(image.size[0] // int(image_width))
        image_width, image_height = image.size
        image = ImageTk.PhotoImage(image)

        location = (col * image_width, row * image_height)
        image_label = Label(canvas, image=image)
        image_label.image = image
        image_label.place(x=location[0], y=location[1])

        text = f'{os.path.basename(image_path)} ({image_score / 100:.2f})'
        text_label = Label(canvas, text=text, bg='white')
        text_label.place(x=location[0], y=location[1])

    root.mainloop()
