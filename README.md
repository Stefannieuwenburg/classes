In this exercise you will make use of Object Oriented Programming. Books have been written about this subject, and some of them may even be worth reading. For now it suffices to say that you are going to declare and use a number of classes that are going to interact with each other. It's a difficult one, so take your time!

Part 1: Players In main.py, write a class Player that is going to represent a soccer player.

Define the Player class' initialization method (init) such that it can receive these arguments, in this order:

name (str) speed (float between 0 and 1) endurance (float between 0 and 1) accuracy (float between 0 and 1) If speed, endurance or accuracy is not between 0 and 1 (inclusive), a ValueError must be raised.

Save the given arguments as instance attributes under the names name, speed, endurance and accuracy.

Define an instance method introduce that takes no arguments (except self!) and returns a string like the following, where 'Bob' is replaced by the player's actual name:

'Hello everyone, my name is Bob.'

Define an instance method strength that takes no arguments and returns a tuple like the following, where the string speed is replaced by the player's actual highest attribute and the value corresponds to that attribute:

('speed', 0.8)

If multiple attributes share the same value, prioritize as follows:

speed > endurance > accuracy

Part 2: Commentators In main.py, create a new class Commentator.

Implement it in such a way that we can do this:

ray = Commentator('Ray Hudson') print(ray.name)

'Ray Hudson'
Write an instance method sum_player that takes an instance of a player and returns the sum of their speed, endurance and accuracy attributes.

To do this you may need the function getattr: The Python getattr Function.

Write an instance method compare_players that takes two instances of Player (in no particular order) and one of 'speed', 'endurance' and 'accuracy' as its arguments and returns the name of the player that scores the highest on this attribute. For example:

alice = Player('Alice', 0.8, 0.2, 0.6) bob = Player('Bob', 0.9, 0.2, 0.6) print(ray.compare_players(alice, bob, 'speed'))

'Bob'
If the players score equally on this attribute, return the name of the player that has the highest strength according to the strength function you just implemented.

If these are also equal, report the name of the player that has the highest total score according to the sum_player function you just implemented.

If these are also equal, return the string:

'These two players might as well be twins!'

Wincpy Check Use wincpy check classes to see if you met all of the requirements for this exercise. Did you pass the test?
