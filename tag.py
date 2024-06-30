import csv
import os

import httpx
import ollama
from tqdm import tqdm

def get_images(img_dir, tags_file):
    with open(tags_file, 'r') as f:
        stored_list = list(csv.reader(f))

    file_extensions = ['.jpg' ,'.png']
    img_list = []

    for file in os.listdir(img_dir):
        _, file_extension = os.path.splitext(file)
        file_path = img_dir + file

        if (
                file_extension.lower() not in file_extensions or
                any(file_path in x for x in stored_list)
            ):
            continue

        img_list.append(file)

    return img_list

def process_images(img_dir, tags_file, img_list, model='llava:7b'):
    if not img_list:
        print()

    check_model_installed(model)

    prompt = (
        'List only the keywords used to describe this image.'
        'Separate keywords with a comma delimiter.'
    )

    for img in tqdm(img_list, desc='Processing Images'):
        img_path = img_dir + img
        response = ollama.chat(
            model=model,
            messages=[{
                'role': 'user',
                'content': prompt,
                'images': [img_path]
            }]
        )
        img_tags = response['message']['content']
        img_tags = ','.join([item.strip() for item in img_tags.split(',')])

        with open(tags_file, 'a',) as f:
            csv.writer(f).writerow([img_path, img_tags])

def check_model_installed(model):
    try:
        ollama.list()
    except httpx.ConnectError as e:
        print('Could not cannot to ollama server.', end=' ')
        print('Please ensure it is running with `ollama serve`.')
        exit()

    if model not in [model['name'] for model in ollama.list()['models']]:
        print(f'This program uses the {model} model ', end='')
        print('but it is not currently installed.')

        options = {'y': 'yes', 'n': 'no'}

        options_string = ''
        for option in options.keys():
            options_string += f'[{option}]{options[option][1:]} '

        input_value = input(f'Would you like to install it? {options_string}')
        while input_value not in list(options.keys()):
            input_value = input(f'Invalid input. {options_string}')

        if input_value == 'y':
            print(f'Downloading {model} model...')
            ollama.pull(model)
            print('Done!\n')
        else:
            print(f'{model} model will not be installed. Exiting...')
            exit()
