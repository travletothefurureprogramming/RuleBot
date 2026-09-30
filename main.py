from tools.intent_parser import get_response

def main():
    print("=" * 45)
    print("🤖  RuleBot - Smart CLI Assistant  🤖")
    print("=" * 45)
    print("Πληκτρολόγησε 'exit' ή 'βγαίνω' για έξοδο.\n")

    while True:
        user_input = input("Εσύ > ").strip()

        if user_input.lower() in ["exit", "βγαινω", "κλεισε"]:
            print("RuleBot > Αντίο! Καλή συνέχεια!")
            break

        if not user_input:
            continue

        response = get_response(user_input)
        print(f"RuleBot > {response}\n")

if __name__ == "__main__":
    main()