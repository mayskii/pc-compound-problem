# Compound Problem

Problem belonging to the post-classroom Mock Interview Question Repository.

## Problem Statement

We are interested in determining whether a whether a string is made up of one or more words in a given list of vocabulary.

Our function will receive a string and a set of strings.

For example:

```py
s = "softwareengineer"
vocab_list = {"engineer", "software", "adie")
```

Here we can see that the given string `s` can be made from two of the words in our vocab list. As a result, the function should return `True`.

Note that the string can use a vocab word multiple times.

For example:

```py
s = "adiessupportingadies"
vocab_list = {"adies", "supporting"}
```

In the above example, the function should return `True`.

However, the string may not use the same character in multiple words.

For example:

```py
s = "friendsandenemies"
vocab_list = {"friends", "sand", "enemies", "end"}
```

The above function should return `False` because we are not allowed to overlap the 's' between both `"friends"` and `"sand"`.

Write a function that returns `True` if a given string can be separated into words from a given set of vocab and `False` if it cannot.

## Examples

### Example 1

```py
s = "softwareengineer"
vocab_list = {"engineer", "software", "adie"}
segmentable(s, vocab_list)
```

Produces

```py
True
```

### Example 2

```py
s = "adiessupportingadies"
vocab_list = {"adies", "supporting"}
segmentable(s, vocab_list)
```

Produces

```py
True
```

### Example 3

```py
s = "friendsandenemies"
vocab_list = {"friends", "sand", "enemies", "end"}
segmentable(s, vocab_list)
```

Produces

```py
False
```
