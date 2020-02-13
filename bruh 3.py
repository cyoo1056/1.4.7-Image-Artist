from PIL import Image, ImageOps

basewidth = 560
baseheight = 560

im = Image.open('040517-97.jpg')
im = im.resize((basewidth, baseheight), Image.NEAREST)
im.save('family1_resized_image.jpg')

im = Image.open('_0025_P822_family_1117_003_E.jpg')
im = im.resize((basewidth, baseheight), Image.NEAREST)
im.save('family2_resized_image.jpg')

im1 = Image.open('family1_resized_image.jpg')
im2 = Image.open('family2_resized_image.jpg')
def get_image_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def get_image_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

get_image_h(im1, im1).save('newimage_h.jpg')
get_image_v(im1, im1).save('newimage_v.jpg')
get_image_h(im2, im2).save('newimage2_h.jpg')
get_image_v(im2, im2).save('newimage2_v.jpg')
get_image_h(im1, im2).save('newimage3_h.jpg')
get_image_v(im1, im2).save('newimage3_v.jpg')

def add_border(input_image, output_image, border, color = 0):
    im = Image.open(input_image)
    if isinstance(border, int) or isinstance(border, tuple):
        im = ImageOps.expand(im, border=border, fill=color)
    else:
        raise RuntimeError('Border is not an integer or tuple!')
    im.save(output_image)
if __name__ == '__main__':
    in_im = 'newimage3_h.jpg'
    add_border(in_im,
               output_image=('bordered_newimage3_h.png'),
               border=(50, 50, 50, 50), 
               color = 'gold')

im_orig = Image.open("bordered_newimage3_h.png")
im_orig.putalpha(255)

starwidth = 1220
starheight = 660
im = Image.open('6cr5pEaei.png')
im = im.resize((starwidth, starheight), Image.NEAREST)
im.save('starborder_resized_image.png')

im = Image.open('starborder_resized_image.png')
im = im.convert("RGBA")
datas = im.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

im.putdata(newData)
im.save("transparent_star.png", "PNG")

background = Image.open("bordered_newimage3_h.png")
foreground = Image.open("transparent_star.png")

background.paste(foreground, (0, 0), foreground)
background.save('finishedimage.png')