from pypokerengine.players import BasePokerPlayer
from neuralnetwork import neuralnetwork
from deuces.card import Card
from deuces.evaluator import Evaluator

class NNPlayer(BasePokerPlayer):

    def __init__(self, dimensions, activationFunction):
        self.neuralnetwork = neuralnetwork.ArtificialNeuralNetwork(dimensions, activationFunction)
        #create a neural network for the player

    def calculateHand(self, hole_card, round_state):
        """ 
        Passes what's on table and in your hand to deuces,
        to calculate hand strength,
        if the flop hasnt been played yet, return -1
        """
        if( round_state["community_card"] == []):
            return -1
            
        board = list( map(lambda x: Card.new(x[-1] + x[0].lower() ), round_state["community_card"] ) )

        hand = list( map(lambda x: Card.new(x[-1] + x[0].lower() ), hole_card) )
        evaluator = Evaluator()
        return evaluator.evaluate(board, hand)

    def generateInput(self, valid_actions, hole_card, round_state):
        print( self.calculateHand( hole_card, round_state) )

        street = round_state["street"]
        #get the current street from the round state
        pot = valid_actions[1]["amount"] / round_state["pot"]["main"]["amount"]
        #amount to raise (action 1) over the amount in the pot
        community_card = round_state["community_card"]

        if round_state["action_histories"][list(round_state["action_histories"].keys())[-1]] != []: 
            last_action = round_state["action_histories"][list(round_state["action_histories"].keys())[-1]][-1]["action"] 
        else:
            last_action = "FIRST TO PLAY"


        #NNinput = [hole_card, community_card, int(street == "flop"), int(street == "turn"), int(street == "river"), int(last_action == "RAISE", pot]
        NNinput = [1, 1, street == "flop", street == "turn", street == "river", last_action == "RAISE", pot]
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
