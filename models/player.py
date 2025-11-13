from models.throw_logic import *
from models.rules import *

class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.throws = []
        self.game = None
        self.winner = False
    
    #dart are recorded as tuples, with value @first_index, and multiplier @second_index
    def record_round(self, dart_1, dart_2, dart_3):
        dart_1_value = dart_1[0] * dart_1[1]
        dart_2_value = dart_2[0] * dart_2[1]
        dart_3_value = dart_3[0] * dart_3[1]
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
                print("Bust")
                print(f"Reset to {self.score}")
                return

            if round_score == self.score:
                if dart_1_value == self.score and dart_1[1] == 2:
                    self.score -= dart_1_value
                    self.winner = True
                    print("WINNER!")
                    return
                elif dart_1_value + dart_2_value == self.score and dart_2[1] == 2:
                    self.score -= dart_1_value + dart_2_value
                    self.winner = True
                    print("WINNER!")
                    return
                
                elif dart_3[1] == 2:
                    self.score -= round_score
                    self.winner = True
                    print("WINNER!")
                    return

                else:
                    self.throws.append(round_darts)
                    print("Bust")
                    print(f"Reset to {self.score}")
                return