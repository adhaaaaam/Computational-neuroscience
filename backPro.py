import random

def tanh(x):
    exp_x = (2.718281828459045 ** x)
    exp_neg_x = (2.718281828459045 ** -x)
    return (exp_x - exp_neg_x) / (exp_x + exp_neg_x)

i1, i2 = 0.05, 0.10
b1, b2 = 0.5, 0.7

w1, w2, w3, w4 = [random.uniform(-0.5, 0.5) for _ in range(4)]
w5, w6, w7, w8 = [random.uniform(-0.5, 0.5) for _ in range(4)]

predictedO1, predictedO2 = 0.01, 0.99
LearningRrate = 0.1

for _ in range(99000):
    Net_h1 = (i1 * w1) + (i2 * w3) + b1
    Net_h2 = (i1 * w2) + (i2 * w4) + b1

    Out_h1 = tanh(Net_h1)
    Out_h2 = tanh(Net_h2)

    Net_o1 = (Out_h1 * w5) + (Out_h2 * w7) + b2
    Net_o2 = (Out_h1 * w6) + (Out_h2 * w8) + b2

    Outo1 = tanh(Net_o1)
    Outo2 = tanh(Net_o2)

    ErrorO1 = predictedO1 - Outo1
    Error_O2 = predictedO2 - Outo2

    deltaOuto1 = -(predictedO1 - Outo1)
    deltaOuto2 = -(predictedO2 - Outo2)

    deltaOutNeto1 = Outo1 * (1 - Outo1)
    deltaOutNeto2 = Outo2 * (1 - Outo2)

    deltaNeto1W5 = Out_h1
    deltaNeto1W7 = Out_h2
    deltaNeto2W6 = Out_h1
    deltaNeto2W8 = Out_h2

    delta_o1 = deltaOuto1 * deltaOutNeto1 * Out_h1
    delta_o2 = deltaOuto2 * deltaOutNeto2 * Out_h2

    w5 -= LearningRrate * delta_o1 
    w6 -= LearningRrate * delta_o2 
    w7 -= LearningRrate * delta_o1 
    w8 -= LearningRrate * delta_o2 

    delta_h1 = (delta_o1 * w5 + delta_o2 * w6) 
    delta_h2 = (delta_o1 * w7 + delta_o2 * w8) 

    w1 -= LearningRrate * delta_h1 * i1
    w2 -= LearningRrate * delta_h2 * i1
    w3 -= LearningRrate * delta_h1 * i2
    w4 -= LearningRrate * delta_h2 * i2

print("Output1 =", Outo1) , print("Output2 =", Outo2) 
