import subprocess
import tempfile

import numpy as np
from matplotlib import pyplot as plt
import os

from load_image import ft_load
from pimp_image import ft_invert, ft_blue, ft_green, ft_grey, ft_red


def image_is_valid(image: np.ndarray) -> bool:
    """Return True if image is a valid 2D or 3D numpy array."""
    try:
        if not isinstance(image, np.ndarray):
            raise TypeError("image must be a numpy array")
        if image.ndim not in (2, 3):
            raise ValueError("image must be a 2D or 3D array")
    except (TypeError, ValueError) as e:
        print(f"{type(e).__name__}: {e}")
        return False

    return True


def draw_image(image: np.ndarray) -> None:
    """Display the image with axes using matplotlib and eog."""
    if not image_is_valid(image):
        return

    display = image.squeeze() if image.ndim == 3 else image
    plt.imshow(display, cmap="gray" if display.ndim == 2 else None)
    tmp = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    try:
        plt.savefig(tmp.name)
        subprocess.run(["eog", tmp.name])
    finally:
        tmp.close()
        os.remove(tmp.name)


def main():
    image = ft_load("landscape.jpg")

    effects = [
        {"name": "Inverted Image", "action": ft_invert},
        {"name": "Red Image", "action": ft_red},
        {"name": "Green Image", "action": ft_green},
        {"name": "Blue Image", "action": ft_blue},
        {"name": "Grey Image", "action": ft_grey},
    ]

    for e in effects:

        name = e["name"]
        print("Effect :", name)

        action = e["action"]
        effected_image = action(image)
        draw_image(effected_image)

    print(ft_invert.__doc__)


if __name__ == "__main__":
    main()
