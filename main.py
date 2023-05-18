import sys
from PIL import Image,ImageOps
def main():
    in_file,out_file=chek_argv()
    check_file(in_file, out_file)

def check_file(in_file,out_file):

    try:

        shirt=Image.open("shirt.png")
        size=shirt.size
        file=Image.open(in_file)
        file=ImageOps.fit(file,size)
        file.paste(shirt, shirt)
        file.save(out_file,Save_all=True)

    except FileNotFoundError:
        sys.exit()

def chek_argv():
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    in_format=sys.argv[1].split('.')[1]
    out_format=sys.argv[2].split('.')[1]
    if not(in_format==out_format):
        sys.exit("Input and output have different extension")
    elif not(in_format.endswith("png") or in_format.endswith("jpg") or in_format.endswith("jpeg")):
        sys.exit("Invalid input")
    elif not(out_format.endswith("png") or out_format.endswith("jpg") or out_format.endswith("jpeg")):
        sys.exit("Invalid output")

    return sys.argv[1],sys.argv[2]



if __name__ == "__main__":
    main()
