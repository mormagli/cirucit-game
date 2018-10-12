
Cirucit is a card game played with 7 cards you can print out from the pdf in this repo. The set of cards, each with 6 curves of each of 6 colors, contains cards that conform to a number of intersecting symmetries without which the game would be noticably imbalanced. 

I wrote a series of Python scripts in tandem with the development of the game's rules (found below) to help produce a viable set of cards. There are no rotationally isometric curves within a color, for example, no two curves share an endpoint, and it is impossible to arrange any two cards such that more than one color of elipse is formed.


# Circuit – rules – 

Circuit is a game for 2-6 players played with 7 cards and 1-3 coins*

Objective:
	Be the first player to complete a loop of your own color. In other words, arrange the cards such 			that at least four curves of your color meet each other, leaving no unmatched endpoint.


Setup:
	Each player picks a color, cards 1-6 are shuffled, and starting player is determined
	(Both player color and starting player may be randomized by shuffling the deck and dealing out 		cards to each player, in which case you should reshuffle before you begin.)
	Place the ‘7’ card face-up on the table, and place the coins on it:
		for 2 players, place 1 coin;
		for 3-4 players, place 2 coins;
		for 5-6 players, place 3 coins.
	In clockwise order, each player takes a turn drawing a card from the deck and placing it on the table. Each card must be played adjacent to at least one card already in play, such that at least one line on that card is aligned with a line of the same color on another card.


Cards:
	On each card there is:
		one curved line of each color;
		a number (1-7). Each number has a color, and each player should consider the card 				which has a number of their color to be ‘their’ card;
		a circle to indicate where to place coins.


Card Placement and movement:
	After all 7 cards are in play, the next player begins the game. Play proceeds clockwise, with each player moving one or more cards on their turn. 
	Moving a card consists of:
		picking up any card, as long as doing so would not isolate one or more cards from the rest (at all times, each card or adjacent set of cards besides the card being moved must be adjacent to all  other cards or sets of adjacent cards)
		playing that card adjacent to at least one card already in play, such that at least one line on that card is aligned with a line of the same color on another card.
	After a player plays a card, they may either end their turn or move the numerically subsequent card (so, if they first moved the ‘5’ card, they may move the ‘6’ card and if they moved the ‘7’ card first, they may move the ‘1’ card). Players may continue to move cards until the numerically subsequent card is one that cannot be moved without isolating one or more cards from the rest.


Coins:
	A card with one or more coins on it cannot be moved, but it is also skipped when determining numerical order (so, if there is a coin on the ‘3’ card and a player moves the ‘2’ card, they may then move the ‘4’ card).
	Coins all start in play (on the ‘7’ card) but may, as the game progresses, end up in the possession of a player. Coins may, in fact, be placed and removed in the middle of someone’s turn, thereby changing the moves available to that player. There is no limit to the number of coins you can have in your possession at a time..
	At any point in their turn, if a player has at least one coin in your possession, they may place that coin on any card (that is not currently being moved).

Interrupting another player’s turn:
	During anyone else’s turn, if a player moves ‘your’ card (the card that has a number matching your color), you may say “break” out loud. If you do so, play is interrupted until you take a coin off of one of the cards. If there are no coins currently in play, you may take a coin from the active player instead. If you say “break” you must take a coin if possible. Once you do, the active player resumes their turn.
	 During anyone else’s turn, if a player moves any card other than ‘your’ card and you have a coin in your possession, you may say “surge” out loud. If you do so, play is interrupted and you must place a coin on ‘your’ card.
