def get_most_common_letter(text):
    counter = {}
    for char in text:
        counter[char] = counter.get(char, 0) + 1
    # added this line to remove any spaces from the counter dictionary
    counter.pop(" ")
    # changed this line from:
    # letter = sorted(counter.items(), key=lambda item: item[1])[0][1]
    # as it returned the count of the first element instead of the letter in the last element
    letter = sorted(counter.items(), key=lambda item: item[1])[-1][0]
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
