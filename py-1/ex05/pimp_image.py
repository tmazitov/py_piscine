import numpy as np


def ft_invert(image: np.ndarray) -> np.ndarray:
    """Invert image colors: each channel value becomes 255 - value."""
    result = np.empty(image.shape, dtype=image.dtype)
    result = 255 - image
    return result


def ft_red(image: np.ndarray) -> np.ndarray:
    """Keep only the red channel, zero out green and blue."""
    result = image * np.array([1, 0, 0], dtype=image.dtype)
    return result


def ft_green(image: np.ndarray) -> np.ndarray:
    """Keep only the green channel, zero out red and blue."""
    result = image - image
    result = result - result
    result[:, :, 1] = image[:, :, 1]
    return result


def ft_blue(image: np.ndarray) -> np.ndarray:
    """Keep only the blue channel, zero out red and green."""
    result = np.zeros(image.shape, dtype=image.dtype)
    result[:, :, 2] = image[:, :, 2]
    return result


def ft_grey(image: np.ndarray) -> np.ndarray:
    """Convert image to greyscale by averaging the three channels."""
    grey = image.sum(axis=2, keepdims=True) / 3
    grey = grey.astype(image.dtype)
    result = np.empty(image.shape, dtype=image.dtype)
    result[:, :, 0:1] = grey
    result[:, :, 1:2] = grey
    result[:, :, 2:3] = grey
    return result
