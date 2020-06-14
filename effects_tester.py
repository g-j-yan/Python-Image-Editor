
from effects import object_filter, shades_of_gray, horizontal_flip


def main():
    print("Welcome to the PPM Image Editor!\n")
    print("Choose the effect to try...\n1)object filter\n2)shades of gray\n3)horizontal flip")
    
    selection = input("Enter the number to select: ")
    validity = True
    
    if "1" in selection:
        print("<OBJECT FILTER>")
        img1 = input("Provide the first filename: ")
        img2 = input("Provide the second filename: ")
        img3 = input("Provide the third filename: ")
    
        object_filter(img1,img2,img3, input("Provide the name of the output: "))
    elif "2" in selection:
        print("<SHADES OF GRAY>")
        img = input("Provide the filename: ")
        shades_of_gray(img, input("Provide the name of the output: "))
        
    elif "3" in selection:
        print("<HORIZONTAL FLIP>")
        img = input("Provide the filename: ")
        horizontal_flip(img, input("Provide the name of the output: "))
    
    else:
        print("Invalid selection! Run the editor again.")
        validity = False
        
    if validity:
        print("Done. Thanks for using the PPM Image Editor!")
        
#run main
main()