from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Exercise:
    title: str
    description: str
    starter_code: str
    solution: str
    validation_code: Optional[str] = None

@dataclass
class Lesson:
    title: str
    content: str
    exercises: List[Exercise]

CURRICULUM = {
    "Deep Learning Basics": Lesson(
        title="Deep Learning Basics",
        content="""# Deep Learning Fundamentals
        
## What is Deep Learning?
Deep learning is a subset of machine learning that uses neural networks with multiple layers.

## Key Concepts
- Neural Networks: Multi-layer networks of artificial neurons
- Training Data: Examples used to teach the network
- Forward Propagation: How data flows through the network
- Backpropagation: How the network learns from mistakes
- Activation Functions: Functions that add non-linearity""",
        exercises=[
            Exercise(
                title="PyTorch Basics",
                description="Create your first tensor and perform basic operations",
                starter_code="""import torch

# Create a tensor
x = torch.tensor([1, 2, 3])
print(f"Tensor: {x}")

# Check CUDA availability
print(f"CUDA available: {torch.cuda.is_available()}")""",
                solution="""import torch

x = torch.tensor([1, 2, 3])
print(f"Tensor: {x}")

if torch.cuda.is_available():
    x_gpu = x.cuda()
    print(f"GPU tensor: {x_gpu}")"""
            )
        ]
    )
}