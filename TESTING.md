# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
|  | [questions.py](https://github.com/KC-85/SillyButSerious/blob/main/questions.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/SillyButSerious/main/questions.py) | ![screenshot](documentation/validation/py--questions.png) | N/A |
|  | [run.py](https://github.com/KC-85/SillyButSerious/blob/main/run.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/SillyButSerious/main/run.py) | ![screenshot](documentation/validation/py--run.png) | N/A |

## User Story Testing

⚠️ INSTRUCTIONS ⚠️

Testing User Stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **Features** should already align with the **User Stories**, so this should be as simple as creating a table with the User Story, matching with the re-used screenshot from the respective Feature.

⚠️ --- END --- ⚠️

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a user | I would like to input the number of each sandwich type sold during the day | so that I can track daily sales accurately. | ![screenshot](documentation/features/feature01.png) |
| As a user | I would like to view a breakdown of total sandwich sales by type | so that I can easily see which sandwiches are the most and least popular. | ![screenshot](documentation/features/feature02.png) |
| As a user | I would like the application to calculate the total sandwiches sold for the day | so that I don’t have to do manual sums. | ![screenshot](documentation/features/feature03.png) |
| As a user | I would like to see a trend of sandwich sales over time (e.g., week, month) | so that I can identify which sandwiches are consistently popular. | ![screenshot](documentation/features/feature04.png) |
| As a user | I would like the application to suggest an estimated number of each sandwich type to make for the next day, based on past sales data | so that I can minimize waste and shortages. | ![screenshot](documentation/features/feature05.png) |
| As a user | I would like the app to categorize sandwiches by type (e.g., vegetarian, meat, cheese) | so that I can track popularity within different dietary categories. | ![screenshot](documentation/features/feature06.png) |
| As a user | I would like to input sales quickly with minimal typing | so that I can focus on running the shop instead of logging data. | ![screenshot](documentation/features/feature07.png) |
| As a user | I would like the app to be intuitive and easy to use | so that I can start tracking sales without needing extensive training. | ![screenshot](documentation/features/feature08.png) |

## Bugs

- There are no known bugs i am aware of during this resubmission.

### Fixed Bugs

### Known Issues

| Issue | Screenshot |
| --- | --- |
| The project is designed to be responsive from `375px` and upwards, in line with the material taught on the course LMS. Minor layout inconsistencies may occur on extra-wide (e.g. 4k/8k monitors), or smart-display devices (e.g. Nest Hub, Smart Watches, Gameboy Color, etc.), as these resolutions are outside the project’s scope, as taught by Code Institute. | ![screenshot](documentation/issues/poor-responsiveness.png) |
| When using a helper `clear()` function, any text above the height of the terminal (24 lines) does not clear, and remains when scrolling up. | ![screenshot](documentation/issues/clear-scrolling.png) |
| The `colorama` terminal colors are fainter on Heroku when compared to the IDE locally. | ![screenshot](documentation/issues/colorama.png) |
| Emojis are cut-off when viewing the application from Firefox. | ![screenshot](documentation/issues/emojis.png) |
| The Python terminal doesn't work well with Safari, and sometimes uses cannot type in the application. | ![screenshot](documentation/issues/safari.png) |
| If a user types `CTRL`+`C` in the terminal on the live site, they can manually stop the application and receive and error. | ![screenshot](documentation/issues/ctrl-c.png) |

> [!IMPORTANT]  
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.

