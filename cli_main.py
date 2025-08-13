import random
import string

print("\n========== (Secure Encoding & Decoding System) ==========\n")

# Mapping special characters to tokens for encoding
special_map = {
    ' ': '_SPC_', '.': '_DOT_', '@': '_AT_', '!': '_EXCL_', '?': '_QSTN_',
    ',': '_COMMA_', ':': '_COLON_', ';': '_SEMICOLON_',
    "'": '_SQUOTE_', '"': '_DQUOTE_', '/': '_SLASH_', '\\': '_BSLASH_',
    '(': '_LPAREN_', ')': '_RPAREN_', '-': '_DASH_', '_': '_UNDERSCORE_'
}
reverse_map = {v: k for k, v in special_map.items()}  # Reverse mapping for decoding


def shift_char(c, shift):
    # Shift alphabetic characters by shift; map special chars to tokens.
    if c.isalpha():
        base = ord('A') if c.isupper() else ord('a')
        # Shift char within alphabet range (A-Z or a-z)
        return chr((ord(c) - base + shift) % 26 + base)
    
    elif c in special_map:
        # Replace special char with mapped token
        return special_map[c]
    
    else:
        # For unknown chars, encode with _UNK_ and ascii code
        return f'_UNK_{ord(c)}_'


def unshift_char(c, shift):
    # Reverse shift for a single alphabet character.
    if len(c) == 1 and c.isalpha():
        base = ord('A') if c.isupper() else ord('a')
        return chr((ord(c) - base - shift) % 26 + base)
    
    else:
        # Non-alpha tokens handled elsewhere
        return c


def random_str(length):
    # Generate random string of given length from letters, digits, punctuation.
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))


def encoding(length):
    shift = 3  # Fixed Caesar cipher shift
    msg = input("\nEnter your message: ")
    words = msg.split(" ")

    print("\n" + "=" * 50 + "\n")

    encoded_words = []

    for word in words:
        # Rotate word by moving first character to end
        rotated = word[1:] + word[0] if len(word) > 1 else word

        # Encode each character with shift or special mapping
        encoded = ''.join(shift_char(c, shift) for c in rotated)

        # Add random prefix and suffix to obscure the encoded word
        random_prefix = random_str(length)
        random_suffix = random_str(length)
        final = random_prefix + encoded + random_suffix
        encoded_words.append(final)

    print("Your message after encoding is: ", " ".join(encoded_words))


def decoding(length):
    shift = 3
    msg = input("\nEnter a message: ")
    words = msg.split(" ")

    print("\n" + "=" * 50 + "\n")

    decoded_words = []

    for word in words:
        # Remove the random prefix and suffix
        core = word[length:-length] if len(word) >= 2 * length else word

        parts = []
        i = 0
        while i < len(core):
            if core[i] == '_':
                # Detect token start; find token end (next '_')
                end = core.find('_', i + 1)
                token = core[i:end + 1]

                if token in reverse_map:
                    # Map back to special char
                    parts.append(reverse_map[token])
                    i = end + 1

                elif core[i:].startswith('_UNK_'):
                    # Handle unknown char token _UNK_<ascii>_
                    end = core.find('_', i + 5)
                    ascii_code = int(core[i + 5:end])
                    parts.append(chr(ascii_code))
                    i = end + 1
                    
                else:
                    # If token not recognized, add as is and move one char forward
                    parts.append(core[i])
                    i += 1
            else:
                # Normal char, just add
                parts.append(core[i])
                i += 1

        # Reverse the shift on alphabet characters
        unshifted = ''.join(unshift_char(c, shift) for c in parts)

        # Reverse rotation by moving last char to front
        original = unshifted[-1] + unshifted[:-1] if len(unshifted) > 1 else unshifted

        decoded_words.append(original)

    print("Your message after decoding is: ", " ".join(decoded_words))


while True:
    print("\nEnter a number according to your choice:\n")
    print("1. Encode\n2. Decode\n3. Exit")
    print("-" * 50)

    try:
        choice = int(input("Your choice is: "))
        print("-" * 50)
    except ValueError:
        print("-" * 50)
        print("Invalid input. Please enter a number.\n")
        print("\n" + "=" * 50)
        continue

    if choice in [1, 2]:
        length_input = input("Enter length of random characters (recommended: 3, default: 3): ")
        print("-" * 50)
        if length_input.strip() == '':
            length = 3
        else:
            try:
                length = int(length_input)
                if length < 1:
                    print("Length should be at least 1. Using default (3).")
                    print("-" * 50)
                    length = 3
            except ValueError:
                print("Invalid length. Using default (3).")
                print("-" * 50)
                length = 3

    if choice == 1:
        encoding(length)
    elif choice == 2:
        decoding(length)
    elif choice == 3:
        print("Thanks for using the secure encoding system.")
        print("\n" + "-" * 50 + "\n")
        break
    else:
        print("Invalid choice. Please choose a valid option.\n")

    print("\n" + "=" * 50)

    