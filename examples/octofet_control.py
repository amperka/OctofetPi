"""Command line utility that allows you to control the state of switches on an
Octofet board."""

import octofet


def main():
    # Chip Enable pin. Set it to 0 or 1, depending on the connections.
    pin_CE = 0
    # Create an object for working with the Octofet board.
    octo = octofet.Octofet(pin_CE)
    try:
        while True:
            print("Enter # of channel to manage (0 to 7):")
            # Selected switch.
            select_switch = int(input())
            if select_switch < 0 or select_switch > 7:
                print("Error: Value should be in 0..7 range")
                continue
            print('Enter "on" to turn on the switch or "off" to turn it off:')
            # The state in which the switch must be turned.
            state = input()
            if state == "on":
                octo.digital_write(select_switch, True)
            elif state == "off":
                octo.digital_write(select_switch, False)
            else:
                print("Error: Incorrect command, expected `on` or `off`")
                continue
    except KeyboardInterrupt:
        print("Exit")


if __name__ == "__main__":
    main()
