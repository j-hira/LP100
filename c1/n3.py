def pi(sentence: str) -> list:
    import re
    pattern = r"\w+"
    results = re.findall(pattern, sentence)
    return [len(x) for x in results]

if __name__ == "__main__":
    sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    print(pi(sentence))
