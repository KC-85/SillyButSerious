**
SILLYBUTSERIOUS


Overview
Silly but Serious is an interactive quiz game designed to challenge users across various categories. With a playful and engaging interface, the quiz targets trivia enthusiasts of all ages who are looking to test their knowledge in a fun and dynamic way. Whether you're aiming to improve your general knowledge or just pass the time, Silly but Serious provides a seamless and enjoyable experience.



source: amiresponsive

UX
The design process for Silly but Serious focused on creating an intuitive and user-friendly interface. The quiz game is easy to navigate, with clear instructions and a simple layout that prioritizes user interaction. The visual elements are both entertaining and functional, ensuring that users remain engaged throughout their quiz experience.

Features
Existing Features
Dynamic Question Display

Each quiz session presents a new set of random questions, ensuring a unique experience every time. The user can select the number of questions they want to answer, making the quiz adaptable to both quick and longer sessions.


Real-time Feedback

Users receive immediate feedback after each question, showing whether their answer was correct or not. This feature keeps the user engaged and informed about their progress throughout the quiz.


Score Tracking

The quiz tracks the user's score and displays it after each question, along with the final score at the end of the session. This feature adds a competitive element to the game, encouraging users to improve their performance.


Future Features
Leaderboards

Implement a leaderboard system where users can compare their scores with others. This feature will add a competitive edge and encourage repeat gameplay.
Category Selection

Allow users to choose specific categories before starting the quiz, tailoring the quiz experience to their interests.
Timed Questions

Introduce a timer for each question to increase the challenge and excitement of the game.
Tools & Technologies Used
used for version control. (git add, git commit, git push)
used for secure online code storage.
used for hosting the deployed back-end site.
used as the back-end programming language.
used as my local IDE for development.
Data Model
Flowchart
A flowchart was created to map out the logic of the quiz game before coding began. This helped in visualizing the user journey and ensuring a smooth user experience.



Classes & Functions
The program is structured using functions to handle various parts of the quiz game:

run_quiz()
Controls the main flow of the quiz, including question selection and score tracking.
display_welcome_message()
Displays the welcome message and instructions for the quiz.
get_quiz_length()
Prompts the user to select the number of questions for the quiz.
play_again()
Asks the user if they want to play again after completing the quiz.
Testing
[!NOTE]
For all testing, please refer to the TESTING.md file.

Deployment
The Silly but Serious quiz game is deployed on Heroku. Below are the steps taken to deploy the project:

Heroku Deployment
Create a New App on the Heroku dashboard.
Add Buildpacks: Python first, then Node.js.
Configure Config Vars such as PORT and any secret keys.
Ensure the following files are present:
requirements.txt
Procfile
runtime.txt
Push the project to Heroku using Git.
Local Deployment
To run the project locally:

Clone the repository: git clone https://github.com/KC-85/SillyButSerious.git
Install dependencies: pip3 install -r requirements.txt
Run the app locally and test the features.
Credits
Content
Source	Location	Notes
YouTube	terminal	Tutorial for adding color to the Python terminal
StackOverflow	various	Helped troubleshoot code issues during development
Media
Source	Location	Type	Notes
Pexels	hero image	image	Favicon and hero image
Unsplash	quiz images	image	Quiz background images
Acknowledgements
Special thanks to my Code Institute mentor for guidance and feedback throughout this project.
Thanks to the Code Institute Slack community for support and troubleshooting help.****