"""Generate the Pig Latin form of a provided word."""

def main():
    """Enter a name, and return its Pig Latin form."""
    print("Convert your English word into Pig Latin.\n")

    vowels = ('a', 'e', 'i', 'o', 'u')

    while True:
        english_word = input("Enter your word: ")
        pig_latin_word = ""

        # Check if first letter is a vowel or not
        if english_word[0] in vowels:
            pig_latin_word = english_word + "way"
        else:
            pig_latin_word = english_word[1:] + english_word[0] + "ay"

        print("\n")
        print(f"Pig Latin form of {english_word}: {pig_latin_word}")

        try_again = input("\nGive it another try? [y] for yes, [n] to quit: ")
        if try_again.lower() == 'n':
            break

if __name__=="__main__":
    main()
