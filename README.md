# KNN-digit-recognizer

Application for digit recognizion using MNIST-data and KNN. 

Instructions for installing and running the app can be found below.

More detailed user guide can be found from [user guide](dokumentaatio/user_guide.md).

## Clone the repository

```git clone https://github.com/imhlas/KNN-digit-recognizer```

## Install Dependencies

```poetry install```

## Activate the virtual environment

Before running the application, activate the virtual environment:

```poetry shell```

## Run the Application

In the root, use command:

```poetry run invoke start```

## Run tests

If you only want to run the unit tests, use command:

```poetry run invoke test```

You can also run the unit tests and create coverage report with command:

```poetry run invoke coverage-report```
