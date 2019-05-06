# Pencil Durability Kata

This application simulates an ordinary graphite pencil, including writing and editing text, point degradation, using the eraser, and sharpening the pencil.

## Prerequisites

```
IntelliJ IDEA with Python Plugin (or PyCharm)
```

## Installing

- Clone the repository at "https://github.com/djdavis1420/pencil_durability.git".
- In your terminal/shell, navigate to the project's root directory.
- Activate a virtual environment (eg, "source ./venv/Scripts/activate") .
    - pip install -Ur test_reqs.txt
- Pytest and Mock will be installed in the virtual environment.

## Contents

 - src/models/pencil.py controls the exercise and the limitations associated with the pencil
 - src/models/paper.py includes supporting methods to erase and edit text
 - test/unit/models/test_pencil.py tests most of the functionality for writing, erasing, and editing text
 - test/unit/models/test_paper.py tests paper specific methods
 - test/integration/test_pencil.py specifically tests text editing and the related interactions between paper and pencil

## Built With

- [IntelliJ IDEA](https://www.jetbrains.com/idea/) - Integrated Development Environment
- [PyTest](https://docs.pytest.org/en/latest/) - Testing Framework for Python
- [mock](https://docs.python.org/dev/library/unittest.mock.html) - Testing Library for Python
