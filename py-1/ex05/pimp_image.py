import numpy as np


def ft_invert(image: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""
    result = 255 - image
    return result


def ft_red(image: np.ndarray) -> np.ndarray:
    """Keeps only the red channel of the image received."""
    result = image * np.array([1, 0, 0], dtype=image.dtype)
    return result


def ft_green(image: np.ndarray) -> np.ndarray:
    """Keeps only the green channel of the image received."""
    result = image - image
    result[:, :, 1] = image[:, :, 1]
    return result


def ft_blue(image: np.ndarray) -> np.ndarray:
    """Keeps only the blue channel of the image received."""
    result = np.zeros(image.shape, dtype=image.dtype)
    result[:, :, 2] = image[:, :, 2]
    return result


def ft_grey(image: np.ndarray) -> np.ndarray:
    """Converts the image received to grayscale."""
    grey = image.sum(axis=2, keepdims=True) / 3
    grey = grey.astype(image.dtype)
    result = np.empty(image.shape, dtype=image.dtype)
    result[:, :, 0:1] = grey
    result[:, :, 1:2] = grey
    result[:, :, 2:3] = grey
    return result
