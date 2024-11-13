### Random cloud field generator, based on MCMC(Markov Chain Monte Carlo) method and EXP-RAN model.

### IMPORT LIBRARIES ###
import sys
import numpy as np


### FUNCTIONS ###
### calculate_alpha: calculate the correlation alpha corresponding to the distance
def calculate_alpha(distance, z0):
    return np.exp(-distance / z0)

### update_grid: update the cloud field
def update_grid(cloud_field, grid_shape, scaling_factor):
    # Initialize the updated cloud field
    updated_cloud_field = np.copy(cloud_field)

    # Define the neighbor range
    neighbor_range = range(-scaling_factor, scaling_factor + 1)

    for i in range(grid_shape[0]):
        for j in range(grid_shape[1]):
            for k in range(grid_shape[2]):
                neighbor_values = []
                
                # Search the neighbor grids
                for di in neighbor_range:
                    for dj in neighbor_range:
                        for dk in neighbor_range:
                            if di == 0 and dj == 0 and dk == 0:
                                continue  # Skip the center grid
                            
                            ni, nj, nk = i + di, j + dj, k + dk
                           
                            # Check the neighbor grid is within the field
                            if (0 <= ni < grid_shape[0] and
                                0 <= nj < grid_shape[1] and
                                0 <= nk < grid_shape[2]):
                                
                                distance = np.sqrt(di**2 + dj**2 + dk**2)
                                alpha = calculate_alpha(distance, z0)
                                rand_val = np.random.rand()
                                
                                # Accept the neighbor grid value if the random value is less than alpha
                                if rand_val < alpha:
                                    neighbor_values.append(cloud_field[ni, nj, nk])
                
                # Update the grid value if there are neighbor values
                if neighbor_values:
                    updated_cloud_field[i, j, k] = np.mean(neighbor_values)
                else:
                    updated_cloud_field[i, j, k] = np.random.rand()  # Randomly generate a new value

    return updated_cloud_field


### update_grid: update the cloud field
### Speed up the update_grid function by vectorizing the neighbor grid search
def update_grid_speed(cloud_field, grid_shape, scaling_factor, z0):
    updated_cloud_field = np.copy(cloud_field)

    # Calculate the offsets for the neighbor grids
    neighbor_range = range(-scaling_factor, scaling_factor + 1)
    offsets = np.array([(di, dj, dk) for di in neighbor_range for dj in neighbor_range for dk in neighbor_range if not (di == 0 and dj == 0 and dk == 0)])

    # Calculate the correlation alpha for each neighbor grid
    distances = np.sqrt(np.sum(offsets**2, axis=1))
    alphas = calculate_alpha(distances, z0)

    # Update the cloud field
    for i in range(grid_shape[0]):
        for j in range(grid_shape[1]):
            for k in range(grid_shape[2]):
                neighbors = []

                for idx, (di, dj, dk) in enumerate(offsets):
                    ni, nj, nk = i + di, j + dj, k + dk

                    # Check the neighbor grid is within the field
                    if (0 <= ni < grid_shape[0] and 0 <= nj < grid_shape[1] and 0 <= nk < grid_shape[2]):
                        if np.random.rand() < alphas[idx]:  # Accept the neighbor grid value
                            neighbors.append(cloud_field[ni, nj, nk])

                # Update the grid value
                updated_cloud_field[i, j, k] = np.mean(neighbors) if neighbors else np.random.rand()

    return updated_cloud_field


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
    grid_shape = (3, 32, 32)   # Field shape (i, j, k)
    z0 = 5                    # Decorrelation distance
    scaling_factor = 1          # Scaling factor
    max_iterations = 1         # Maximum number of iterations
    
    # Initialize the cloud field
    cloud_field = np.random.rand(*grid_shape)  # Define the initial cloud field

    # Update the cloud field
    for _ in range(max_iterations):
        cloud_field = update_grid_speed(cloud_field, grid_shape, scaling_factor, z0)

    # Write this to numpy file
    np.save(output_file, cloud_field)
