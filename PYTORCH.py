import torch

# Create a tensor
x = torch.tensor([[1, 2], [3, 4]])
print("Tensor:\n", x)

# Create a random tensor
rand_tensor = torch.rand(2, 3)
print("\nRandom Tensor:\n", rand_tensor)

# Zeros and Ones
z = torch.zeros(2, 2)
o = torch.ones(2, 2)

a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
b = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)

print("Add:\n", a + b)
print("Mul:\n", a * b)
print("MatMul:\n", a @ b)
print("Mean:", a.mean())
print("Reshape:\n", a.view(4))


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

x = torch.rand(3, 3).to(device)
print("On GPU:\n", x)

x = torch.tensor(2.0, requires_grad=True)
y = x ** 2 + 3 * x + 4
y.backward()  # Computes dy/dx

print("Gradient of y w.r.t x:", x.grad)

x = torch.tensor(5.0, requires_grad=True)
y = 3 * x + 7
y.backward()
print("dy/dx:", x.grad)  # Should print 3


