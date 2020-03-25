from PIL import Image
import urllib.request

URL = 'https://upload.wikimedia.org/wikipedia/commons/e/ed/Raccoon_%28Procyon_lotor%29_2.jpg'

with urllib.request.urlopen(URL) as url:
    with open('temp.jpg', 'wb') as f:
        f.write(url.read())

img = Image.open('temp.jpg')