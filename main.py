# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line

#Opd part 

class Player:
    def __init__(self,name:str, speed:float,endurance:float,accuracy:float):
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy              
        if speed > 1 or speed < 0:
            raise ValueError (f'speed must be between 0 and 1')
        if endurance > 1 or endurance < 0:
            raise ValueError(f'endurence must be between 0 and 1')
        if accuracy > 1 or accuracy < 0:
            raise ValueError(f'accuracy must be between 0 and 1')
        
    def introduce(self):
        return f'Hello everyone, my name is Super,{self.name}'


    def strength(self):
        if self.speed > self.endurance > self.accuracy:
                return ('speed', self.speed)
        elif self.endurance > self.accuracy:
            return ('endurance', self.endurance)
        else:
            return ('accuracy', self.accuracy)   
 
#Opd part 2   

class Commentator:
    def __init__(self, name:str):
        self.name = name
        
    def sum_player(self, player): 
        return player.speed + player.endurance + player.accuracy
    
    def compare_players(self, play_1, play_2, strength): 
        
        player_one_strength = getattr(play_1, strength)
        player_two_strength = getattr(play_2, strength)
        
        if player_one_strength > player_two_strength:
            return play_1.name
        elif player_one_strength < player_two_strength:
            return play_2.name
        elif play_1.strength()[1] > play_2.strength()[1]:
            print('test')
            return play_1.name
        elif play_2.strength()[1] > play_1.strength()[1]:
            print('test')
            return play_2.name
        elif self.sum_player(play_1) > self.sum_player(play_2):
            print('test1')
            return play_1.name
        elif self.sum_player(play_2) > self.sum_player(play_1):
            print('test1')
            return play_2.name
        else:
            return 'These two players might as well be twins!'

        
ray = Commentator('Ray Hudson')
print(ray.name)
alice = Player('Alice',0.8, 0.2, 0.6)
bob = Player('Bob', 0.9, 0.2, 0.6)
print(ray.compare_players(alice, bob, 'speed'))