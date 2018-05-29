from pypokerengine.players import BasePokerPlayer

class HumanPlayer(BasePokerPlayer):
    """
    A command line based interface to play along
    """
    def __init__(self):
        self.name = input("Enter your name: ")

    def declare_action(self, valid_actions, hole_card, round_state):
        optionDict = { "F":0 , "C":1 , "R":2 } 
        print( self.name, ", it's your turn!")
        print("Your cards are: ", hole_card)
        chosen = input("(R)aise, (F)old, (C)all: " )

        try:
            action_info = valid_actions[ optionDict[chosen] ]
        except KeyError:
            # Assume to call if the input is incorrect
            action_info = valid_actions[1]
        
        action, amount = action_info["action"], action_info["amount"]
        if(chosen == "R"):
            amount = amount["min"]
        return action, amount
         
        
    def receive_game_start_message(self, game_info):
        pass

    def receive_round_start_message(self, round_count, hole_card, seats):
        pass

    def receive_street_start_message(self, street, round_state):
        pass

    def receive_game_update_message(self, action, round_state):
        pass

    def receive_round_result_message(self, winners, hand_info, round_state):
        pass

