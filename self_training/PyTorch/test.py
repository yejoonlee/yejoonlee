from yeznable.self_training.PyTorch import c_nn_example

net = c_nn_example.Net()
torch = c_nn_example.torch
nn = c_nn_example.nn

input = torch.randn(1, 1, 32, 32)
out = net(input)
# print(out.size())

net.zero_grad()
out.backward(torch.randn(1,10),retain_graph=True)

target = torch.arange(1, 11, dtype=torch.float) # dummy
target = target.view(1, -1)
criterion = nn.MSELoss()

loss = criterion(out, target)

net.zero_grad()

print('conv1.bias.grad before backward')
print(net.conv1.bias.grad)

loss.backward()

print('conv1.bias.grad after backward')
print(net.conv1.bias.grad)

learning_rate = 0.01

# # SGD
# for f in net.parameters():
#     f.data.sub_(f.grad.data * learning_rate)

import torch.optim as optim

# create optimizer
optimizer = optim.SGD(net.parameters(), lr=0.01)

# in training loop
optimizer.zero_grad()
output = net(input)
loss = criterion(output, target)
loss.backward()
optimizer.step()