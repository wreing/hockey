#!/usr/bin/env python

import csv
import argparse
import elo

def main():
    parser = argparse.ArgumentParser(description='Compute Elos from a csv of game stats')
    parser.add_argument('games',
                    help='csv formated match results')
    args = parser.parse_args()

    e = elo.elo()

    csvfile = open(args.games, 'rb')

    csvDict = csv.DictReader(csvfile, fieldnames=['date','away_team','away_score','home_team','home_score', 'overtime','type' ], delimiter=',')

    #Build the distinct list of teams
    for row in csvDict:
        e.add_team(row['home_team'])
        e.add_team(row['away_team'])


    #Process the games
    csvfile = open(args.games, 'rb')
    csvDict = csv.DictReader(csvfile, fieldnames=['date','away_team','away_score','home_team','home_score', 'overtime','type' ], delimiter=',')

    for row in csvDict:
        try:
            e.play_match(row['home_team'], int(row['home_score']), row['away_team'], int(row['away_score']), False, 30, 1)
        except ValueError:
            print row


    for team in e.teams:
        print team + ',' + str(e.teams[team].elo) +',' + str(e.teams[team].matches)



if __name__ == '__main__':
    main()
