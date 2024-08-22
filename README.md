SILLYBUTSERIOUS

GitHub Repository here:

Live Application here: https://silly-but-serious-ff8c9d0224be.herokuapp.com/

source: amiresponsive

UX
The SillyButSerious Quiz is designed to be a fun and challenging quiz game that tests the user’s knowledge across various categories. The game targets users who enjoy trivia and want to test their skills in a competitive environment. The simple interface is intended to be intuitive, allowing users to focus on answering questions rather than navigating complex menus.

The game is hosted on Heroku and runs in the terminal, which presents some limitations, such as incompatibility with mobile and tablet devices. This constraint is due to the specific terminal environment provided by Code Institute.

User Stories
New Site Users
As a new site user, I want to start the quiz easily so that I can test my knowledge.
As a new site user, I want to see my progress after each question so that I know how well I'm doing.
As a new site user, I want to play a quiz with a varying number of questions so that I can choose the quiz length based on my available time.
Returning Site Users
As a returning site user, I want to replay the quiz multiple times so that I can improve my score.
As a returning site user, I want to challenge myself with different categories so that I can broaden my knowledge base.
Features
Existing Features
Welcome Message & Instructions

When the user starts the game, they are greeted with a stylized welcome message using ASCII art. The instructions are displayed in a clear format, ensuring that users understand how to play.

Question Selection

Users can select the number of questions they want to answer, giving them control over the quiz length.

Question Display

Each question is displayed along with multiple-choice answers. Users can select an option, and the system will provide immediate feedback on whether the answer is correct.

Final Score Display

After completing the quiz, users receive a final score that summarizes their performance.

Future Features
Category Selection
Allow users to select specific categories before starting the quiz to tailor the experience to their interests.
Timed Questions
Introduce a time limit for each question to increase the challenge.
Multiplayer Mode
Implement a mode where multiple users can compete against each other in real-time.
Tools & Technologies Used
 used for version control. (git add, git commit, git push)
 used for secure online code storage.
 used for hosting the deployed back-end site.
 used as the back-end programming language.
 used for ASCII art text in the terminal.
 used for colored text output in the terminal.
Data Model
The quiz logic is straightforward, focusing on presenting questions, recording answers, and displaying the final score. The program uses lists and dictionaries to store questions and possible answers. Random selection ensures that the same quiz does not repeat when played multiple times.

python
Copy code
def get_quiz_length():
    """Prompt the user to choose the number of questions for the quiz."""
    # Code to handle quiz length selection
The quiz questions are stored in a separate file (questions.py) and imported into the main quiz logic. This modular approach keeps the code organized and makes it easier to manage.

Testing
[!NOTE]
For all testing, please refer to the TESTING.md file.

Testing was performed manually due to the terminal-based nature of the game. Unfortunately, due to the constraints of the terminal environment, the game does not function on mobile or tablet devices.

Deployment
Heroku Deployment
This project is deployed on Heroku and is accessible via the following link: SILLYBUTSERIOUS.

Deployment steps:

Follow Heroku's deployment process for a Python app, including setting up Procfile, requirements.txt, and configuring the necessary environment variables.
Local Deployment
To deploy this project locally:

Clone the repository.
Install the required dependencies using pip install -r requirements.txt.
Run the application in your terminal.
Credits
Content
Source	Location	Notes
W3Schools	entire site	for general coding examples and inspiration
StackOverflow	specific issues	for troubleshooting and code snippets
Acknowledgements
I would like to thank my Code Institute mentor, Tim Nelson for his support throughout the development of this project.
Special thanks to the Code Institute Slack community for providing advice and support during development.
