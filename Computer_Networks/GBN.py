from collections import deque
import random


def go_back_n_protocol(total_frames, window_size):
    # Initialize variables
    frames = list(range(total_frames))  # Create frames [0,1,2,...]
    window = deque(maxlen=window_size)  # Sliding window with max size
    next_frame_to_send = 0  # Next frame to be sent
    frames_acknowledged = 0  # Count of acknowledged frames

    # Simple error simulation (20% chance of loss)
    def frame_is_lost():
        return random.randint(1, 100) <= 20

    print("\nTransmission Details:")
    print("- Window size:", window_size)
    print("- Total frames:", total_frames)
    print("- Frame loss chance: 20%")
    print("\nHow the window slides:")
    print("1. In normal case: Window slides by 1 frame after acknowledgment")
    print("2. In error case: Window goes back to first unacknowledged frame\n")
    input("Press Enter to start transmission...")

    while frames_acknowledged < total_frames:
        # Step 1: Fill the window with new frames
        while len(window) < window_size and next_frame_to_send < total_frames:
            print(f"\nSending frame {next_frame_to_send}")
            window.append(next_frame_to_send)
            next_frame_to_send += 1
            print(f"Current window: {list(window)}")

        # Step 2: Process the first frame in window
        if window:
            current_frame = window[0]
            error = frame_is_lost()

            print(f"\nProcessing frame {current_frame}")

            if error:
                print(f"❌ Frame {current_frame} was lost!")
                print("Window sliding behavior:")
                print(f"- Current window: {list(window)}")
                print(f"- Next_frame_to_send was: {next_frame_to_send}")

                # On error: Go back to the lost frame
                next_frame_to_send = current_frame
                window.clear()

                print(f"- Next_frame_to_send is now: {next_frame_to_send}")
                print("- Window cleared for retransmission")
                print(f"- Will retransmit from frame {current_frame}")

            else:  # Frame received successfully
                print(f"✓ Frame {current_frame} received successfully")
                print("Window sliding behavior:")
                print(f"- Before: {list(window)}")
                window.popleft()  # Remove acknowledged frame
                frames_acknowledged += 1
                print(f"- After:  {list(window)}")

            print(f"\nProgress: {frames_acknowledged}/{total_frames} frames acknowledged")
            input("\nPress Enter for next transmission...")

    print("\nAll frames transmitted successfully!")


# Run the protocol
if __name__ == "__main__":
    total_frames = int(input("Enter number of frames to send: "))
    window_size = int(input("Enter window size: "))
    go_back_n_protocol(total_frames, window_size)