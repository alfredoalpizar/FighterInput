from flask import Flask, request, render_template
import base64
import requests
import os
import sys
from PIL import Image


os.chdir(os.path.dirname(os.path.realpath(__file__)))
app = Flask(__name__)
client_id = '7d1a7fbd90843cb'
headers = {"Authorization": "Client-ID "+client_id}
uploadURL= "https://api.imgur.com/3/image"



@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/submit', methods=["POST"])
def submit():
    #checkb = int(request.form['checkb'])
    size = int(request.form['size'])

    comboinput = request.form['inputs'].strip().upper()
    images = []

    skip = False

    for index, c in enumerate(comboinput):
        if not skip:
            if c == '1':
                images.append(Image.open('static/1-96px.png').convert('RGBA'))
                skip=False
            elif c == '2':
                images.append(Image.open('static/2-96px.png').convert('RGBA'))
                skip=False
            elif c == '3':
                images.append(Image.open('static/3-96px.png').convert('RGBA'))
                skip=False
            elif c == '4':
                images.append(Image.open('static/4-96px.png').convert('RGBA'))
                skip=False
            elif c == '5':
                images.append(Image.open('static/5-96px.png').convert('RGBA'))
                skip=False
            elif c == '6':
                images.append(Image.open('static/6-96px.png').convert('RGBA'))
                skip=False
            elif c == '7':
                images.append(Image.open('static/7-96px.png').convert('RGBA'))
                skip=False
            elif c == '8':
                images.append(Image.open('static/8-96px.png').convert('RGBA'))
                skip=False
            elif c == '9':
                images.append(Image.open('static/9-96px.png').convert('RGBA'))
                skip=False
            elif c == ',':
                images.append(Image.open('static/comma-96px.png').convert('RGBA'))
                skip=False
            elif c == 'L':
                images.append(Image.open('static/L-96px.png').convert('RGBA'))
                skip=False
            elif c == 'M':
                images.append(Image.open('static/M-96px.png').convert('RGBA'))
                skip=False
            elif c == 'H':
                images.append(Image.open('static/H-96px.png').convert('RGBA'))
                skip=False
            elif c == 'S':
                images.append(Image.open('static/S-96px.png').convert('RGBA'))
                skip=False
            elif c == 'A':
                if comboinput[index+1] == '1':
                    images.append(Image.open('static/A1-96px.png').convert('RGBA'))
                else:
                    images.append(Image.open('static/A2-96px.png').convert('RGBA'))
                skip=True

    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGBA', (total_width, max_height),(0, 0, 0, 0))

    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset, 0), mask=im)
        x_offset += im.size[0]

    new_im.save('test1.png', format='png')

    if size == 24:
        sz=total_width/4, size
        im=Image.open('test1.png').convert('RGBA')
        im.thumbnail(sz, Image.ANTIALIAS)
        im.save('result.png', format='png')
        os.remove('test1.png')

    elif size == 48:
        sz = total_width / 2, size
        im = Image.open('test1.png').convert('RGBA')
        im.thumbnail(sz, Image.ANTIALIAS)
        im.save('result.png', format='png')
        os.remove('test1.png')
    elif size == 98:
        os.rename("test1.png", "result.png")

    image = open('result.png', 'rb')
    image_read = image.read()
    image_64_encode = base64.encodebytes(image_read)

    payload = {
        'image': image_64_encode
    }
    #r = requests.post(uploadURL, data=payload, headers=headers)
    #data =r.json()
    #print(data)
    #os.remove('result.png')
    #return data["data"]["link"]
    return 'testing'
if __name__ == '__main__':
    app.run()
