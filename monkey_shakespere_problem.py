import random


goal = "methinks it is like a weasel"
attempts = 0
score = 0


def split(word):
    return [char for char in word]


goal_list = split(goal)


def generate_string():
    """Generates 28 char random string using chars a-z and 'space'."""
    attempt = ''
    for i in range(28):
        attempt += random.choice('abcdefghijklmnopqrstuvwxyz ')
    return attempt


current_best_attempt = generate_string()


def make_score(attempt, goal_list):
    """Returns the similarity ratio of attempt and goal."""
    global score
    global current_best_attempt
    global attempts
    attempt_list = split(attempt)
    matching_chars = 0
    for i in range(len(goal)):
        if attempt_list[i] == goal_list[i]:
            matching_chars += 1
        else:
            attempt_list[i] = random.choice('abcdefghijklmnopqrstuvwxyz ')
            attempts += 1

    score = round(matching_chars / len(goal), 4)
    print(score, ''.join(attempt_list))
    current_best_attempt = ''.join(attempt_list)


while score < 1.0:
    make_score(current_best_attempt, goal_list)

print(attempts)
