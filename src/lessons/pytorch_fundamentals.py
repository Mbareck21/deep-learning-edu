from .base_lesson import BaseLesson

class PyTorchFundamentals(BaseLesson):
    def __init__(self, parent=None):
        content = """# PyTorch Fundamentals

## Autograd: Automatic Differentiation
PyTorch's autograd allows automatic computation of gradients - essential for training neural networks.

### Key Concepts
- `requires_grad`: Tracks operations for gradient computation
- `backward()`: Computes gradients
- `grad`: Stores computed gradients
- `detach()`: Stops gradient tracking
- `no_grad()`: Disables gradient computation

## Practice Exercises

### Exercise 1: Basic Autograd
```python
import torch

# Create tensor with gradient tracking
x = torch.tensor([2.0], requires_grad=True)
y = x ** 2  # Square the tensor
y.backward()  # Compute gradient

print(f"x: {x}")
print(f"y: {y}")
print(f"dy/dx: {x.grad}")  # Should be 4.0 (derivative of x^2 is 2x)
```

### Exercise 2: Neural Network Basics
Create a simple linear layer:
```python
import torch
import torch.nn as nn

# Define input features and layer
input_features = torch.tensor([[2.0, 3.0]])
layer = nn.Linear(2, 1)  # 2 inputs, 1 output

# Forward pass
output = layer(input_features)
print(f"Output: {output}")
```

### Exercise 3: Training Loop
Implement basic training loop:
```python
import torch
import torch.nn as nn
import torch.optim as optim

# Generate sample data
X = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y = torch.tensor([[2.0], [4.0], [6.0], [8.0]])

# Model, loss, optimizer
model = nn.Linear(1, 1)
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Training loop
for epoch in range(100):
    # Forward pass
    outputs = model(X)
    loss = criterion(outputs, y)
    
    # Backward pass
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    if epoch % 10 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item():.4f}')

# Test prediction
test_input = torch.tensor([[5.0]])
prediction = model(test_input)
print(f"\\nPrediction for input 5: {prediction.item():.2f}")
```

## Key Methods
1. `tensor.backward()`: Compute gradients
2. `tensor.grad`: Access gradients
3. `optimizer.zero_grad()`: Reset gradients
4. `optimizer.step()`: Update weights
5. `criterion(output, target)`: Compute loss

## Next Steps
- Convolutional Neural Networks
- Recurrent Neural Networks
- Custom Datasets
- Model Deployment"""
        super().__init__("PyTorch Fundamentals", content, parent)

    def get_default_code(self):
        return """import torch
import torch.nn as nn

# Try implementing a simple neural network
# 1. Define model
# 2. Create sample data
# 3. Train model"""