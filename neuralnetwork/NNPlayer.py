from pypokerengine.players import BasePokerPlayer
from neuralnetwork import neuralnetwork

class NNPlayer(BasePokerPlayer):

    def __init__(self, dimensions, activationFunction):
        self.neuralnetwork = neuralnetwork.ArtificialNeuralNetwork(dimensions, activationFunction)
        #create a neural network for the player

    def generateInput(self, valid_actions, hole_card, round_state):
        street = round_state["street"]
        #get the current street from the round state
        pot = valid_actions[1]["amount"] / round_state["pot"]["main"]["amount"]
        #amount to raise (action 1) over the amount in the pot
        community_card = round_state["community_card"]

        last_action = round_state["action_histories"][list(round_state["action_histories"].keys())[-1]][-1]["action"] if round_state["action_histories"][list(round_state["action_histories"].keys())[-1]] != [] else "FIRST TO PLAY"
        #long line to retrive the action of the last player, last action is burried in tons of dictionaries

        #NNinput = [hole_card, community_card, int(street == "flop"), int(street == "turn"), int(street == "river"), int(last_action == "RAISE", pot]
        NNinput = [1, 1, int(street == "flop"), int(street == "turn"), int(street == "river"), int(last_action == "RAISE"), pot]
        #eventually use the line above, but for now set the hole_card and community_card to 1
        return NNinput

    def declare_action(self, valid_actions, hole_card, round_state):
        NNinput = self.generateInput(valid_actions, hole_card, round_state)
        #use the generateInput function to generate input

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
