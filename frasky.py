#Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
# user_input = (input("Enter a list of integers separated by spaces: "))
# numbers = user_input.split()

# sum = 0
# for i in range(len(numbers)):
#  #   int(numbers[i])  # Convert each string to an integer
#     sum += int(numbers[i])

#print(sum)
#Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.
# favorite_books = ("1984", "To Kill a Mockingbird", "The Great Gatsby", "Pride and Prestige", "7 habits of Highly succesful People")
# for book in favorite_books:
#     print(book)

#Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. 
# Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
# personal_info = {}
# personal_info['name'] = input('What is your name? ')
# personal_info['age'] = input('How old are you? ')
# personal_info['favorite_color'] = input('What is your favorite color? ')
# print(personal_info)
#Write a program that accepts user input to create two sets of integers. 
# Then, create a new set that contains only the elements that are common to both sets.

# first_set = input("Insert numbers with a spcae ")
# first_set1 = set(map(int, first_set.split()))
# second_set = input("Insert numbers with a space ")
# second_set1 = set(map(int, second_set.split()))
# common_elements = first_set1.intersection(second_set1)
# print(common_elements)

#Create a program that stores a list of words.
# Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.
words = input("Enter a list of words separated by spaces: ")
words_list = words.split()
odd_words = []
for i in range(len(words_list)):
    if len(words_list[i]) % 2 != 0:
        odd_words.append(words_list[i])
print("Words with odd number of characters:", odd_words)