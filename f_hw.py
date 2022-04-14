from PIL import Image
import warnings

def get_obj_file(FileName):
    try:
        img = Image.open(FileName)
    except FileNotFoundError:
        print("Error! Cannot open file:", FileName)
        return -1
    
    return img

def glue_horizontally(InputFile1, InputFile2, OutputFile):
    img1 = get_obj_file(InputFile1)
    img2 = get_obj_file(InputFile2)

    if(img1 == -1 or img2 == -1): return -1

    # get sizes of input image
    w1, h1 = img1.size
    w2, h2 = img2.size

    if(h1 != h2):
        warnings.warn("Images have different size! One photo will be cropped.")

    # size of new image
    width = w1+w2
    height = min(h1, h2)

    NewImage = Image.new('RGB', (width, height))

    x_offset = 0
    NewImage.paste(img1, (x_offset, 0))
    x_offset += w1
    NewImage.paste(img2, (x_offset, 0))

    NewImage.save(OutputFile)

    img1.close()
    img2.close()
    NewImage.close()
    
    # success
    return 1


def main():
    InputFile1 = input("Input first  image: ")
    InputFile2 = input("Input second image: ")
    OutputFile = input("Input output  file: ")

    glue_horizontally(InputFile1, InputFile2, OutputFile)


def AutoTest():
    k = glue_horizontally("AutoTestFile1.jpeg", "AutoTestFile2.jpeg", "AutoTestOutput.jpeg")
    
    if k == -1:
        return 0
    
    out = Image.open("AutoTestOutput.jpeg")
    w, h = out.size
    out.close()

    if w == 900 and h == 900: return 1
    else: return 0


if(AutoTest() == 0):
    print("AutoTest failed.")
else:
    main()