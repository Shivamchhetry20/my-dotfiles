# FIX: Need to fix the NeoVIM config to detect the python packages!!!
import os
import sys
import numpy as np
import torch as t
import pandas as pd
import torch.nn as nn

# TODO: Dummy model class need to look into it!!
class NN(nn.Module):
    def __init__(self, n, c):
        self.n = n
        self.c = c

    # NOTE: the forward class is not completed!!
    def forward(self, x):
        pass


