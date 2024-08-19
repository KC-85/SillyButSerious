"""
This module contains the logic for running an interactive quiz game.
It includes functions for managing a leaderboard and displaying questions.
"""

import random
import json
import os
from termcolor import colored
from questions import QUESTIONS
# Assuming QUESTIONS is imported from questions.py

LEADERBOARD_FILE = "leaderboard.json"
QUIZ_LENGTHS = [10, 20, 50, 100]


def display_welcome_message():
    """Display a welcome message and instructions for the quiz."""
    print(colored(
        "\n===== Welcome to the Silly but Serious Quiz! =====", "cyan"
    ))
    print(colored("\nHow to play:", "yellow"))
    print("1. Choose the number of questions you want to answer.")
    print(
        "2. For each question, enter the letter (A, B, C, or D) "
        "corresponding to your answer."
    )
    print(
        "3. After each question, you'll see if you were correct and "
        "your current score."
    )
    print(
        "4. At the end of the quiz, you can add your name to the "
        "leaderboard."
    )
    print("5. Have fun and test your knowledge across various categories!")
    print(colored("\nLet's begin!", "green"))
    input("Press Enter to start...")


def load_leaderboard():
    """Load the leaderboard from a JSON file."""
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, 'r') as file:
            return json.load(file)
    return []


def save_leaderboard(leaderboard):
    """Save the leaderboard to a JSON file."""
    with open(LEADERBOARD_FILE, 'w') as file:
        json.dump(leaderboard, file)


def update_leaderboard(name, score, total_questions):
    """Update the leaderboard with a new score."""
    leaderboard = load_leaderboard()
    leaderboard.append(
        {"name": name, "score": score, "total": total_questions}
    )
    leaderboard.sort(
        key=lambda x: (x["score"] / x["total"], x["total"]),
        reverse=True
    )
    leaderboard = leaderboard[:20]  # Keep only top 20
    save_leaderboard(leaderboard)


def display_leaderboard():
    """Display the top 20 scores from the leaderboard."""
    leaderboard = load_leaderboard()
    print("\nTop 20 Leaderboard:")
    for i, entry in enumerate(leaderboard, 1):
        print(
            f"{i}. {entry['name']}: {entry['score']}/{entry['total']} "
            f"({entry['score'] / entry['total'] * 100:.2f}%)"
        )


def get_quiz_length():
    """Prompt the user to choose the number of questions for the quiz."""
    while True:
        try:
            print("\nChoose the number of questions:")
            for i, length in enumerate(QUIZ_LENGTHS, 1):
                print(f"{i}. {length} questions")
            choice = int(input("Enter your choice (1-4): "))
            if 1 <= choice <= 4:
                return QUIZ_LENGTHS[choice - 1]
            print(
                colored(
                    "Invalid choice."
                    "Enter a number between 1 and 4 (A, B, C, D).",
                    "red"
                )
            )
        except ValueError:
            print(colored("Invalid input. Please enter a number.", "red"))


def run_quiz():
    """Run the main quiz game."""
    display_welcome_message()
    total_questions = get_quiz_length()
    asked_questions = set()
    score = 0

    for question_num in range(total_questions):
        # Get a question that has not been asked
        while True:
            question_index = random.randint(0, len(QUESTIONS) - 1)
            if question_index not in asked_questions:
                asked_questions.add(question_index)
                break

        question = QUESTIONS[question_index]

        # Display the question
        print(f"\nCategory: {question['category']}")
        print(question['question'])
        for option, answer in question['options'].items():
            print(f"{option}: {answer}")

        # Get user answer
        while True:
            user_answer = input("Your answer (A/B/C/D): ").upper()
            if user_answer in ['A', 'B', 'C', 'D']:
                break
            print(colored("Invalid input. Please enter A, B, C, or D.", "red"))

        # Check if the answer is correct
        if user_answer == question['correct_answer']:
            print(colored("Correct!", "green"))
            score += 1
        else:
            print(colored(f"Wrong. The correct answer was {question['correct_answer']}.", "red"))

        print(f"Current Score: {score}/{question_num + 1}")

    print(f"\nQuiz completed! Final Score: {score}/{total_questions}")
    
    # Update leaderboard
    name = input("Enter your name for the leaderboard: ")
    update_leaderboard(name, score, total_questions)
    display_leaderboard()

if __name__ == "__main__":
    run_quiz()
    