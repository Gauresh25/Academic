import random
import time

# Get inputs
bit_sequence = int(input('Enter the bit sequence: '))
total_no_frames = int(input('Enter the total no of frames: '))

sending_window = 2 ** bit_sequence - 1
receiving_window = 1

print(f'Sending Window Size: {sending_window}')
print(f'Receiving Window Size: {receiving_window}')

frame = []
for i in range(total_no_frames):
    frame.append(input(f"Enter the {i}th frame: "))

print("Frames to be sent:", frame)


def send_frame(frame_number):
    # Simulate sending frame
    print(f"Sending Frame {frame_number}: {frame[frame_number]}")
    # Simulate random loss of frame
    if random.choice([True, False]):
        return False  # Simulate frame loss
    return True  # Simulate successful transmission


def receive_ack(ack_number):
    # Simulate receiving an ACK
    print(f"Receiving ACK for Frame {ack_number}")
    return random.choice([True, False])  # Simulate random ACK loss


def go_back_n_protocol():
    base = 0
    next_seq_num = 0

    while base < total_no_frames:
        # Send all frames in the current window
        while next_seq_num < base + sending_window and next_seq_num < total_no_frames:
            if send_frame(next_seq_num):
                next_seq_num += 1
            else:
                print(f"Frame {next_seq_num} lost, retrying...")

        # Wait for ACK for the base frame
        while base < next_seq_num:
            if receive_ack(base):
                print(f"ACK received for Frame {base}")
                base += 1
            else:
                print(f"ACK for Frame {base} lost, retransmitting...")
                # Retransmit all frames starting from base
                next_seq_num = base

        # Simulate a small delay for the next iteration
        time.sleep(1)


go_back_n_protocol()
