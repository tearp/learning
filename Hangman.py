import random

hangman_ascii = """
| |  | |  / _ \  | \ | | | | |_| |  \/  | / _ \ | \ | |
| |__| | | |_| | ||\ | | | |___  | |\/| || |_| |||\ | |
|  __  | |  _  | || \  | | |_| | | |  | ||  _  ||| \  |
| |  | | | | | | ||  \ | |     | | |  | || | | |||  \ |
|_|  |_| |_| |_| ||   \| |_____| |_|  |_||_| |_|||   \|
"""

pics = [
"""
+===+
 |  |
    |
    |
    |
____|
|   |""",

"""
+===+
 |  |
 O  |
    |
    |
____|
|   |""",

"""
+===+
 |  |
 O  |
 |  |
    |
____|
|   |""",
"""
+===+
 |  |
 O  |
/|  |
    |
____|
|   |""",

"""
+===+
 |  |
 O  |
/|\ |
    |
____|
|   |""",

"""
+===+
 |  |
 O  |
/|\ |
/   |
____|
|   |""",

"""
+===+
 |  |
 O  |
/|\ |
/ \ |
____|
|   |"""
]

EASY = ('pie', 'cake', 'bear', 'duck', 'truck')
MED = ('piglet', 'automotive', 'seagull', 'baroness')
HARD = ('xylophone', 'fashionista', 'manbearpig', 'gronkowski')
choice = ''
word = []
board = []
guessed = []

def Hangman():
	global board, word
	guesscount = 0
	board = ['_' for char in word]
	print ' '.join(board)
	if board == word:
		print "YOU WIN!"
		quit()
	while guesscount < 6 :
		if char in guessed == char in word:
			print "YOU WIN!"
			exit()
		guess = raw_input("Guess a letter: ")
		if guess in word:
			board = [char if char == guess or char in guessed else '_' for char in word]
			board = ' '.join(board)
			guessed.append(guess)
		if guess not in word:
			board = [char if char == guess or char in guessed else '_' for char in word]
			board = ' '.join(board)
			guesscount += 1
			guessed.append(guess)
		print(pics[guesscount] + "\n" + board + "\nNext guess: ")
	if guesscount == 6:
		print(pics[guesscount] + "\n YOU DIED. RIP.")
		exit()		

def main():
	global choice, word, new
	print hangman_ascii
	choice = raw_input("Welcome to hangman.\nChoose your difficulty: EASY, MED, HARD.\n")
	if choice == 'EASY':
		word = random.choice(EASY)
		Hangman()
	if choice == 'MED':
		word = random.choice(MED)
		Hangman()
	if choice == 'HARD': 
		word = random.choice(HARD)
main()
