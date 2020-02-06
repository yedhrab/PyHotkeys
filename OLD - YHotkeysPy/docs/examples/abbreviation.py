import keyboard

source_text = "Esma"
replacement_text = "🦋"


global replacement
replacement = '\b'*(len(source_text)+1) + replacement_text


def callback():
    global replacement
    return keyboard.write(replacement)


keyboard.add_word_listener(source_text, callback, triggers=[
                           ':'], match_suffix=False, timeout=2)

keyboard.wait()
