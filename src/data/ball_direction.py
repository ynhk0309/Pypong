from enum import Enum


# Basic x-y coordinate system: Up and Right being positive


class BallXDirection(Enum):
    LEFT = -1
    RIGHT = 1


class BallYDirection(Enum):
    DOWN = -1
    UP = 1


