import random

def get_cards_list():
    return [
        {'name': 'Ace', 'value': 1},
        {'name': 'Two', 'value': 2},
        {'name': 'Three', 'value': 3},
        {'name': 'Four', 'value': 4},
        {'name': 'Five', 'value': 5},
        {'name': 'Six', 'value': 6},
        {'name': 'Seven', 'value': 7},
        {'name': 'Eight', 'value': 8},
        {'name': 'Nine', 'value': 9},
        {'name': 'Ten', 'value': 10},
        {'name': 'Jack', 'value': 10},
        {'name': 'Queen', 'value': 10},
        {'name': 'King', 'value': 10},
    ];
    
class Player:
    
    def __init__(self, name):
        self.name = name
        
        self.cards = []
        self.aces_cards = []
        self.not_aces_cards = []
        self.total = 0
        self.initiate_cards()
        
    def initiate_cards(self):
        self.visible = self.get_random_card()
        
        self.cards.append(self.visible)
        self.cards.append(self.get_random_card())
    
    def get_random_card(self):
        rand = random.randrange(0, 12, 1)
        card = get_cards_list()[rand]
        return Card(card['name'], card['value'])
            
    def pick_card(self):
        card = self.get_random_card()
        self.cards.append(card)
    
    def get_ace_cards(self):
        for card in self.cards:
            if card.name == 'Ace':
                self.aces_cards.append(card)
        return self.aces_cards
    
    def calculate_cards(self, cards):
        total = 0
        for card in cards:
            total += card.value
        return total
    
    def get_total(self):
        all_cards_total = self.calculate_cards(self.cards)
        ace_cards_total = self.calculate_cards(self.get_ace_cards())
        
        if ace_cards_total > 0 and all_cards_total <= 11:
           # ( calculate one of aces as 11 and remove its old value )
           self.total = all_cards_total + 10
        else:
            self.total = all_cards_total
        
        return self.total

class Card:
    
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def set_card_value(self, value):
        self.value = value
    
def main():
    print(""" 
        Each player will has 2 cards, one of them is
        visible to the other player,
        each player calculate the summition of his/her cards,
        and palyer can pick a card until the total be more
        close to 21,
        for Ace it's two values (1/11) depending on
        its position at the game, by default it's 1
        but can be 11 if the total will be 21 or less,
    """)
    
    continue_playing = True
    human_finished_picking = False
    cpu_finished_picking = False
    
    cpu = Player('CPU')
    
    human_name = input('Please enter your name:\n')
    human = Player(human_name)
    
    print(f'You got {human.get_total()}, Your cards are:')
    for card in human.cards:
        print(f"{card.name}, {card.value} \n")
    
    while(continue_playing):
        while(not human_finished_picking):
            print(f'CPU has: {cpu.visible.name}, {cpu.visible.value} \n')
            
            new_pick = input('Would you like to pick a new card? \n(y for yes / anything for no):\n')
            if(new_pick == 'y'):
                human.pick_card()
                print(f'Total cards: {human.get_total()}, Your cards are:')
                for card in human.cards:
                    print(f"{card.name}, {card.value} \n")
                if(human.get_total() > 21):
                    print(f'You got {human.get_total()} more than 21, You lose :(')
                    human_finished_picking = True
                    continue_playing = False
            else:
                human_finished_picking = True

        print('=============================================')
        
        while(not cpu_finished_picking):
            if(cpu.get_total() < 17):
                cpu.pick_card()
                if(cpu.get_total() > 21):
                    print(f'CPU got {cpu.get_total()} more than 21, You Won :)')
                    cpu_finished_picking = True
                    continue_playing = False
            else:
                cpu_finished_picking = True
                continue_playing = False

    if cpu.get_total() <= 21 and  human.get_total() <= 21:
        if cpu.get_total() > human.get_total():
            print(f'CPU got {cpu.get_total()}, and you got {human.get_total()}\n YOU LOSE :(')
        else:
            print(f'CPU got {cpu.get_total()}, and you got {human.get_total()}\n YOU WON :)')

    print('=============================================')
    print(f'Your cards: {human.get_total()}, as following:')
    for card in human.cards:
        print(f"{card.name}, {card.value} \t")
    print('=============================================')
    print(f'CPU cards: {cpu.get_total()}, as following:')
    for card in cpu.cards:
        print(f"{card.name}, {card.value} \t") 
        
main()