from typing import TypedDict
from gpiozero import InputDevice


class PinsConfig(TypedDict):
    pin: int


class Config(TypedDict):
    pins: PinsConfig


class Switch(InputDevice):

    """child class of gpiozero.InputDevice, main functionality is instance property 'value'"""

    def __init__(self, config: Config):
        super().__init__(config['pins']['pin'])