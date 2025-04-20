def mad_libs():
    print("Let's play Mad Libs! Fill in the blanks below:")

    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb (past tense): ")
    adverb = input("Enter an adverb: ")
    place = input("Enter a place: ")
    emotion = input("Enter an emotion: ")

    story = f"""
    Today I went to {place}. 
    It was a very {adjective} day. 
    I saw a {noun} that {verb} {adverb} right in front of me! 
    I couldn't believe it, I felt so {emotion}!
    """

    print("\nHere is your Mad Libs story:")
    print(story)

mad_libs()
