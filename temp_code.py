import torch
x = torch.tensor([1.0, 2.0, 3.0])  # Float tensor
y = torch.tensor([1, 2, 3])        # Integer tensor


if torch.cuda.is_available():
    x_gpu = x.cuda()
    print(f"GPU tensor: {x_gpu}")