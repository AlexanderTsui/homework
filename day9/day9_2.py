import math


class Point:

    def __init__(self, x, y, z):
        self.x = 0
        self.y = 0
        self.z = 0
        print(f"创建了Point({self.x}, {self.y}, {self.z})")

    def __add__(self, other):
        if isinstance(other, Vector):
            new_x = self.x + other.x
            new_y = self.y + other.y
            new_z = self.z + other.z
            return Point(new_x, new_y, new_z)
        if isinstance(other, Point):
            print("你不能把两个点相加！")

    def __sub__(self, other):
        if isinstance(other, Point):
            new_x = self.x - other.x
            new_y = self.y - other.y
            new_z = self.z - other.z
            return Vector(new_x, new_y, new_z)
        if isinstance(other, Vector):
            new_x = self.x - other.x
            new_y = self.y - other.y
            new_z = self.z - other.z
            return Point(new_x, new_y, new_z)

    def __eq__(self, other):
        if isinstance(other, Point):
            if self.x == other.x and self.y == other.y and self.z == other.z:
                return True
            else:
                return False
        else:
            print("用于比较的对象不是Point类！")

    def __lt__(self, other):
        if isinstance(other, Point):
            distance_self = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
            distance_other = math.sqrt(other.x ** 2 + other.y ** 2 + other.z ** 2)
            return distance_self < distance_other
        return NotImplemented

    def __del__(self):
        print(f"销毁了Point({self.x}, {self.y}, {self.z})")


class Vector:

    def __init__(self, x, y, z):
        self.x = 0
        self.y = 0
        self.z = 0
        print(f"创建了Vector({self.x}, {self.y}, {self.z})")

    def __add__(self, other):
        if isinstance(other, Vector):
            new_x = self.x + other.x
            new_y = self.y + other.y
            new_z = self.z + other.z
            return Vector(new_x, new_y, new_z)

    def __sub__(self, other):
        if isinstance(other, Vector):
            new_x = self.x - other.x
            new_y = self.y - other.y
            new_z = self.z - other.z
            return Vector(new_x, new_y, new_z)

    def __mul__(self, angle):
        radians = math.radians(angle)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y, self.z)

    def __truediv__(self, angle):
        radians = math.radians(angle)
        new_x = self.x * math.cos(radians) + self.y * math.sin(radians)
        new_y = -self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y, self.z)

    def __eq__(self, other):
        if isinstance(other, Vector):
            if self.x == other.x and self.y == other.y and self.z == other.z:
                return True
            else:
                return False
        else:
            print("用于比较的对象不是Vector类！")

    def __lt__(self, other):
        if isinstance(other, Vector):
            self_modulus = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
            other_modulus = math.sqrt(other.x ** 2 + other.y ** 2 + other.z ** 2)
            return self_modulus < other_modulus
        return NotImplemented

    def __del__(self):
        print(f"销毁了Vector({self.x}, {self.y}, {self.z})")
