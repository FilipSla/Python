import math

ab = 10
bc = 10


def calculateAngle(ab: int, bc: int):
    """calculateAngle _summary_

    Args:
        ab (int): _description_
        bc (int): _description_

    Returns:
        _type_: _description_
    """
    ac = pow(pow(ab, 2) + pow(bc, 2), 0.5)
    return round(math.atan(ab / ac) * (180 / math.pi))


result = print(calculateAngle(ab, bc))
