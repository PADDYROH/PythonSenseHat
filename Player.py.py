class Player:

    def __init__(self,name):
    	self.__score = 0
    	self.__name = name

    def add_to_score(self,score_to_add):
    	if score_to_add > 0 and score_to_add <= 6:
    		self.__score += score_to_add
    	else:
    		print("Not Valid Score")

    def get_score(self):
    	return self.__score

    def get_name(self):
    	return self.__name