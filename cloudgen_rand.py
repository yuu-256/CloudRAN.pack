### Random cloud field generator, based on MCMC(Markov Chain Monte Carlo) method and EXP-RAN model.
### This is random version of cloudgen.py, which generates a random cloud field (no correlation between grids).

### IMPORT LIBRARIES ###
import sys
import numpy as np

### MAIN FUNCTION ###
if __name__ == '__main__':
    
    # Check the number of arguments
    if len(sys.argv) != 3:
        print('Usage: python3 cloudgen.py <output_file> <seed>')
        sys.exit(1)

    # Get output file path as an argument, and seed
    output_file = sys.argv[1]
    seed = int(sys.argv[2])

    # Set the random seed
    np.random.seed(seed)

    # Parameters setting
    grid_shape = (10, 100, 100)   # Field shape (i, j, k)
    z0 = 0.55                    # Decorrelation distance
    scaling_factor = 3          # Scaling factor
    max_iterations = 1         # Maximum number of iterations
    
    # Initialize the cloud field
    cloud_field = np.random.rand(*grid_shape)  # Define the initial cloud field

    # Write this to numpy file
    np.save(output_file, cloud_field)
