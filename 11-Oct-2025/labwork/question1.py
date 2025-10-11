# 1.Write a python program to generate a story for an user entered word.

def generate_story(word):
    """Return a short story that includes the user's word."""
    return (
        f"Once upon a time, a curious adventurer found a mysterious '{word}' in an old chest. "
        "Everyone in the village wondered what powers it held. One day, the adventurer used the '") + word + "' and discovered a hidden map leading to a place where dreams come true."


def main():
    user_word = input("Enter a word or short phrase: ").strip()
    if not user_word:
        print("You didn't enter anything. Using 'treasure' as default.")
        user_word = "treasure"
    story = generate_story(user_word)
    print("\nHere is your story:\n")
    print(story)

if __name__ == "__main__":
    main()
