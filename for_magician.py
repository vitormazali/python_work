# initializing lists for the program
magicians = ["alice","david","carolina"]
showrunners = []

# running through the list items and performing actions in each loop
for magician in magicians:
    print(f"\nThat was a great trick! Congrats, {magician.title()}!")
    showrunners.append(magician.title())
    print(f"We have watched the show from:\t")
    for showrunner in showrunners:
        print(f"{showrunner}")

# closing the program
print(f"\nThanks all of the great magicians, {magicians}, we had a good time with you!")