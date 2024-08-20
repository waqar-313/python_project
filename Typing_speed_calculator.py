from time import time
import random

test_strings = [
    "In a world full of challenges and opportunities, those who persevere and remain focused on their goals are the ones who ultimately succeed. It's not about how fast you reach the finish line, but how much you learn and grow along the way.",
    "The art of communication is the language of leadership. The ability to convey thoughts clearly and effectively is a crucial skill that can open doors to countless opportunities, both personally and professionally.",
    "In the digital age, technology continues to evolve at an unprecedented pace, shaping the way we live, work, and interact with one another. Staying updated with the latest advancements is essential for both individuals and organizations.",
    "As the sun set over the horizon, the sky was painted with hues of orange and pink, reflecting off the calm waters of the lake. It was a moment of pure tranquility, a reminder of the beauty that exists in the simplest of things.",
    "The pursuit of knowledge is a lifelong journey, one that requires curiosity, dedication, and a willingness to challenge the status quo. It's through this journey that we expand our understanding of the world and our place in it.",
    "In times of uncertainty, it is the strength of our relationships and the support of those around us that help us navigate through challenges. Building and maintaining these connections is vital to our overall well-being.",
    "The key to innovation lies in thinking outside the box, challenging traditional norms, and embracing new ideas. It's through this mindset that we can create solutions that have a lasting impact on the world.",
    "With each passing day, we are presented with new opportunities to make a positive difference, whether in our own lives or in the lives of others. It's the small actions, when combined, that lead to meaningful change.",
    "The journey of self-improvement is never-ending. It involves continuously setting new goals, reflecting on our progress, and making adjustments as needed. It's this commitment to growth that drives us to become the best versions of ourselves.",
    "In the face of adversity, it's important to remember that challenges are not meant to break us, but to build us. Each obstacle we overcome adds to our strength, resilience, and ability to face future challenges with confidence."
]

def count_mistakes(practice_text, user_text):
    errors = 0
    # Compare up to the length of the shortest text
    length = min(len(practice_text), len(user_text))
    for i in range(length):
        if practice_text[i] != user_text[i]:
            errors += 1
    # Add one for each extra character in the longer text
        else:
          errors+=1
    return errors

def calculate_speed(start_time, end_time, user_text):
    time_diff = end_time - start_time
    if time_diff <= 0:
        return 0
    words = len(user_text.split())
    speed = words / (time_diff / 60)  # Words per minute
    return round(speed, 2)

# Choose a random practice text
practice_text = random.choice(test_strings)
print("                          ***** Typing Master *****")
print()
print(practice_text)
print()

start_time = time()
user_text = input("Enter: ")
end_time = time()

print(f"Speed: {calculate_speed(start_time, end_time, user_text)} wpm")
print(f"Mistakes: {count_mistakes(practice_text, user_text)}")
