### IMPORT LIBRARIES ###
import numpy as np
import sys

### This function converts a numpy array to a text file with the following contents.
def npy_to_txt(npy_file, text_file):
    # Load the npy file
    data = np.load(npy_file)

    # Generate the output lines
    def generate_output_lines(data_slice):
        return [" ".join(f"{float(val):.3f}" for val in row) + "\n" for row in data_slice]

    ### Making POVs (32*32)
    list = np.array([])

    for i in np.arange(0.015625, 1.00, 0.03125):
        for j in np.arange(0.015625, 1.00, 0.03125):
            i = np.round(i,6)
            j = np.round(j,6)
            list = np.append(list, f'1 {i} {j}')

    def list_to_text(list):
        text_output = '\n'.join(list)
        return text_output

    pov_list = list_to_text(list)

    # Write the text file
    with open(text_file, 'w') as f:
        f.write("1  1  1  0    icont (Rayleigh, CKD, L(0), photon-info)\n")
        f.write("1  0  0  3  1  10  0  : ISOL INDA  INDG  imthd  ipol NDA NDS\n")
        f.write("2  0.0   60.0   : NA0 TH0\n")
        f.write("9  0.0 10.0 20.0 30.0  40.0  50.0  60.0 70.0 80.0 : NA1 TH1 (hemisphere)\n")
        f.write("2  0.0   60.0    : NFI  FI\n")
        f.write("0.5  0.7  wl-min -max\n")
        f.write("0.1  0.0  : GALB fow SW and LW spectral regions\n")
        f.write("6 3 : IATM NLN/ IPB\n")
        f.write("10 4 3 2\n")
        f.write("  0    0.98                  : IFRH TRH\n")
        f.write("  1    2     0.5E-4         : NPOLY ICN WLCN\n")
        f.write("  1    1                  : NCOMP CNPT\n")
        f.write("  1                         : MPTC\n")
        f.write("  1.0                       : VPTC\n")
        f.write("1  40000    : icycl np\n")
        f.write("32  32  1.0  1.0 : nx ny dx dy\n")
        f.write("0.0  fis\n")

    # Write the data slices
    for i, slice_data in enumerate(data):
        output_lines = generate_output_lines(slice_data)

        with open(text_file, 'a') as f:  # 'a'で追記モードにする
            f.write(f"1 {i+1}  ipoly lz/cconc(i,j,lz,ipoly) lower cloud layer\n")
            f.writelines(output_lines)

    # Write the POVs 
    with open(text_file, 'a') as f:
        f.write("1024 0 npv llr/llu rpv1 rpv2\n")
        f.writelines(pov_list)

    return

if __name__ == "__main__":
    # Get input and output file path as an argument
    if len(sys.argv) < 3:
        print("Usage: python mktext_input.py <npy_file> <text_file>")
        exit(1) # Exit with an error code

    fnm = sys.argv[1]
    output_fnm = sys.argv[2]

    npy_to_txt(fnm, output_fnm)
