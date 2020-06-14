
def object_filter(infile1, infile2, infile3, outfile):
    """Compare the 3 images and create a new one based on their common pixels"""
    file1 = open(infile1, "r")
    file2 = open(infile2, "r")
    file3 = open(infile3, "r")
    output = open(outfile, "w")
    
    #read metadata
    p1, dim1, max1 = scan_metadata(file1)
    p2, dim2, max2 = scan_metadata(file2)
    p3, dim3, max3 = scan_metadata(file3)
    
    #write metadata
    output.write(p1)
    for x in dim1:
        output.write(x)
        output.write(" ")
    output.write("\n")
    output.write(max1)

    #begin reading pixel data
    line1 = file1.readline()
    line2 = file2.readline()
    line3 = file3.readline()   

    while(len(line1) > 0):
        line1_list = line1.split()
        line2_list = line2.split()
        line3_list = line3.split()

        #find the values that match 2 out of 3
        commonList = find_common(line1_list, line2_list, line3_list)
        
        #write these to the file
        for x in commonList:
            output.write(x)
            output.write("   ")
        output.write("\n")
        
        #move on to the next line
        line1 = file1.readline()
        line2 = file2.readline()
        line3 = file3.readline()

    file1.close()
    file2.close()
    file3.close()
    output.close()
    
    pass
        
def shades_of_gray(infile, outfile):
    """Converts image to a greyscale version"""
    file = open(infile, "r")
    output = open(outfile, "w")
    
    #read metadata
    p1, dim1, max1 = scan_metadata(file)
    
    #write metadata
    output.write(p1)
    for x in dim1:
        output.write(x)
        output.write(" ")
    output.write("\n")
    output.write(max1)
    
    #get pixels in list form
    everyPixel = list_each_pixel(file)
    
    #change each pixel to grayscale by averaging the RGB values
    for p in everyPixel:
        rgb_avg = (int(p[0])+int(p[1])+int(p[2]))//3
        p[0] = p[1] = p[2] = str(rgb_avg)
        
    #write pixel data to file
    pixCount = 0  
    for i in range (0, int(dim1[1]), 1):
        linePixels = []
        for j in range(0, int(dim1[0]), 1):
            linePixels.append(everyPixel[pixCount])
            pixCount += 1
        for x in linePixels:
            output.write(x[0])
            output.write(" ")
            output.write(x[1])
            output.write(" ")
            output.write(x[2])
            output.write(" ")
        output.write("\n")
    
    file.close()
    output.close()
    
    pass
    
def horizontal_flip(infile, outfile):
    """Flips image horizontally"""
    file = open(infile, "r")
    output = open(outfile, "w")
    
    #read metadata
    p1, dim1, max1 = scan_metadata(file)
    
    #write metadata
    output.write(p1)
    for x in dim1:
        output.write(x)
        output.write(" ")
    output.write("\n")
    output.write(max1)
   
    #get pixels in list form
    everyPixel = list_each_pixel(file)
    
    #create line of pixels, flip it, then write to file
    pixCount = 0  
    for i in range (0, int(dim1[1]), 1):
        linePixels = []
        for j in range(0, int(dim1[0]), 1):
            linePixels.append(everyPixel[pixCount])
            pixCount += 1
        linePixels.reverse()
        for x in linePixels:
            output.write(x[0])
            output.write(" ")
            output.write(x[1])
            output.write(" ")
            output.write(x[2])
            output.write(" ")
        output.write("\n")
    
    file.close()
    output.close()
    
    pass
    
def scan_metadata(filename):
    """Reads the first three lines of metadata"""
    ptype = filename.readline()
    dim = filename.readline()
    max_value = filename.readline()
    dimensions = dim.split()

    return ptype, dimensions, max_value

def find_common(list1, list2, list3):
    """Determines which 2 images have the pixels in common"""
    if list1 == list2:
        return list1
    elif list1 == list3:
        return list1
    else:
        return list2

def list_each_pixel(file):
    """Reads all RGB values in file, then makes a list of lists of 3 each"""
    allNumbers = []
    allPixels = []
    
    #make list of all values
    for line in file:
        for value in line.split():
            allNumbers.append(value)
    
    #turn that into a list of pixel sub-lists
    for i in range(0, len(allNumbers), 3):
        onePixel = []
        onePixel.append(allNumbers[i])
        onePixel.append(allNumbers[i+1])
        onePixel.append(allNumbers[i+2])
        allPixels.append(onePixel)
        
    return allPixels