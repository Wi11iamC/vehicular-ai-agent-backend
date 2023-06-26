import requests
import os

def main():
    API_URL = 'http://localhost:8000/rgb/'
    image_path = os.path.abspath("data/rgb_sample1.png")
    print((image_path))
    # Open the image file in binary mode
    with open(image_path, 'rb') as image_file:
        files = {'image_url': image_file}

        response = requests.post(API_URL, files=files)

        if response.status_code == 201:
            print('RGB sensor image created successfully')
        else:
            print('Failed to create RGB sensor image')

    return 0



if __name__ == '__main__':
    main()
