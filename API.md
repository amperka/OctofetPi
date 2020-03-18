# Octofet API

## class Octofet
Create an object of type Octofet to communicate with a particular Octofet board. One Octofet board
provides 8 power switches also known as "channels".

### `Octofet(pin_CE: int, device_count: int = 1)`
Constructs a new Octofet board object that uses the default hardware SPI bus.
- `pin_CE`: the chip enable (also known as chip select or slave select) pin used to control the
shift-register latch. It can take the values `0` or `1`, which corresponds to the `CE0` or `CE1`
pins on the Raspberry Pi board.
- `device_count`: the number of Octofet boards connected in a daisy-chain. If omitted, defines a
single Octofet board.

### `digital_write(channel: int, value: bool, device: int = 0) -> None`
Sets the state ("on" or "off") of one power switch.
- `channel`: the power switch index. Ranges from `0` to `7`.
- `value`: defines the desired switch state. Valid values: `True` to turn on or `False` to turn off.
- `device`: the index of the affected Octofet in the daisy-chain. Ranges from `0` to `n - 1`, where
`n` is the number of Octofets in the chain. If omitted, targets Octofet nearest to the controller.

### `digital_write_all(value: List[bool], device: int = 0) -> None`
Sets the state ("on" or "off") of all power switches at once.
- `value`: list of boolean values for all of 8 power switches. One value for one channel: `True` is
"on" and `False` is "off".
- `device`: the index of the affected Octofet in the daisy-chain. Ranges from `0` to `n - 1`, where
`n` is the number of Octofets in the chain. If omitted, targets Octofet nearest to the controller.

### `get_channel_state(channel: int, device: int = 0) -> bool`
Returns the last (i.e., current) set state for one power switch of the device. Returns `True` if
turned on or `False` otherwise.
- `channel`: the power switch index. Ranges from `0` to `7`.
- `device`: the index of the affected Octofet in the daisy-chain. Ranges from `0` to `n - 1`, where
`n` is the number of Octofets in the chain. If omitted, targets Octofet nearest to the controller.

### `get_all_channel_states(device: int = 0) -> List[bool]`
Returns a boolean list of the last (i.e., current) set state for all 8 power switches of the device
at once. One value from the list corresponds to one channel: `True` is "on" and `False` is "off".
The argument `device` is the index of the affected Octofet in the daisy-chain. Ranges from `0` to
`n - 1`, where `n` is the number of Octofets in the chain. If omitted, targets Octofet nearest to
the controller.
