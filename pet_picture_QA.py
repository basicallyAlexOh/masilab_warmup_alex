#################################################################
# The data_dir variable is the only input allowed to your code. 
# Do not modify any file names in the image directory.
data_dir = "./MASI_pets"
# Add your code below.
#################################################################


import pandas as pd
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np
from collections import Counter

# Image Class
# Main purpose for organization and useful for consistency
class Image:
    def __init__(self, filename):
        self.name = filename
        self.petName = filename.split('.')[0].split('_')[0]
        self.owner = filename.split('.')[0].split('_')[1]
        self.myImage = cv2.imread(data_dir + '/' + filename)
        self.height = self.myImage.shape[0]
        self.width = self.myImage.shape[1]
        self.aspectRatio = self.width / self.height
        self.totalPixels = self.width * self.height

    def getDictionary(self):
        myDict = {'Name': self.name,
                  'Height': self.height,
                  'Width': self.width,
                  'Size': self.totalPixels,
                  'Aspect Ratio': self.aspectRatio,
                  'Pet Name': self.petName,
                  'Owner Initials': self.owner
                  }
        return myDict



def main():
    #############################
    #          TASK 1           #
    #############################
    image_list = [] # holds image objects
    for filename in os.listdir(data_dir):
        ext = filename.split('.')[1]
        if ext == 'jpg' or ext == 'jpeg':
            image_list.append(Image(filename))

    myDict = {'Name': [],
              'Height': [],
              'Width': [],
              'Size': [],
              'Aspect Ratio': [],
              'Pet Name': [],
              'Owner Initials': []
              }

    for myImage in image_list:
        tempDict = myImage.getDictionary()
        for key in myDict:
            myDict[key].append(tempDict[key])


    df = pd.DataFrame(myDict)
    df.sort_values(['Size','Pet Name'], inplace=True)
    df.to_csv('out.txt', encoding='utf-8', index=False, sep='\t')


    print(df.to_string())



    #############################
    #          TASK 2           #
    #############################
    size_list = df['Size']
    ar_list = df['Aspect Ratio']
    count_list = Counter(zip(size_list,ar_list))

    # https://stackoverflow.com/questions/46700733/how-to-have-scatter-points-become-larger-for-higher-density-using-matplotlib
    # Allows for coinciding scatter plot points to appear as larger dots on the scatter plot
    sizes = [20*count_list[(x,y)] for x,y in zip(size_list,ar_list)]

    plt.scatter(size_list, ar_list, s=sizes)
    plt.xlabel('Size (Pixels)')
    plt.ylabel('Aspect Ratio (Unitless)')
    plt.title('Aspect Ratio vs. Size of Pet Pictures')
    plt.savefig('Aspect Ratio vs. Size.jpg')
    # plt.show()












if __name__ == "__main__":
   main()