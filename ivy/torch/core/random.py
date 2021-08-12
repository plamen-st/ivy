"""
Collection of PyTorch random functions, wrapped to fit Ivy syntax and signature.
"""

# global
import torch
from typing import Optional, List


def random_uniform(low: float = 0.0, high: float = 1.0, shape: Optional[List[int]] = None, dev_str: str = 'cpu'):
    rand_range = high - low
    if shape is None:
        true_shape: List[int] = []
    else:
        true_shape: List[int] = shape
    return torch.rand(true_shape).to(dev_str.replace('gpu', 'cuda')) * rand_range + low


def multinomial(population_size: int, num_samples: int, batch_size: int, probs: Optional[torch.Tensor] = None,
                replace: bool = True, dev_str: str = 'cpu'):
    if probs is None:
        probs = torch.ones((batch_size, population_size,)) / population_size
    return torch.multinomial(probs, num_samples, replace).to(dev_str.replace('gpu', 'cuda'))


def randint(low: int, high: int, shape: List[int], dev_str: str = 'cpu'):
    return torch.randint(low, high, shape).to(dev_str.replace('gpu', 'cuda'))


def seed(seed_value: int = 0) -> None:
    torch.manual_seed(seed_value)
    torch.cuda.manual_seed(seed_value)
    return


def shuffle(x):
    batch_size = x.shape[0]
    return x[torch.randperm(batch_size)]