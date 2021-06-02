def reverse_sentence(sentence):
    rev = sentence.split(' ')[::-1]
    return " ".join(rev)


if __name__ == "__main__":
    print("Hello my name is Kelton")
    print(":reversed:")
    print(reverse_sentence("Hello my name is Kelton"))