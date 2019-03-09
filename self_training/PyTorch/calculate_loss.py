from yeznable.self_training.PyTorch import nn_example

net = nn_example.Net()
torch = nn_example.torch
nn = nn_example.nn

input = torch.randn(1, 1, 32, 32)
out = net(input)
# print(out.size())

net.zero_grad()
out.backward(torch.randn(1,10))

target = torch.arange(1, 11, dtype=torch.float) # dummy
target = target.view(1, -1)
criterion = nn.MSELoss()

loss = criterion(out, target)
print(loss)