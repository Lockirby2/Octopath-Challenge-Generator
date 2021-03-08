# Octopath-Challenge-Generator
Hello, and welcome to the Octopath Traveler challenge randomizer! The idea is that every time you complete a chapter for a character, you run the randomizer again to generate a new set of restrictions.  The randomizer is designed to give more restrictions at the less difficult parts of the game to ensure that it is always a challenge.

This is designed with the idea that you will complete chapter 1 for every character, then chapter 2, etc. The run ends when you defeat Galdera. If you do things out of order, you might need to make up rulings on the fly to account for that. If you think there's a grey area in a restriction, I encourage you to just decide what is interesting for you and roll with it.

Many restrictions refer to "slots". The character in "slot 1" is always your main character if they're in your party.  The character in "slot 2" is always the character whose chapter you are going to complete next (unless they're your main character, of course).  Otherwise, you can pick any character for any slot.

The restrictions before the all-caps message below are meant to apply to the entire game. If you don't like one of these game-wide rules (e.g., you want to play with a specific main character or don't like skipping treasure/sidequests), just ignore it!

## Config

Take a look at Config.py for a couple of extra options:

seed: If you want to play using the same restrictions as somebody else, you should use the same seed.  If you don't care, just use random.seed().
cumulative: If cumulative is False, the list of restrictions will be entirely replaced every time you complete a chapter with a character.  If cumulative is True, restrictions will build on the restrictions that already existed. Once you've completed a chapter with all characters, the list of restrictions will reset for next chapter. Note that there won't always be a new restriction in the list. You must specify a seed for this to work.

## Usage

You will need to install Python 3.8.0 to run this program.  Open the command line from the folder containing the code.  Use the command "python RandomOctopath.py" to run the program.  It will then prompt you to enter the number of chapters that you have completed and the number of characters that you have completed them with.  Enter these values to generate your restrictions.
