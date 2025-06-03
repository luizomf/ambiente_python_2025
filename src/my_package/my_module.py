def my_function(x: int, y: int) -> int:
    return x + y


def run_from_script() -> None:
    my_result = my_function(1, 2)
    print(f"The result is {my_result}")


if __name__ == "__main__":
    run_from_script()
