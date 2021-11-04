import requests


def main():
    img = requests.get('https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png')
    if img.status_code == 200:
        with open("sample.jpg", 'wb') as f:
            f.write(img.content)
        print('got file')


if __name__ == "__main__":
    main()
