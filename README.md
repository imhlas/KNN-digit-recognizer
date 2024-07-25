# Application for Digit Recognition using KNN algorithm

This application utilizes the KNN algorithm (K-Nearest Neighbors) trained on MNIST data to demonstrate its applicability in image recognition tasks.

Key features:

- KNN algorithm: Utilizes the K-Nearest Neighbors algorithm for digit recognition from MNIST data.
- MNIST data: Leverages the widely-used MNIST dataset, which contains thousands of handwritten digits.
- Parameter tuning: Allows users to modify KNN parameters and observe changes in the recognition results.

## Instructions for installing and running the app

### Clone the repository

```git clone https://github.com/imhlas/KNN-digit-recognizer```

### Install Dependencies

```poetry install```

### Activate the virtual environment

Before running the application, activate the virtual environment:

```poetry shell```

### Run the Application

In the root, use command:

```poetry run invoke start```

### Run tests

If you only want to run the unit tests, use command:

```poetry run invoke test```

You can also run the unit tests and create coverage report with command:

```poetry run invoke coverage-report```
