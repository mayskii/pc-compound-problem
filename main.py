def segmentable(s, vocab_list):
    vocab = set(vocab_list)
    n = len(s)
    
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in vocab:
                dp[i] = True
                break
    
    return dp[n]


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
