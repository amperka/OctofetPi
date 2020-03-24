"""Command line utility that allows you to control the state of switches on the
Octofet board."""

import octofet


def main():
    # Chip Enable pin. Set it to 0 or 1, depending on the connections.
    pin_CE = 0
    # Create an object for working with the Octofet board.
    octo = octofet.Octofet(pin_CE)
    try:
        while True:
            print("Enter the number of the switch you want to turn on/off.")
            # Selected switch.
            select_switch = int(input())
            if select_switch < 0 or select_switch > 7:
                print("The selected switch is not on the board, try again!")
                continue
            print('Enter "on" to turn on the switch or "off" to turn it off.')
            # The state in which the switch must be turned.
            state = input()
            if state == "on":
                octo.digital_write(select_switch, True)
            elif state == "off":
                octo.digital_write(select_switch, False)
            else:
                print("Incorrect command, try again!")
                continue
    except KeyboardInterrupt:
        print("Exit")


if __name__ == "__main__":
    main()
