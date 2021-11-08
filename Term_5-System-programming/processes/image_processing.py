from concurrent.futures import ProcessPoolExecutor
import concurrent.futures
import os
import time
from PIL import Image, ImageFilter


parent_dir_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
folder_path = os.path.join(parent_dir_path, 'threads', 'img')
img_names = [name for name in os.listdir(folder_path) if name.endswith(".jpg")]
img_paths = [os.path.join(folder_path, img_name) for img_name in os.listdir(folder_path) if img_name.endswith(".jpg")]

# print(folder_path)
# print(img_paths)
# print(img_names)


size = (1200, 1200)


def process_image(img_path):
    img_name = img_path.split('/')[-1]
    img = Image.open(img_path)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f'processed/{img_name}')
    print(f'{img_name} was processed')


if __name__ == '__main__':
    # 1 process processing
    start = time.time()

    for index, img_path in enumerate(img_paths):
        img_name = img_path.split('/')[-1]
        img = Image.open(img_path)
        img = img.filter(ImageFilter.GaussianBlur(15))
        img.thumbnail(size)
        img.save(f'processed/{img_name}')
        print(f'{img_name} was processed')

    finish = time.time()
    print(f'\nTime Processing images 1 process: {finish - start} s\n\n')

    # multiprocessing

    start = time.time()

    with ProcessPoolExecutor() as executor:
        executor.map(process_image, img_paths)

    finish = time.time()
    print(f'\nTime with multiprocessing: {finish - start} s')


