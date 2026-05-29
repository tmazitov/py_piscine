import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """Load image as an array of pixels and prints its shape."""
    try:
        with Image.open(path) as img:
            pixels = len(img.getbands())
            h = img.height
            w = img.width
            print(f"The shape of image is: ({h}, {w}, {pixels})")
            return np.array(img)
    except (FileNotFoundError, OSError, TypeError, AttributeError) as e:
        print(f"{type(e).__name__}: {e}")
        return np.array([])
