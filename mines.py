import hashlib
import random

def generate_random(seed):
    """Generate a random number generator with a given seed."""
    return random.Random(seed)

def hash_seed(seed):
    """Hash the seed using SHA-256 to produce a consistent hash."""
    return hashlib.sha256(seed.encode('utf-8')).hexdigest()

def get_positions(seed, num_boxes, num_mines):
    """Generate positions for mines based on seed and number of mines."""
    rng = generate_random(seed)
    positions = list(range(num_boxes))
    rng.shuffle(positions)
    return positions[:num_mines]

def print_board(board, rows, cols):
    """Print the board in a grid format."""
    for i in range(rows):
        print(" ".join(board[i * cols:(i + 1) * cols]))

def main():
    num_boxes = 25
    num_rows = 5
    num_cols = 5
    print("Welcome to the Mine Predictor!")
    
    # Input number of mines
    num_mines = int(input(f"Enter the number of mines (between 1 and {num_boxes - 1}): "))
    if not (1 <= num_mines < num_boxes):
        print(f"Invalid number of mines. It must be between 1 and {num_boxes - 1}.")
        return

    # Input seeds
    client_seed = input("Enter the client seed: ")
    server_seed = input("Enter the server seed (hashed): ")
    
    # Verify server seed is a valid hash
    if not len(server_seed) == 64 or not all(c in "0123456789abcdef" for c in server_seed):
        print("Invalid server seed format. It should be a 64-character hexadecimal string.")
        return

    # Generate hash for the client seed
    client_seed_hash = hash_seed(client_seed)
    
    # Combine client seed hash with server seed to form the final seed
    final_seed = client_seed_hash + server_seed
    
    # Get positions for mines
    mine_positions = get_positions(final_seed, num_boxes, num_mines)
    
    # Create board
    board = ['💎'] * num_boxes
    for pos in mine_positions:
        board[pos] = '💣'
    
    # Print the board
    print_board(board, num_rows, num_cols)

if __name__ == "__main__":
    main()
