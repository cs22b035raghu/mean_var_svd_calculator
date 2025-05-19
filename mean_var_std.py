import numpy as np

def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")

    ap = np.array(input_list).reshape(3, 3)

    calculations = {
        'mean': [ap.mean(axis=0).tolist(), ap.mean(axis=1).tolist(), ap.mean().item()],
        'variance': [ap.var(axis=0).tolist(), ap.var(axis=1).tolist(), ap.var().item()],
        'standard deviation': [ap.std(axis=0).tolist(), ap.std(axis=1).tolist(), ap.std().item()],
        'max': [ap.max(axis=0).tolist(), ap.max(axis=1).tolist(), ap.max().item()],
        'min': [ap.min(axis=0).tolist(), ap.min(axis=1).tolist(), ap.min().item()],
        'sum': [ap.sum(axis=0).tolist(), ap.sum(axis=1).tolist(), ap.sum().item()]
    }

    return calculations

