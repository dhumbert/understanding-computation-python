class Number:
    value = None
    is_reducible = False

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Boolean:
    value = None
    is_reducible = False

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Add:
    left = None
    right = None
    is_reducible = True

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return '{} + {}'.format(self.left, self.right)

    def reduce(self):
        if self.left.is_reducible:
            return Add(self.left.reduce(), self.right)
        elif self.right.is_reducible:
            return Add(self.left, self.right.reduce())
        else:
            return Number(self.left.value + self.right.value)


class Multiply:
    left = None
    right = None
    is_reducible = True

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return '{} * {}'.format(self.left, self.right)

    def reduce(self):
        if self.left.is_reducible:
            return Add(self.left.reduce(), self.right)
        elif self.right.is_reducible:
            return Add(self.left, self.right.reduce())
        else:
            return Number(self.left.value * self.right.value)


class LessThan:
    left = None
    right = None
    is_reducible = True

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return '{} * {}'.format(self.left, self.right)

    def reduce(self):
        if self.left.is_reducible:
            return LessThan(self.left.reduce(), self.right)
        elif self.right.is_reducible:
            return LessThan(self.left, self.right.reduce())
        else:
            return Boolean(self.left.value < self.right.value)


class Machine:
    expression = None

    def __init__(self, expression):
        self.expression = expression

    def step(self):
        self.expression = self.expression.reduce()

    def run(self):
        while self.expression.is_reducible:
            print(self.expression)
            self.step()
        print(self.expression)