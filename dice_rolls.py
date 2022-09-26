from random import randint

SUCCESS_THRESHOLD = 7


def _roll_single_dice(doubles: int = 10):
    result = randint(1, 10)
    if result >= doubles:
        return 2
    if result > SUCCESS_THRESHOLD:
        return 1
    return 0


def roll(dice: int, doubles: int = 10):
    return sum(_roll_single_dice(doubles) for _ in range(dice))
