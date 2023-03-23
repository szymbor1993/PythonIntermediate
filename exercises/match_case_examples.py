# variables in ’case’ statements     

def location(point: tuple):
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"X axis, Y={y}")
        case (x, 0):
            print(f"Y axis, X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")


# custom classes in ’case’ statements

class Point:
    x: int
    y: int
    
    def __init__(self, x, y):
        self.x = x
        self.y = y


def location(point: Point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"X axis, Y={y}")
        case Point(x=x, y=0):
            print(f"Y axis, X={x}")
        case Point() as p:
            print(f"X={p.x}, Y={p.y}")
        case _:
            raise ValueError("Provided value is not of type 'Point'")


# enums

import enum

class UserType(enum.Enum):
    COMPLAINER = "complainer"
    APPROVER = "approver"


def perform_action(user_type: UserType, **kwargs):
    match user_type:
        case UserType.COMPLAINER:
            send_complaint(kwargs["user"], kwargs["data"])
        case UserType.APPROVER:
            if kwargs["approve"]:
                approve_complaint(kwargs["complaint_id"])
            else:
                reject_complaint(kwargs["complaint_id"])
