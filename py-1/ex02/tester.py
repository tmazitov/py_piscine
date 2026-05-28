from load_image import ft_load


def main():
    tests = [
        "./animal.jpeg",
        "./landscape.jpg",
        "./notexist.png",
        "./load_image.py",
        None,
        123
    ]

    for path in tests:
        image = ft_load(path)
        if image.size > 0:
            print(f"Loaded image from '{path}' successfully.\n")
        else:
            print(f"Failed to load image from '{path}'.\n")


if __name__ == '__main__':
    main()
