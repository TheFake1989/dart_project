from models.kast import *
from models.rules import *

class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.throws = []
        self.game = None
    
    #dart are recorded as tuples, with value @first_index, and multiplier @second_index
    def record_round(self, dart_1, dart_2, dart_3):
        dart_1_value = throw(dart_1)
        dart_2_value = throw(dart_2)
        dart_3_value = throw(dart_3)
        round_darts = [dart_1_value, dart_2_value, dart_3_value]
        round_score = dart_1_value + dart_2_value + dart_3_value

        if self.game == "shoot_down":
            if round_score < self.score:
                self.score -= round_score
                print(f"Dart 1 = {dart_1_value}, Dart 2 = {dart_2_value}, Dart 3 = {dart_3_value}, ")
                print(f"Points remaining {self.score}")
                self.throws.append(round_darts)
                return
            
            if round_score > self.score:
                self.throws.append(round_darts)
                return

            if round_score == self.score:
                if dart_1_value == self.score and dart_1[1] == 2:
                    self.score -= dart_1_value
                    print("WINNER!")
                    return
                elif dart_1_value + dart_2_value == self.score and dart_2[1] == 2:
                    self.score -= dart_1_value + dart_2_value
                    print("WINNER!")
                    return
                
                elif dart_3[1] == 2:
                    self.score -= round_score
                    print("WINNER!")
                    return
                else: 
                    print("Bust")
                    return