from pypokerengine.players import BasePokerPlayer
from neuralnetwork import neuralnetwork
from neuralnetwork import feedForward

class NNPlayer(BasePokerPlayer):

    def __init__(self, dimensions, activationFunction):
        self.neuralnetwork = neuralnetwork.ArtificialNeuralNetwork(dimensions, activationFunction)
        #create a neural network for the player

    def declare_action(self, valid_actions, hole_card, round_state):
        street = round_state["street"]
        pot = round_state["pot"["main"]]
        community_card = round_state["community_card"]
        NNinput = [hole_card, community_card, int(street == "flop"), int(street == "turn"), int(street == "river"), pot]
        #pseudocode for the input of the neural network

        move = self.neuralnetwork.generateMove(NNinput)
        #use the generateMove function to generate a move, returns (0,1,2)

        action_info = valid_actions[move]
        #get the action info for pypokerengine corresponding to the move

        action, amount = action_info["action"], action_info["amount"]

        if(move == 2):
            amount = amount["min"]
        #if the move == 'raise', set the riase amount

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
