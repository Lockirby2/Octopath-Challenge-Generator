import random

# Setting these values won't affect anything. You set these from the command line.
chapter = None
completed = None

# If you want to play using the same restrictions as somebody else, you should use the same seed.
# If you don't care, just use random.seed()
seed = "Boon"
#seed = random.seed()

# If cumulative is False, the list of restrictions will be entirely replaced every time you complete a chapter with a character.
# If cumulative is True, restrictions will build on the restrictions that already existed. Once you've completed a chapter with all characters, the list of restrictions will reset for next chapter. Note that there won't always be a new restriction in the list. You must specify a seed for this to work.
cumulative = True