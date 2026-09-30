from tools.intent_parser import get_response

def main():
    user_input = None

    while user_input != "exit":
        print("Πώς μπορώ να βοηθήσω;")
        user_input = input("> ")

        print(get_response(user_input))

main()