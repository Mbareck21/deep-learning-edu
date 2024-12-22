from .base_lesson import BaseLesson

class DeepLearningBasics(BaseLesson):
    def __init__(self, parent=None):
        content = """# Introduction to Deep Learning

## What is Deep Learning?
Deep Learning is a type of machine learning that teaches computers to learn from experience. It uses neural networks to recognize patterns in data, similar to how our brains work.

## Getting Started with PyTorch

### Essential Imports
First, let's understand the basic imports we need:
```python
import torch  # Main PyTorch library
import numpy as np  # For numerical operations
```

### Creating Tensors - Examples
Here are different ways to create tensors:
```python
# Create from Python list
x = torch.tensor([1, 2, 3])
print(f"From list: {x}")

# Create with specific data type
float_tensor = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)
print(f"Float tensor: {float_tensor}")

# Create zeros and ones
zeros = torch.zeros(2, 3)  # 2x3 tensor of zeros
ones = torch.ones(2, 3)   # 2x3 tensor of ones
print(f"Zeros:\\n{zeros}")
print(f"Ones:\\n{ones}")
```

### Basic Operations - Examples
Common tensor operations:
```python
# Create tensors
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])

# Addition
c = a + b
print(f"Addition: {c}")

# Multiplication
d = a * 2
print(f"Multiplication by 2: {d}")

# Matrix multiplication
m1 = torch.tensor([[1, 2], [3, 4]])
m2 = torch.tensor([[5, 6], [7, 8]])
result = torch.matmul(m1, m2)
print(f"Matrix multiplication:\\n{result}")
```

## Practice Exercises

### Exercise 1: Creating Tensors
Create the following tensors:
1. A 3x3 tensor filled with random numbers
2. A 2x4 tensor filled with zeros
3. Convert a NumPy array to a PyTorch tensor

<solution>
```python
import torch
import numpy as np

# 1. Random tensor
random_tensor = torch.rand(3, 3)
print("Random tensor:\\n", random_tensor)

# 2. Zeros tensor
zeros_tensor = torch.zeros(2, 4)
print("\\nZeros tensor:\\n", zeros_tensor)

# 3. NumPy to PyTorch
numpy_array = np.array([[1, 2, 3], [4, 5, 6]])
pytorch_tensor = torch.from_numpy(numpy_array)
print("\\nConverted tensor:\\n", pytorch_tensor)
```
</solution>

### Exercise 2: Tensor Operations
Implement the following operations:
1. Add two 2x2 tensors
2. Multiply a tensor by a scalar
3. Compute the dot product of two vectors

<solution>
```python
import torch

# Create tensors
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[5, 6], [7, 8]])

# 1. Addition
sum_tensor = a + b
print("Sum:\\n", sum_tensor)

# 2. Scalar multiplication
scalar_mul = a * 3
print("\\nScalar multiplication:\\n", scalar_mul)

# 3. Dot product
v1 = torch.tensor([1, 2, 3])
v2 = torch.tensor([4, 5, 6])
dot_product = torch.dot(v1, v2)
print("\\nDot product:", dot_product)
```
</solution>

### Exercise 3: Tensor Properties
Write code to:
1. Check tensor's device (CPU/GPU)
2. Get tensor's shape and data type
3. Reshape a tensor

<solution>
```python
import torch

# Create a tensor
x = torch.randn(3, 4)

# 1. Check device
print("Device:", x.device)

# 2. Shape and dtype
print("Shape:", x.shape)
print("Data type:", x.dtype)

# 3. Reshape
reshaped = x.reshape(4, 3)
print("\\nReshaped tensor:\\n", reshaped)
```
</solution>

## Key Methods Summary
1. `torch.tensor()`: Create tensor from data
2. `torch.zeros()`, `torch.ones()`: Create tensors filled with 0s or 1s
3. `tensor.to(device)`: Move tensor to CPU/GPU
4. `tensor.shape`, `tensor.dtype`: Get tensor properties
5. `tensor.reshape()`: Change tensor dimensions

## Next Steps
- Neural Network Basics
- Activation Functions
- Forward Propagation
- Training Process"""
        super().__init__("Deep Learning Basics", content, parent)