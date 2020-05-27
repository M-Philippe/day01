from vector import Vector


pos = [0, 1.0, 2.0]
v1 = Vector(pos)
print(v1.__dict__)
v2 = Vector(3)
print(v2.__dict__)
v3 = Vector(range(10, 18))
print(v3.__dict__)
print("Addition")
v1 = v1 + v2
v4 = v3 + 3.8
# error
# v1 += "hello"
print(v1.__dict__)
print(v4.__dict__)

v1 = Vector(pos)
v2 = Vector(3)
v3 = Vector(range(10, 18))
# error
# v1 -= v3
v1 = v1 - v2
v4 = v3 - 3.8
print("Substraction")
print(v1.__dict__)
print(v4.__dict__)

v1 = Vector(pos)
v2 = Vector(3)
v3 = Vector(range(10, 18))
# error
# v1 -= v3
v1 = v1 - v2
v4 = v3 - 3.8
print("Substraction")
print(v1.__dict__)
print(v4.__dict__)

v1 = Vector(pos)
v2 = Vector(3)
v3 = Vector(range(10, 18))
v1 = v1 / 3
v3 /= 3
print("Division")
print(v1.__dict__)
print(v3.__dict__)

v1 = Vector(pos)
v2 = Vector(3)
v3 = Vector(range(10, 18))
v1 = v1 * v2
v3 *= 3
print("multiplication")
print(v1)
print(v3.__dict__)
