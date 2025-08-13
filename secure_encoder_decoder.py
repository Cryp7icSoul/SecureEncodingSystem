import random
import string
import sys
import os
import importlib.util

# --- PyInstaller Packaging Support ---
def resource_path(relative_path):
    """Get absolute path to resource for PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# --- Original Encoding/Decoding Logic ---
# Mapping special characters to tokens
special_map = {
    ' ': '_SPC_', '.': '_DOT_', '@': '_AT_', '!': '_EXCL_', '?': '_QSTN_',
    ',': '_COMMA_', ':': '_COLON_', ';': '_SEMICOLON_',
    "'": '_SQUOTE_', '"': '_DQUOTE_', '/': '_SLASH_', '\\': '_BSLASH_',
    '(': '_LPAREN_', ')': '_RPAREN_', '-': '_DASH_', '_': '_UNDERSCORE_'
}

# Reverse mapping for decoding
reverse_map = {v: k for k, v in special_map.items()}

def shift_char(c, shift):
    """Shift alphabetic characters, map special chars to tokens."""
    if c.isalpha():
        base = ord('A') if c.isupper() else ord('a')
        return chr((ord(c) - base + shift) % 26 + base)
    elif c in special_map:
        return special_map[c]
    else:
        return f'_UNK_{ord(c)}_'

def unshift_char(c, shift):
    """Reverse shift for a single alphabet character."""
    if len(c) == 1 and c.isalpha():
        base = ord('A') if c.isupper() else ord('a')
        return chr((ord(c) - base - shift) % 26 + base)
    return c

def random_str(length):
    """Generate random string of given length."""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def encode_message(msg, length=3, shift=3):
    """Encode a message using Caesar cipher + rotation + special mapping."""
    words = msg.split(" ")
    encoded_words = []
    for word in words:
        rotated = word[1:] + word[0] if len(word) > 1 else word
        encoded = ''.join(shift_char(c, shift) for c in rotated)
        final = random_str(length) + encoded + random_str(length)
        encoded_words.append(final)
    return " ".join(encoded_words)

def decode_message(msg, length=3, shift=3):
    """Decode a message back to original."""
    words = msg.split(" ")
    decoded_words = []
    for word in words:
        core = word[length:-length] if len(word) >= 2 * length else word
        parts = []
        i = 0
        while i < len(core):
            if core[i] == '_':
                end = core.find('_', i + 1)
                token = core[i:end + 1]
                if token in reverse_map:
                    parts.append(reverse_map[token])
                    i = end + 1
                elif core[i:].startswith('_UNK_'):
                    end = core.find('_', i + 5)
                    ascii_code = int(core[i + 5:end])
                    parts.append(chr(ascii_code))
                    i = end + 1
                else:
                    parts.append(core[i])
                    i += 1
            else:
                parts.append(core[i])
                i += 1
        unshifted = ''.join(unshift_char(c, shift) for c in parts)
        original = unshifted[-1] + unshifted[:-1] if len(unshifted) > 1 else unshifted
        decoded_words.append(original)
    return " ".join(decoded_words)

# --- PyInstaller Runtime Support ---
if getattr(sys, 'frozen', False):
    # Running in PyInstaller bundle
    def get_module_path():
        return os.path.dirname(sys.executable)
else:
    # Running in normal Python environment
    def get_module_path():
        return os.path.dirname(os.path.abspath(__file__))