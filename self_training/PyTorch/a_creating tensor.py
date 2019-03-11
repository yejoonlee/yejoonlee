# use conda env tc

from __future__ import print_function
import torch

x = torch.rand(5,3)
y = torch.rand(5,3)

result= torch.empty(3,3)

torch.add(x,y,out = result)

print(result)