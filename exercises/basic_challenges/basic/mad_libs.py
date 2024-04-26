def mad_libs():
    story = "Once upon a time, there was a {} {} who {} {}."
    noun = input("Enter a noun: ")
    adjective = input(f"Enter an adjective: ")
    verb1 = input(f"Enter a verb: ")
    verb2 = input(f"Enter another verb: ")
    print(story.format(noun, adjective, verb1, verb2))

mad_libs()