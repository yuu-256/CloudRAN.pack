import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.cm as cm

### READ NUMBERS FROM GIVEN LINE NUMBER ###
def read_numbers_from_line(filename, line_number):
    with open(filename, 'r') as f:
        # allocate all lines in the file
        lines = f.readlines()
        
        # get the target line
        target_line = lines[line_number - 1]
        
        # space-separated numbers in the target line
        numbers = [content for content in target_line.split()]

    return numbers

# Usage
# filename = 'sample.txt'
# line_number = 5  # 5th line
# numbers = read_numbers_from_line(filename, line_number)
# print(numbers)  # Output [123, 456, 789]


if __name__ == '__main__':
     
    upflux = np.array([])

    fnm = '../out_test32'
    line_number = [i for i in range(1474,6590,5)]
    upflux_0 = np.array([])
    upflux_60 = np.array([])
    for line_number in line_number:
        numbers = read_numbers_from_line(fnm, line_number)
        ### Append the numbers to the list
        upflux_0 = np.append(upflux_0, float(numbers[3]))
        upflux_60 = np.append(upflux_60, float(numbers[4]))
    upflux_0 = np.reshape(upflux_0, (32, 32))
    upflux_60 = np.reshape(upflux_60, (32, 32))

    print(upflux_0)
    print(upflux_60)

    # Scale the values
    flux_min = np.min(upflux_0)
    flux_max = np.max(upflux_0)
    upflux_0_norm = (upflux_0 - flux_min)/(flux_max - flux_min) * 255
    print(flux_min, flux_max)
    print(upflux_0_norm)

    # Set colorbar
    plt.imshow(upflux_0_norm, cmap=cm.gray)
#    plt.imshow(upflux, cmap=cm.gray)
    plt.colorbar()
    plt.show()

    # Plotting
    # pil_img = Image.fromarray(upflux,mode='F')
    # pil_img = pil_img.resize((upflux.shape[1]*100, upflux.shape[0]*100))
    # pil_img.save('sample/out_split/out_test.tiff')
