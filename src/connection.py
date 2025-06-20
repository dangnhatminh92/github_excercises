import torch
import torch.nn as nn

class MyReluActivation(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return torch.clamp(x, min = 0)
