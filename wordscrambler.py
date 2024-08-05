import random

def scramble_one_letter(word):
    if len(word) < 2:
        return word  # No need to scramble if the word is too short

    # Choose a random index to move
    index_to_move = random.randint(0, len(word) - 1)
    
    # Choose a new position for the selected letter
    new_position = random.randint(0, len(word) - 1)
    
    # Ensure the new position is different from the original position
    while new_position == index_to_move:
        new_position = random.randint(0, len(word) - 1)
    
    # Create a list of characters from the word
    char_list = list(word)
    
    # Move the character to the new position
    char_to_move = char_list.pop(index_to_move)
    char_list.insert(new_position, char_to_move)
    
    # Join the list back into a string
    scrambled_word = ''.join(char_list)
    
    return scrambled_word

# Test the word scrambler
word = input("Enter a word to scramble: ")
scrambled_word = scramble_one_letter(word)
print("Scrambled word:", scrambled_word)
