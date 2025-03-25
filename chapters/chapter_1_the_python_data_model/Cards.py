import sys
import collections
import time
from random import choice, shuffle

from .utils import check_for_numbers

# Define the Card datatype
Card = collections.namedtuple("Card", ['rank', 'suit', 'value'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    # Holds the numerical value of a card with 2 being low and Ace being 14 high
    values = list(range(2, 15))
    def __init__(self):
        self._cards = [Card(rank, suit, value) for rank, value in zip(self.ranks, self.values)
                                        for suit in self.suits]
        
    def shuffle(self):
        """
            Shuffle the deck of cards.
        """
        shuffle(self._cards)

    def __len__(self):
        """
            Returns the length of the deck of cards
        """
        return len(self._cards)
    
    def __getitem__(self, position):
        """
            Returns the item at a given index. Allows the cards to be indexed like a list.
            Supports slicing. 
        """
        return self._cards[position]


def score_round(p1: Card, p2: Card):
    """
        Score the round by card value given two cards.
        Return the score index to increment (0 - player 1, 1 - player 2)
    """
    if p1.value > p2.value: # Player 1 wins
        return 0
    
    elif p2.value > p1.value: # player 2 wins
        return 1
    
    else: # Tie doesn't increment score
        return -1

def main():
    args = sys.argv[1:]

    rounds = 20

    print(args)

    if len(args) > 0 and args[0] == "-rounds":
        if check_for_numbers(args[1]):
            rounds = int(args[1])

    deck = FrenchDeck()
    deck.shuffle()


    # Play a 2=player game of War
    score = [0, 0]
    p1 = deck[0::2]
    p2 = deck[1::2]
    rounds = min(len(p1), rounds)
    rounds = max(1, rounds)

    for i in range(rounds):
        print(f"Round: {i+1}")
        print(f"P1: {p1[i].rank} of {p1[i].suit}")
        print(f"P2: {p2[i].rank} of {p2[i].suit}")
        winner = score_round(p1[i], p2[i])

        if winner >= 0: # Is not Negative
            wp = 1 if winner == 0 else 2
            print(f"Player {wp} wins the round.")
            score[winner] += 1
        else:
            print("Round was a tie.")

        print(f"Score: p1-{score[0]}, p2-{score[1]}")
        time.sleep(3) # Give a rest between rounds
    
    if score[0] > score[1]:
        print("Player 1 Wins the Game!")

    elif score[1] > score[0]:
        print("Player 2 Wins the Game!")

    else:
        print("Tie Game! Play Again!")

if __name__ == "__main__":
    main()
