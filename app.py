from pyfiglet import figlet_format
from termcolor import colored
import random
import time
from colorama import *

# utility functions
def print_ascii(text, color):
  print(colored(figlet_format(text), color))

def colored_text(string, color):
	return color + str(string) + Fore.RESET

def rainbow_string(string):
	new_str = ""

	for i in string:
		new_str += random.choice(all_colors) + i
	new_str += Fore.RESET
	return new_str

# recursion function
def ask_for_questions_n():
	global random_n
	try:
		random_n = int(input(f"🔢 Choose a number of questions that you wanna solve between {colored_text(random_nums['min_q'], Fore.GREEN)} and {colored_text(random_nums['max_q'], Fore.GREEN)}: "))
		# If user input number is not in correct range then throw an error
		if random_n not in range(random_nums['min_q'], random_nums['max_q'] + 1):
			raise Exception()
	except:
		print(colored_text("❌ Something went wrong ¯\\_(ツ)_/¯", Fore.RED))
		ask_for_questions_n()

def generate_random_question(min_nums, max_nums):
	res = ""
	random_operations = ["+", "-", "*"]
	rand_nums_n = random.randint(min_nums, max_nums)
	for i in range(rand_nums_n):
		rand_num = random.randint(1, 30)
		rand_oper = random.choice(random_operations)
		if i == rand_nums_n - 1:
			res += f"{rand_num} ="
		else:
			res += f"{rand_num} {rand_oper} "
	return {
		"question": res,
		"correct": eval(res.split("=")[0]),
}

# variables
all_colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
random_n = 0
random_nums = {
	"min_q": 5,
	"max_q": 30,
}

general_right_questions = 0
random_right_questions = 0

random_questions_n = 0

general_questions = [
	{
		"title": "A figure with 3 sides is known as a: ",
		"correct": "triangle"
	},
	{
		"title": "The smallest two digit number is: ",
		"correct": 10
	},
	{
		"title": "A figure which has no sides and no corners is called: ",
		"correct": "circle"
	},
	{
		"title": "What's pi: ",
		"correct": 3.14
	},
	{
		"title": "Solve: ∞ - ∞ = ",
		"correct": 0
	}
]


# Intro Text
time.sleep(1)
print_ascii("Math Test", "blue")

time.sleep(1)
print(f"The test is devided to 2 parts: {colored_text('General', Fore.CYAN )} and {colored_text('Random', Fore.CYAN)} questions!\n")
time.sleep(3)
play = input("🎲 Start the game? y/n: ")

def game():
	global general_right_questions
	global random_right_questions
	global random_questions_n
	global random_n

	# ------------- General questions -------------
	print(colored_text('''+-------------------+
| GENERAL QUESTIONS | 
+-------------------+
''', Fore.CYAN))
	time.sleep(1.5)
	for i in range(len(general_questions)):
		answer = input(colored_text(f"{i + 1}/{len(general_questions)} ", Fore.MAGENTA) + general_questions[i]['title'] + Fore.YELLOW)
		if answer == str(general_questions[i]['correct']):
			print(colored_text(f"{answer} ✅", Fore.GREEN))
			general_right_questions += 1
		else:
			print(colored_text(f"{answer} ❌", Fore.RED) + colored_text(f" | Correct answer: {general_questions[i]['correct']}", Fore.GREEN))

		print()
		time.sleep(1)

	print(f"👍 Okay, you finished all {colored_text('General', Fore.BLUE)} questions!")
	time.sleep(3)
	print(f"🎮 Now it's time for {colored_text('Random', Fore.BLUE)} questions which are created by a computer randomly!")
	time.sleep(3)
	print("🍀 Good luck!")
	time.sleep(1.7)
	
	# ------------- Random questions -------------
	print(colored_text('''+------------------+
| RANDOM QUESTIONS | 
+------------------+
''', Fore.CYAN))
	time.sleep(1.2)
	ask_for_questions_n()
	time.sleep(0.7)
	print(f"\nNow you should answer {random_n} random questions!\n")
	time.sleep(2)
	for i in range(random_n):
		rand_question = generate_random_question(2, 4)
		answer = input(f"{colored_text(f'{i + 1}/{random_n}', Fore.MAGENTA)} {rand_question['question']} " + Fore.YELLOW)
		random_questions_n += 1
		if answer == str(rand_question['correct']):
			print(colored_text(f"{answer} ✅", Fore.GREEN))
			random_right_questions += 1
		else:
			print(colored_text(f"{answer} ❌", Fore.RED) + colored_text(f" | Correct answer: {rand_question['correct']}", Fore.GREEN))
		
		print()
		time.sleep(1)

	# End of the game
	time.sleep(2)
	print(rainbow_string("CONGRATULATIONS!"))
	time.sleep(2)
	print(f"✔ You finished our {rainbow_string('MATH TEST')}\n")
	time.sleep(3)
	print("Here are the results: \n")
	time.sleep(1)
	print(f"{colored_text('General', Fore.CYAN)} question results: {colored_text(f'{general_right_questions}/{len(general_questions)}✅', Fore.GREEN)}")
	print(f"{colored_text('Random', Fore.CYAN)} question results: {colored_text(f'{random_right_questions}/{random_questions_n}✅', Fore.GREEN)}")

	time.sleep(3)
	print_ascii("Game Over", "blue")

if play == "yes" or play == "y":
	print("✅ Yes\n")
	time.sleep(2)
	game()
