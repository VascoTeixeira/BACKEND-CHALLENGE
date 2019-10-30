import contextlib
import random


def do_log(msg):
    print(("    " * LOG_INDENT) + msg)


def no_log(msg):
    pass


log = do_log
LOG_INDENT = 0


@contextlib.contextmanager
def indent_log():
    global LOG_INDENT
    LOG_INDENT += 1
    yield
    LOG_INDENT -= 1


@contextlib.contextmanager
def suppress_log():
    global log
    orig_log = log
    log = no_log
    yield
    log = orig_log


def draw(n=30):
    """Draw a sample of 'n' different numbers in the range [1, 60]."""
    return set(random.sample(xrange(1, 61), n))


def str_to_mask(mask_str, hit_symbol="X"):
    """Convert a string representing a card mask to a list of booleans."""
    return [char == hit_symbol for char in mask_str]


def mask_to_str(mask, hit_symbol="X", miss_symbol="-"):
    """Inverse of str_to_mask()."""
    return "".join(hit_symbol if m else miss_symbol for m in mask)


class Card(object):
    """Represents the bingo card composed by a list of numbers"""
    def __init__(self, nums):
        self.nums = list(nums)

    def __repr__(self):
        return repr(self.nums)

    def hits(self, draw):
        """List of booleans indicating whether each cell's number is part of the 'draw'."""
        return [n in draw for n in self.nums]
        #raise NotImplementedError(">>> your code goes here <<<")


class Prize(object):
    """Represents a bingo prize value given based on a specific bingo pattern"""
    def __init__(self, value, mask):
        self.value = value
        self.mask = mask

    def __repr__(self):
        return "{} (value={})".format(mask_to_str(self.mask), self.value)

    def check(self, card_hits):
        """True if the given 'card_hits' list contains this prize."""
        comparison_list = [x and y for x, y in zip(card_hits, self.mask)] #Pairs the 'card_hits' with the prize pattern mask, then proceeds to create a boolean list indicating if each hit is present in the prize pattern 
        return comparison_list == self.mask #if the comparison_list is equal to the prize pattern, the card_list follows the corresponding pattern
        #raise NotImplementedError(">>> your code goes here <<<")


class Game(object):
    """Represents the Game object used to accommodate the list of possible prizes in the game"""
    def __init__(self, prizes=()):
        self.prizes = list(prizes)


class Player(object):
    """Represents the player object used to accommodate player data (player cards, player balance), and game actions affecting the player"""
    def __init__(self, game, cards, balance=100):
        self.game = game
        self.cards = cards
        self.balance = balance

    def play(self, bet=1):
        self.place_bet(bet)
        nums = draw()
        log("Draw: {}".format(sorted(nums)))
        prizes_won = list(self.check_cards(nums))
        if len(prizes_won) > 0:
            log("Awarding prizes:")
            with indent_log():
                for prize in prizes_won:
                    self.award_winnings(prize, bet)
        log("Balance after play: {}".format(self.balance))
        return prizes_won

    def check_cards(self, nums):        
        """Verify prizes against all cards and return an iterable of all prizes won."""
        prizes = []
        for card in self.cards:
            for prize in self.check_card(card, nums):
                prizes.append(prize)
        return prizes
        #raise NotImplementedError(">>> your code goes here <<<")

    def check_card(self, card, nums):
        """Verify prizes against a given card and return an iterable of all prizes won."""
        log("Checking card: {}".format(card))
        card_hits = card.hits(nums)
        with indent_log():
            log("Card hits: {}".format(mask_to_str(card_hits)))
            for prize in self.game.prizes:
                log("Checking prize: {}".format(prize))
                if prize.check(card_hits):
                    with indent_log():
                        log("Prize won!")
                        yield prize

    def place_bet(self, bet):
        log("Placing bet: {}".format(bet))
        self.add_balance(-bet*len(self.cards)) #bet value multiplied by the number of cards (negative value being that it must be subtracted to the player's balance)
        #raise NotImplementedError(">>> your code goes here <<<")

    def award_winnings(self, prize, bet):
        log("Awarding winnings for {} with bet {}.".format(prize, bet))
        self.add_balance(prize.value*bet) #the player's winnings are multiplied by the player's bet value
        #raise NotImplementedError(">>> your code goes here <<<")

    def add_balance(self, delta):
        new_balance = self.balance + delta
        log("Balance change: {} {:+d} => {}".format(self.balance, delta, new_balance))
        if new_balance < 0.0:
            raise ValueError("attempting to set negative balance")
        self.balance = new_balance


# Global list of bingo prizes.
PRIZES = [
    Prize(
        value=2000,
        mask=str_to_mask(
            "XXXXX"
            "XXXXX"
            "XXXXX"
        ),
    ),
    Prize(
        value=200,
        mask=str_to_mask(
            "X---X"
            "XXXXX"
            "X---X"
        ),
    ),
    Prize(
        value=20,
        mask=str_to_mask(
            "X---X"
            "X---X"
            "X---X"
        ),
    ),
    Prize(
        value=10,
        mask=str_to_mask(
            "--X--"
            "-X-X-"
            "X---X"
        ),
    ),
    Prize(
        value=10,
        mask=str_to_mask(
            "-----"
            "XXXXX"
            "-----"
        ),
    ),
    Prize(
        value=5,
        mask=str_to_mask(
            "X---X"
            "-----"
            "X---X"
        ),
    ),
]

#Initializes all the game data
def init(seed=None):
    random.seed(seed)
    return Player(
        game=Game(prizes=PRIZES),
        cards=[Card(draw(15)) for _ in xrange(5)], #Draws 5 possible player cards with 15 random numbers each
        balance=1000,
    )


def main(nplays=38785):
    player = init(seed=0)
    with suppress_log():
        for _ in xrange(nplays-1):
            player.play(bet=random.choice([1, 2, 3]))
    player.play(bet=random.choice([1, 2, 3]))
    return player


if __name__ == "__main__":
    main()
