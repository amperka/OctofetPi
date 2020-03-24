""" The program turns on all the switches in course, then turns them off."""

import time
import octofet


def main():
    print("Please enter the number of devices used.")
    # The number of Octofet boards used.
    device_count = int(input())
    # Chip Enable pin. Set it to 0 or 1, depending on the connections.
    pin_CE = 0
    # Create an object for working with one or more Octofet boards.
    octo = octofet.Octofet(pin_CE, device_count)
    # Switch state variable.
    state = True
    print("Program started...")
    try:
        while True:
            # For each device.
            for device in range(device_count):
                # For each switch.
                for switch in range(8):
                    # Set the current state for the switch.
                    octo.digital_write(switch, state, device)
                    # Wait 1 second.
                    time.sleep(1)
            # Toogle state.
            state = not state
    except KeyboardInterrupt:
        print("Exit")


if __name__ == "__main__":
    main()
