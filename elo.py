#!/usr/bin/env python

'''
See:
    http://en.wikipedia.org/wiki/World_Football_Elo_Ratings

Rn - R0 + K x G x (W -We)
Rn = is the new rating
Ro = is the old (pre-match) rating

K  = is the weight constant for the tournament played:
G  = Goal Differential
   =  0 = 1
   =  1 = 1
   =  2 = 1.5
   = >2 = (11+N)/8

W  = is the result of the game (1 for a win, 0.5 for a draw, and 0 for a loss).
We = is the expected result (win expectancy), either from the chart or the following formula:
   = 1/ 10 ^(dr/400) + 1

'''

class team:
    def __init__(self, name):
        self.name    = name
        self.elo     = 1500
        self.matches = 0

class elo:

    def __init__(self):
        self.teams = {}

    def add_team(self, t):
        self.teams[t] = team(t)

    def play_match(self, home_team, home_score, visitor_team, visitor_score, neutral=False, k=20, add_match=0):
        h = self.teams[home_team]
        v = self.teams[visitor_team]

        h.matches = h.matches + add_match
        v.matches = v.matches + add_match

        if home_score > visitor_score:
            W = 1.0
        elif home_score == visitor_score:
            W = 0.5
        elif home_score < visitor_score:
            W = 0.0

        G_1 = abs(home_score - visitor_score)
        if G_1 == 0 or G_1 == 1:
            G = 1.0
        elif G_1 == 2:
            G = 1.5
        else:
            G = (11.0+G_1)/8.0

        if (neutral == False):
            dr = (h.elo - v.elo + 100)
        else:
            dr = (h.elo - v.elo)


        W_e = 1.0/(10.0**(-dr/400.0) + 1.0)

        P = k * G*(W - W_e)

        h.elo = h.elo + P
        v.elo = v.elo - P


def main():
    # Test netural field single game numbers from wikipedia
    e = elo()
    e.add_team('pats')
    e.add_team('jets')

    e.teams['pats'].elo =630
    e.teams['jets'].elo =500

    e.play_match('pats',3, 'jets',1, True)

    if round(e.teams['pats'].elo) != 640:
        print "Pats = ", e.teams['pats'].elo
    if round(e.teams['jets'].elo) != 490:
        print "Jets = ", e.teams['jets'].elo



if __name__ == '__main__':
    main()



