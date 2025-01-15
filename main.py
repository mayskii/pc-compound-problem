def segmentable(s, vocab_list):
    pass


s = "softwareengineer"
vocab_list = set(["engineer", "software", "adie"])
assert (segmentable(s, vocab_list)) == True

s = "adiessupportingadies"
vocab_list = set(["adies", "supporting"])
assert (segmentable(s, vocab_list)) == True

s = "friendsandenemies"
vocab_list = set(["friends", "sand", "enemies", "end"])
assert (segmentable(s, vocab_list)) == False

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
