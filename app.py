import os
from datetime import datetime

USER_NAME = "annie"    # keep as-is or change to what you want shown
VERSION   = "1.0.0"

def say_hi(msg: str = "✨ Hello from annie via CI/CD! ✨", file_directory: str = "/app/data/") -> None:
    os.makedirs(file_directory, exist_ok=True)
    # include seconds to avoid collisions
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"outputfile_{USER_NAME}_{VERSION}_timestamp_{timestamp}.txt"
    file_path = os.path.join(file_directory, file_name)
    with open(file_path, "w") as f:
        f.write(msg)
    print(f"File '{file_path}' created successfully.")

def add_numbers(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    say_hi()
