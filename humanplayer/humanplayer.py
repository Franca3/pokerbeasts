from pypokerengine.players import BasePokerPlayer

class HumanPlayer(BasePokerPlayer):
    """
    A command line based interface to play along
    """
    def __init__(self):
        name = input("Enter your name :")

    def declare_action(self, valid_actions, hole_card, round_state):
        optionDict = { "R":0 , "C":1 , "F":2 } 
        chosen = input("(R)aise, (F)old, (C)all: " )

        try:
            call_action_info = valid_actions[chosen]
        except KeyError:
            # Assume to call if the input is incorrect
            call_action_info = valic_actions[1]
        
        action, amount = call_action_info["action"], call_action_info["amount"]
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

