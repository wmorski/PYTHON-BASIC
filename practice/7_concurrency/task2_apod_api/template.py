import os
import time
import requests
from concurrent.futures import ThreadPoolExecutor

API_KEY = "UVk3mdbm4BKjx8jDxdg83e4n2AlKCFmFb2QN6dMg"
APOD_ENDPOINT = 'https://api.nasa.gov/planetary/apod'
OUTPUT_IMAGES = './output'


def get_apod_metadata(start_date: str, end_date: str, api_key: str) -> list:
    url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&start_date={start_date}&end_date={end_date}'
    response = requests.get(url)
    return response.json()


def download_image(element: dict):
    if element['media_type'] == 'image':
        image = requests.get(element['url']).content
        image_name = element['url'].split('/')[-1]
        with open(f'{OUTPUT_IMAGES}/{image_name}', 'wb') as image_file:
            image_file.write(image)


def download_apod_images(metadata: list):
    with ThreadPoolExecutor() as executor:
        executor.map(download_image, metadata)
    """
    Sequential Code (around 100 seconds):
    for element in metadata:
        print(element)
        if element['media_type'] == 'image':
            image = requests.get(element['url']).content
            image_name = element['url'].split('/')[-1]
            with open(f'{OUTPUT_IMAGES}/{image_name}', 'wb') as image_file:
                image_file.write(image)
    """


def main():
    start_getting_metadata = time.time()
    metadata = get_apod_metadata(
        start_date='2021-08-01',
        end_date='2021-09-30',
        api_key=API_KEY,
    )
    print("Time of getting metadata:", time.time() - start_getting_metadata)
    download_apod_images(metadata=metadata)


if __name__ == '__main__':
    if not os.path.exists(OUTPUT_IMAGES):
        os.makedirs(OUTPUT_IMAGES)

    for file in os.listdir(OUTPUT_IMAGES):
        os.remove(os.path.join(OUTPUT_IMAGES, file))

    start = time.time()
    main()
    print("Time needed for the program:", time.time() - start)
