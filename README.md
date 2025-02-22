# Questions Generator

Questions Generator is a CLI program written in Python that randomly generates questions from a `CSV` file. Each question includes its answer, difficulty level, and a hint. The program uses the pandas library for data handling and rich for an enhanced CLI interface.

## Features

* Random selection of questions from a CSV file
* Display of questions with specified difficulty levels
* Option to show a hint
* Improved CLI interface using `rich`

## How to run

```shell
python questions_generator.py
```

By default the script read the csv file named `questions.csv`.

You can specify another csv file, as shown below:

```shell
python questions_generator.py -q "file.csv"
```

You can also specify to show questions that have a certain level of difficulty, and if they will be shown only once (no repetition)

```shell
python questions_generator.py -r -d <difficult>
```

## How to insert your questions

A sample file called `questions.csv` is already available in the folder, anyway, you can add your questions in easy way as shown below:

```csv
question,answer,hint,difficulty
"Q1","A1","h1",1
"Q2","A2","h2",0
"Q3","A3","h3",1
"Q4","A4","h4",0
"Q5","A5","h5",0
"Q6","A6","h6",1
```

## Demo

![cli demo](images/demo.gif)

## Dependencies

- `rich` *(used for CLI affordance)*
- `pandas` *(used for CSV)*
- `random` *(built-in module)*
- `os` *(built-in module)*
- `sys` *(built-in module)*
- `argparse` *(built-in module)*

# Author

*Emilio Garzia, 2024*
