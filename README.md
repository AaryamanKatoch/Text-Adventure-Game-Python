1) Aaryaman Katoch    akatoch@stevens.edu

2) Github URL - 

3) Hours spent on the project : 15 hours

4) Testing of the code was done manually by me. I created a few test maps and tested my code for expected vs actual outputs for various input commands.

5) Unresolved Bugs and Issues: My testcases are failing on Gradescope. It might be because of my win and loose conditions, which can cause an early end of game.

6) Example of a difficult issue or bug: While testing my code I saw that the first lines about the roomn you are in (eg: You are in a simple room with white walls.
Exits: north east) were appearing everytime, even when it made no sense for example, 
====>>>>  Instead of 
(What would you like to do? get rose
You pick up the rose.
What would you like to do? inventory
Inventory:
  rose
What would you like to do? go north
You go north.)

====>>>>It was something like: 
(What would you like to do? get rose
You pick up the rose.
You are in a simple room with white walls.

Exits: north east
What would you like to do? inventory
Inventory:
  rose
You are in a simple room with white walls.

Exits: north east
What would you like to do? go north
You go north.).

I solved this issue by adding a flag to check if the room description is required or not.

7) Three Extensions I implemented:
Help verb, drop verb and winning and losing conditions 

Help Verb - help verb tells players what the valid verbs are. We write ... after verbs that expect a target of some kind. It will give a list of all the verbs we have defined in our application. The command list is immediately followed by a "What would you like to do?" message.

drop Verb - drop verb drops an item in of the rooms. It can only drop an item from the inventory. Its implementation was kind of similar to get verb. 
Syntax : drop [item]

Winnning and Losing Conditions:
Winning Condition - Enter room 0 with exactly three items in inventory

Example step to win:
Take East from white room
Pick up the rose
Take a North from red room
Pick up sword and shield
Take a South from green room
Take a west from red room
You win


Losing Condition - entered room 0 or run any command in room 0 five times without 3 items in the inventory

Example steps to loose:
Run any 5 commands ( valid or valid in the white room without 3 items in inventory)





