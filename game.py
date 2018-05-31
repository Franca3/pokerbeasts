from pypokerengine.api.game import setup_config, start_poker
from fish_player import FishPlayer
from human_player.human_player import HumanPlayer
from neuralnetwork.NNPlayer import NNPlayer
from neuralnetwork import feedForward

if (__name__ == "__main__" ):
    config = setup_config(max_round=10, initial_stack=100, small_blind_amount=5)
    config.register_player(name="p1", algorithm=FishPlayer() )
    config.register_player(name="p2", algorithm=FishPlayer() )
    #config.register_player(name="hm", algorithm=HumanPlayer() )
    #config.register_player(name="p3", algorithm=FishPlayer())
    config.register_player(name='neuralnetwork', algorithm = NNPlayer([7,11,3],feedForward.sigmoid) )
    game_result = start_poker(config, verbose = 1)

    print(game_result)
