class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.text_scores = ["Love","Fifteen","Thirty","Forty"]

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1
        
    def get_score(self):
        if self.player1_score >= 4 or self.player2_score >= 4:
            score_difference = self.player1_score - self. player2_score

            if score_difference == 0:
                return "Deuce"
            elif score_difference == 1:
                return "Advantage player1"
            elif score_difference == -1:
                return "Advantage player2"
            elif score_difference >= 2:
                return "Win for player1"
            else:
                return "Win for player2"
        else:
            if self.player1_score == self.player2_score:
                return f"{self.text_scores[self.player1_score]}-All"
            else:
                return f"{self.text_scores[self.player1_score]}-{self.text_scores[self.player2_score]}"
