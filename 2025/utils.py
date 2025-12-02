def read_input(file_path: str) -> list[str]:
    input_path = f"2025/inputs/{file_path}"
    with open(input_path, 'r') as f:
        lines = [line.rstrip() for line in f]
    return lines