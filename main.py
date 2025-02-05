import time

while True:
    startStopwatch = input("Please enter 'Start' to start the stopwatch, and 'Quit' to exit: ").strip().lower()

    if startStopwatch == 'start':
        print("Stopwatch started! Press Ctrl+C to stop.")
        start_time = time.time()

        try:
            while True:
                elapsed_time = time.time() - start_time
                print(f"Time: {elapsed_time:.3f} seconds", end="\r")
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("\nStopwatch stopped.")

    elif startStopwatch == 'quit':
        print("Exiting...")
        break

    else:
        print("I didn't quite get that...")
