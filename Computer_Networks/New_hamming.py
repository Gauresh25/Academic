def calculate_redundant_bits(data_bits):
    """Calculate the number of redundant bits needed."""
    r = 0
    while 2 ** r < data_bits + r + 1:
        r += 1
    return r


def get_hamming_positions(length):
    """Get positions of redundant and data bits in the Hamming code."""
    redundant_positions = [2 ** i for i in range(length.bit_length())]
    data_positions = [i for i in range(1, length + 1) if i not in redundant_positions]
    return redundant_positions, data_positions


def position_to_binary(position, total_bits):
    """Convert a position to its binary representation."""
    return format(position, f'0{total_bits}b')


def calculate_parity(data, check_position, total_bits):
    """Calculate parity for a given position."""
    count = 0
    for i in range(1, total_bits + 1):
        if i & check_position:  # Check if position should be included in parity calculation
            if data[total_bits - i]:  # Check if bit is 1
                count += 1
    return count % 2


def encode_hamming(data):
    """Encode data using Hamming code."""
    data_bits = len(data)
    r = calculate_redundant_bits(data_bits)
    total_bits = data_bits + r

    # Create the Hamming code array with zeros
    hamming = [0] * total_bits

    # Get positions for redundant and data bits
    redundant_positions, data_positions = get_hamming_positions(total_bits)

    # Place data bits
    data_index = 0
    for pos in data_positions:
        if data_index < len(data):
            hamming[total_bits - pos] = int(data[data_index])
            data_index += 1

    # Calculate and place parity bits
    for r_pos in redundant_positions:
        hamming[total_bits - r_pos] = calculate_parity(hamming, r_pos, total_bits)

    return hamming


def check_hamming(received_code):
    """Check received Hamming code for errors."""
    total_bits = len(received_code)
    error_position = 0

    # Calculate error syndrome
    for i in range(total_bits):
        if 2 ** i < total_bits:
            parity = calculate_parity(received_code, 2 ** i, total_bits)
            if parity != 0:  # If parity check fails
                error_position += 2 ** i

    return error_position


def main():
    # Get input data
    data = input("Enter the data bits (e.g., 1001): ").strip()
    if not all(bit in '01' for bit in data):
        print("Error: Please enter valid binary data (0s and 1s only)")
        return

    # Generate Hamming code
    hamming_code = encode_hamming(data)
    print(f"\nGenerated Hamming code: {''.join(map(str, hamming_code))}")

    # Simulate transmission and error detection
    received = input("\nEnter received code (press Enter to use generated code, or enter modified code): ").strip()
    if not received:
        received = ''.join(map(str, hamming_code))

    if not all(bit in '01' for bit in received) or len(received) != len(hamming_code):
        print("Error: Invalid received code")
        return

    # Convert received string to list of integers
    received_code = [int(bit) for bit in received]

    # Check for errors
    error_pos = check_hamming(received_code)
    if error_pos == 0:
        print("\nNo errors detected!")
    else:
        print(f"\nError detected at position {error_pos} from right")
        # Correct the error
        received_code[len(received_code) - error_pos] ^= 1
        print(f"Corrected code: {''.join(map(str, received_code))}")


if __name__ == "__main__":
    main()