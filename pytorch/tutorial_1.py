from __future__ import print_function
import torch

print("Tensors:")
# empty 5*3 tensor
x = torch.empty(5, 3)
# random initialized 5*3 tensor
x = torch.rand(5, 3)
# tensor initialized with zeros of dtype long
x = torch.zeros(5, 3, dtype=torch.long)
# tensor initialized with values
x = torch.tensor([5.5, 3])
# reuse previus tensor
x = x.new_ones(5, 3, dtype=torch.double)
x = torch.randn_like(x, dtype=torch.float)
print(x)
# size of tensor
print(x.size()) # returns a tuple

# Operations:
print("Operations:")
y = torch.rand(5, 3)
# addition 1
result_1 = x + y
# addition 2
result_2 = torch.add(x, y)
# addition to an output tensor as argument
result_3 = torch.empty(5, 3)
torch.add(x, y, out=result_3)
# addition in-place
y.add_(x)

# conventional numpy operations
print(x)
print(x[:, 1])

# resizing/reshape a tensor
print("\nRESIZING:")
x = torch.randn(4,4)
print(x)
y = x.view(16)
print(y)
z = x.view(-1, 8)
print(z)
print("sizes")
print(x.size(), y.size(), z.size())

# get value from one element tensor
print("get value:")
x = torch.randn(1)
print(x)
print(x.item())

# Numpy Bridge (converting from torch tensor to numpy array and vice versa)
print("Numpy Bridge:")
# torch to numpy:
print("torch to numpy:")
a = torch.ones(5)
b = a.numpy()

a.add_(1)
print(a)
print(b)

# numpy into torch
print("numpy to torch:")
import numpy as np
a = np.ones(5)
b = torch.from_numpy(a)
np.add(a, 1, out=a)
print(a)
print(b)


#CUDA tensors:
print("CUDA tensors:")
if torch.cuda.is_available():
    device = torch.device("cuda")
    y = torch.ones_like(x, device=device)
    x = x.to(device)
    z = x + y
    print(z)
    print(z.to("cpu", torch.double))
