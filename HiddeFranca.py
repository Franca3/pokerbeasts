import pypokerengine
from pypokerengine.players import BasePokerPlayer
import random

class FishPlayer(BasePokerPlayer):  # Do not forget to make parent class as "BasePokerPlayer"

    #  we define the logic to make an action through this method. (so this method would be the core of your AI)
    def declare_action(self, valid_actions, hole_card, round_state):
        totaalkaarten=hole_card+round_state['community_card']
        print(totaalkaarten)
        #print(round_state)
        print(valid_actions)
        
        
        # valid_actions format => [fold_action_info, call_action_info, raise_action_info]
        call_action_info = valid_actions[1]
        action, amount = call_action_info["action"], call_action_info["amount"]
        return action, amount   # action returned here is sent to the poker engine
    
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

class FishPlayerHiddeFranca(BasePokerPlayer):  

    def berekenafstand(self,handkaarten):   #Geef een waarde aan een hand
        afstandtabel={0:10,1:5,2:3,3:2,4:1}
        if handkaarten[0][1]==14: #een aas kan als 1 of als 14 gelden, bij het bepalen van de afstand moeten we beide opties bekijken.
            a=abs(handkaarten[0][1]-handkaarten[1][1])
            b=abs(1-handkaarten[1][1])
            afstand1=min(a,b)
        elif handkaarten[1][1]==14:
            a=abs(handkaarten[0][1]-handkaarten[1][1])
            b=abs(1-handkaarten[0][1])
            afstand1=min(a,b)
        else:    
            afstand1=abs(handkaarten[0][1]-handkaarten[1][1])
        if afstand1 in afstandtabel:
            return afstandtabel[afstand1]
        else:
            return 0
        
    def kaartennaarLijst(self,kaarten):
                #We wijzen aan elke kaart een waarde toe, de kleuren laten we hun naam behouden.
        kaartWaarden={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
        totaalkaarten2=[]
        for a in kaarten:
            lijst=[]
            lijst.append(a[0])
            lijst.append(kaartWaarden[a[1]])
            totaalkaarten2.append(lijst)
        return totaalkaarten2
    
    def declare_action(self, valid_actions, hole_card, round_state): #Hier begint de actie
        totaalkaarten=hole_card+round_state['community_card']
        print(totaalkaarten)
        print(valid_actions)
        
        randomgetal=random.randint(1,4)
        # valid_actions format => [fold_action_info, call_action_info, raise_action_info]
        fold_action_info = valid_actions[0]
        call_action_info = valid_actions[1]
        raise_action_info = valid_actions[2]
            
        kaartenlijst = self.kaartennaarLijst(totaalkaarten)
        if len(kaartenlijst)==2:
            score = self.berekenafstand(kaartenlijst)
            print(score)
            
        
        #Inzet afhankelijk van random getal
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
    
from pypokerengine.api.game import setup_config, start_poker

config = setup_config(max_round=10, initial_stack=100, small_blind_amount=5)
config.register_player(name="p1", algorithm=FishPlayer())
config.register_player(name="p2", algorithm=FishPlayer())
config.register_player(name="p3", algorithm=FishPlayerHiddeFranca())
game_result = start_poker(config, verbose=1)

print(game_result)
