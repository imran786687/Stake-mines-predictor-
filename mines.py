import hashlib
import random

def get_nonce():
    rand_val = random.random()
    if rand_val < 0.50:
        return 1
    else:
        return 2

def generate_grid(num_mines, client_seed, server_seed, nonce):
    combined_seed = f"{client_seed}{server_seed}{nonce}"
    grid_size = 5
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
    
    # Generate a hash from the combined seed
    hash_val = hashlib.sha256(combined_seed.encode()).hexdigest()
    
    # Convert the hash to a list of integers
    int_values = [int(hash_val[i:i+2], 16) for i in range(0, len(hash_val), 2)]
    
    # Place mines and gems
    positions = [(i, j) for i in range(grid_size) for j in range(grid_size)]
    random.shuffle(positions)
    
    for i in range(num_mines):
        if i < len(positions):
            x, y = positions[i]
            grid[x][y] = '💣'
    
    for i in range(num_mines, len(positions)):
        if i < len(positions):
            x, y = positions[i]
            grid[x][y] = '💎'
    
    return grid

def print_grid(grid):
    for row in grid:
        print(' '.join(row))

def main():
    num_mines = int(input("Enter the number of mines (between 1 and 24): "))
    if not (1 <= num_mines <= 24):
        print("Invalid number of mines.")
        return
    
    client_seed = input("Enter the active client seed: ")
    server_seed = input("Enter the active server seed: ")
    
    nonce = get_nonce()
    
    print(f"Selected nonce: {nonce}")
    
    grid = generate_grid(num_mines, client_seed, server_seed, nonce)
    print("\nGenerated Grid:")
    print_grid(grid)

if __name__ == "__main__":
    main()
