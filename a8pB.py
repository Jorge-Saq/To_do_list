import sys

#This opens the file that the user provided
def generate_list(filename):
	try: #This will run if there is a file that can be opened
		total_list = []
		to_do_list = {}

		#This splits the title, description, and completed and puts it in a master list
		with open(f"{filename}","r") as fin:
			for line in fin:
				words = line.split(",")
				for i,word in enumerate(words):
					words[i] = word.strip()
				total_list.append(words)

			#Traverses the master list, and puts everything in a dictionary.
			for lists in total_list:
					title = lists.pop(0)
					completed = lists.pop()
					if(completed.lower()) == 'yes':
						lists.append(True)
					else:
						lists.append(False)
					rest = lists
					to_do_list[title] = rest
		print()
		return to_do_list

	#In the case the file does not exist it creates a empty dictionary
	except OSError:
		to_do_list = {}
		print()
		return to_do_list

#This edits the file by writing the information out
def save_list(filename , todo_list):

	#This is incase they want to save a empty dictionary
	if(len(todo_list)==0):
		with open(f"{filename}", "w") as fin:
			fin.writelines("")
			fin.close()
		print("Empty text file saved!")
		return

	#This writes the lines in English and correct way.
	else:	
		with open(f"{filename}", "w") as fin:
			for tasks in todo_list:
				lists=todo_list[tasks]
				desc =lists[0]
				completed= lists[-1]
				if completed==True:
					completed = 'Yes'
				else:
					completed = 'No'
				L = [f"{tasks}, {desc}, {completed}\n"]
				fin.writelines(L)
			fin.close()
		print("File saved.\n")

#This adds items to the dictionary
def add_item(todo_list):
	lists=[]
	title = input("Title of task: ")
	desc = input("Description of task: ")
	lists.append(desc)
	lists.append(False)
	todo_list[title]=lists
	print(f"{title} has been added to your list.\n")
	return todo_list

#This removes items from the dictionary
def remove_item(todo_list):
	title = input("What is the title of the task you've completed? ")
	try:
		del todo_list[title]
		print(f"{title} has been removed from the todo list.")
	except KeyError:
		print(f"No task with the title {title} was found. Please double check your spelling and try again.")

#This changes the boolean from false to true
def mark_as_completed(todo_list):
	title = input("What is the title of the task you've completed? ")

	try:
		lists= todo_list[title]
		lists[-1]=True

	except KeyError:
		print(f"No task with the title {title} was found. Please double check your spelling and try again.")

#This prints each item in the list with the correct format
def print_list(todo_list):
	print("\nYour current todo list:")
	for tasks in todo_list:
		lists= todo_list[tasks]
		completed = lists[-1]
		if(completed ==True ):
			completed = "X"
		else:
			completed = " "
		print(f"[{completed}] {tasks}: {lists[0]}")
	print()
	
#This just prints out all the instructions again
def print_instructions():
	print("Type 's' to save your list to a file.")
	print("Type 'q' to quit (remember to save first!).")
	print("Type 'l' to print and see your list.")
	print("Type 'a' to add a new item to the list.")
	print("Type 'c' to mark an item as completed.")
	print("Type 'r' to remove an item from the list.")
	print("Type 'h' to see these instructions again.")

print("Welcome to your to-do list! Instructions:")
print_instructions()


#Call to open the file
user_file = input("Input the file name you want to open: ")
to_do_list = generate_list(user_file)

#Continues to run untill user chooses 'q'
while True:
	user_input = input("What would you like to do? (s/q/l/a/c/r/h) ").lower()
	if user_input == 'q':
		print("Goodbye.")
		sys.exit()
	elif user_input == 's':
		save_list(user_file,to_do_list)
	elif user_input == 'a':
		add_item(to_do_list)
	elif user_input == 'r':
		remove_item(to_do_list)
	elif user_input == 'c':
		mark_as_completed(to_do_list)
	elif user_input == 'l':
		print_list(to_do_list)
	elif user_input == 'h':
		print_instructions()
	else:
		print("Invalid command, Try again.")