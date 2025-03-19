import PIL.Image

ASCII_CHARS = ["@","#","$","%","?","*","+",";",":",",","."]

# function to resize the input image
def resizeImage(image,new_width=100):
    width,height = image.size
    ratio = height/width
    new_height = int(new_width*ratio)
    resized_image = image.resize((new_width,new_height))
    return resized_image


# converting image to grey scale
def convertTogreyScale(image):
    grey_scaled_img = image.convert("L")
    return grey_scaled_img

# convert each pixel to ascii chars
def convertPixToAscii(image):
    pixels = image.getdata()    
    chars = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return chars

def main(new_width = 100):
    # Enter a valid image path
    path = input("Enter a image path:\n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path,'is not a valid pathname to an image.')    

    new_image_data = convertPixToAscii(convertTogreyScale(resizeImage(image=image)))

    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0,pixel_count,new_width))

    print(ascii_image)

    # save the img
    with open("ascii_img.txt",'w') as f:
        f.write(ascii_image)

if __name__ == "__main__":
    main()    