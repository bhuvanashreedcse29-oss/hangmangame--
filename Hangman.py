import random
word_data = {
    "Animals": [
        ("tiger", "Big striped wild animal"),
        ("elephant", "Largest land animal"),
        ("kangaroo", "Jumps and has a pouch"),
        ("dolphin", "Smart sea animal"),
    ],
    "Fruits": [
        ("apple", "Keeps doctor away"),
        ("banana", "Yellow curved fruit"),
        ("mango", "King of fruits"),
        ("grapes", "Small juicy bunch fruit"),
    ],
    "Countries": [
        ("india", "Famous for Taj Mahal"),
        ("japan", "Land of rising sun"),
        ("brazil", "Famous for football"),
        ("canada", "Cold country"),
    ]
}

def choose_category():
    print("\n📂 Choose Category:")
    for i, key in enumerate(word_data.keys(), 1):
        print(f"{i}. {key}")
    
    choice = int(input("Enter choice number: "))
    category = list(word_data.keys())[choice - 1]
    return category

def play_game():
    category = choose_category()
    word, hint = random.choice(word_data[category])

    guessed = []
    display = ["_"] * len(word)
    chances = 6
    score = 0
    hint_used = False

    print("\n🎯 Hangman (Smart Version)")
    print("Category:", category)

    while chances > 0 and "_" in display:
        print("\nWord:", " ".join(display))
        print("Guessed:", " ".join(guessed))
        print("Chances left:", chances)
        print("Score:", score)

        print("\nOptions:")
        print("1. Guess Letter")
        print("2. Get Hint (-2 score)")

        option = input("Choose option (1/2): ")

        if option == "2":
            if not hint_used:
                print("💡 Hint:", hint)
                score -= 2
                hint_used = True
            else:
                print("⚠️ Hint already used!")
            continue

        guess = input("Enter letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Invalid input!")
            continue

        if guess in guessed:
            print("⚠️ Already guessed!")
            continue

        guessed.append(guess)

        if guess in word:
            print("✅ Correct!")
            score += 2
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
        else:
            print("❌ Wrong!")
            chances -= 1
            score -= 1

    if "_" not in display:
        print("\n🎉 You Won!")
    else:
        print("\n💀 You Lost!")

    print("Word was:", word)
    print("Final Score:", score)

def main():
    while True:
        play_game()
        again = input("\nPlay again? (yes/no): ").lower()
        if again != "yes":
            print("👋 Exiting Game...")
            break

main()
