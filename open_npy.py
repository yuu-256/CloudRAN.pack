### THIS SCRIPT IS USED TO OPEN THE .NPY FILES AND DISPLAY THE IMAGES
### IMPORT LIBRARIES ###
import sys
import numpy as np
import matplotlib.pyplot as plt

### FUNCTIONS ###
# Display the images
def display_images(data,layer):
    # Display the images
    plt.imshow(data[layer,:,:],cmap='gray')
    plt.colorbar()
    plt.show()

# Display the path
def display_path(data):
    # Get the path from the data
    path = np.sum(data,axis=0)

    # Display the path
    plt.imshow(path)
    plt.show()


if __name__ == '__main__':

    # Check the number of arguments
    if len(sys.argv) != 2:
        print('Usage: python3 open_npy.py <output_file>')
        sys.exit(1)

    # Get output file path as an argument
    output_file = sys.argv[1]

    # Load the .npy file
    data = np.load(output_file)

    # Display the images
    display_images(data,0)
    display_path(data)
