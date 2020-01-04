from __future__ import print_function
import torch

# Create tensor with requires_grad=True to track computation
x = torch.ones(2, 2, requires_grad=True)
print(x)

# compute with x
y = x + 2
print(y)
print(y.grad_fn)

# compute with y
z = y*y*3
out = z.mean()
print(z, out)

out.backward()
print(x.grad)
