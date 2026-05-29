import os
import subprocess
import sys
import tempfile
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def is_number(value: any) -> bool:
    """Return True if value is a non-bool integer."""
    return isinstance(value, (int)) and not isinstance(value, bool)


def slice_image(image: np.ndarray, begin: int) -> np.ndarray:
    """Slice a 400x400 grayscale region from the center of the image."""
    try:
        if not isinstance(image, np.ndarray):
            raise TypeError("image must be a numpy array")
        if not is_number(begin):
            raise TypeError("begin must be an integer")

        if image.ndim != 3:
            raise ValueError("image must be a 3D array")
        if image.shape[2] < 1:
            raise ValueError("image must have at least one channel")
    except (TypeError, ValueError) as e:
        print(f"{type(e).__name__}: {e}")
        return np.array([])

    required_sizes = {
        "height": 400,
        "width": 400,
        "channels": 1,
    }

    offset_height = (image.shape[0] - required_sizes["height"]) // 2
    offset_width = (image.shape[1] - required_sizes["width"]) // 2

    h = required_sizes["height"]
    w = required_sizes["width"]
    c = required_sizes["channels"]

    print(f"New shape after slicing: ({h}, {w}, {c})",
          f"or ({h}, {w})" if c == 1 else "")

    return image[
        offset_height:offset_height + h,
        offset_width:offset_width + w,
        :c
    ]


def image_is_valid(image: np.ndarray) -> bool:
    """Return True if image is a valid 3D numpy array."""
    try:
        if not isinstance(image, np.ndarray):
            raise TypeError("image must be a numpy array")
        if image.ndim != 3:
            raise ValueError("image must be a 3D array")
    except (TypeError, ValueError) as e:
        print(f"{type(e).__name__}: {e}")
        return False

    return True


def draw_image(image: np.ndarray) -> None:
    """Display the image with axes using matplotlib and eog."""
    if not image_is_valid(image):
        return

    display = image.squeeze() if image.shape[2] == 1 else image
    plt.imshow(display, cmap="gray" if display.ndim == 2 else None)
    tmp = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    try:
        plt.savefig(tmp.name)
        subprocess.run(["eog", tmp.name])
    finally:
        tmp.close()
        os.remove(tmp.name)


def main():
    """Load animal.jpeg, slice a 400x400 grayscale region and display it."""
    animal_image = ft_load("./animal.jpeg")
    if animal_image.size <= 0:
        print("Failed to load animal image.")
        sys.exit(1)

    print(animal_image)

    sliced_image = slice_image(animal_image, 0)
    print(sliced_image)

    draw_image(sliced_image)


if __name__ == '__main__':
    main()
