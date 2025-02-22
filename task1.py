import random

def tanh(x):
    exp_x = (2.718281828459045 ** x) 
    exp_neg_x = (2.718281828459045 ** -x)
    return (exp_x - exp_neg_x) / (exp_x + exp_neg_x)

i1, i2 = 0.05, 0.10
b1, b2 = 0.5, 0.7

w1, w2, w3, w4 = [random.uniform(-0.5, 0.5) for _ in range(4)]
w5, w6, w7, w8 = [random.uniform(-0.5, 0.5) for _ in range(4)]

net_h1 = (i1 * w1) + (i2 * w3) + b1
net_h2 = (i1 * w2) + (i2 * w4) + b1

out_h1 = tanh(net_h1)
out_h2 = tanh(net_h2)

net_o1 = (out_h1 * w5) + (out_h2 * w7) + b2
net_o2 = (out_h1 * w6) + (out_h2 * w8) + b2

out_o1 = tanh(net_o1)
out_o2 = tanh(net_o2)

print("Output1 =", out_o1)
print("Output2 =", out_o2)
