# These implement training data for 4-8 coefficients without requiring loops
from random import randint

# Eight Coefficients
def eightNumbers(train_count, train_limit, coefficients):
    train_input = list()
    train_output = list()
    for i in range(train_count):
        a = randint(0, train_limit)
        b = randint(0, train_limit)
        c = randint(0, train_limit)
        d = randint(0, train_limit)
        e = randint(0, train_limit)
        f = randint(0, train_limit)
        g = randint(0, train_limit)
        h = randint(0, train_limit)
        output = (coefficients[0]*a) + (coefficients[1]*b) + (coefficients[2]*c) + (coefficients[3]*d) + (coefficients[4]*e) + (coefficients[5]*f) + (coefficients[6]*g) + (coefficients[7]*h)
        train_input.append([a, b, c, d, e, f, g, h])
        train_output.append(output)

    return train_input, train_output

# Seven Coefficients
def sevenNumbers(train_count, train_limit, coefficients):
    train_input = list()
    train_output = list()
    for i in range(train_count):
        a = randint(0, train_limit)
        b = randint(0, train_limit)
        c = randint(0, train_limit)
        d = randint(0, train_limit)
        e = randint(0, train_limit)
        f = randint(0, train_limit)
        g = randint(0, train_limit)
        output = (coefficients[0]*a) + (coefficients[1]*b) + (coefficients[2]*c) + (coefficients[3]*d) + (coefficients[4]*e) + (coefficients[5]*f) + (coefficients[6]*g)
        train_input.append([a, b, c, d, e, f, g])
        train_output.append(output)

    return train_input, train_output

# Six Coefficients
def sixNumbers(train_count, train_limit, coefficients):
    train_input = list()
    train_output = list()
    for i in range(train_count):
        a = randint(0, train_limit)
        b = randint(0, train_limit)
        c = randint(0, train_limit)
        d = randint(0, train_limit)
        e = randint(0, train_limit)
        f = randint(0, train_limit)
        output = (coefficients[0]*a) + (coefficients[1]*b) + (coefficients[2]*c) + (coefficients[3]*d) + (coefficients[4]*e) + (coefficients[5]*f)
        train_input.append([a, b, c, d, e, f])
        train_output.append(output)

    return train_input, train_output

# Five Coefficients
def fiveNumbers(train_count, train_limit, coefficients):
    train_input = list()
    train_output = list()
    for i in range(train_count):
        a = randint(0, train_limit)
        b = randint(0, train_limit)
        c = randint(0, train_limit)
        d = randint(0, train_limit)
        output = (coefficients[0]*a) + (coefficients[1]*b) + (coefficients[2]*c) + (coefficients[3]*d)
        train_input.append([a, b, c, d])
        train_output.append(output)

    return train_input, train_output

# Four Coefficients
def fourNumbers(train_count, train_limit, coefficients):
    train_input = list()
    train_output = list()
    for i in range(train_count):
        a = randint(0, train_limit)
        b = randint(0, train_limit)
        c = randint(0, train_limit)
        d = randint(0, train_limit)
        output = (coefficients[0]*a) + (coefficients[1]*b) + (coefficients[2]*c) + (coefficients[3]*d)
        train_input.append([a, b, c, d])
        train_output.append(output)

    return train_input, train_output