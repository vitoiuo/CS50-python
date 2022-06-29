def convert (emoji: str) -> str:
    emoji_dict = {':)': '🙂', ':(':'🙁'}
    print(emoji_dict[emoji])