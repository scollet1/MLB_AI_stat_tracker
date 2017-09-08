# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    construct.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: scollet <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/09/06 14:58:34 by scollet           #+#    #+#              #
#    Updated: 2017/09/06 14:58:35 by scollet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import xml.etree.ElementTree as ET
import objects
import random
from copy import deepcopy
import os.path

'''
def fighters(data_file):
    profile = ET.parse(data_file).getroot()
    fighter_list = {}
    for fighters in profile:
        for fighter in fighters:
            #print fighters.get('id')
        fighter_list['brawler.ID'] = deepcopy(brawler)
    return fighter_list
'''

def fights(data_file):
    for i in range(171):
        if os.path.isfile(str(i) + '.xml'):
            schedule = ET.parse(str(i) + '.xml').getroot()
            fight_list = {}
            #print i
            for summary in schedule:
                for events in summary:
                    for event in events:
                        for fights in event:
                            #for fight in fights:
                            this = objects.Fight()
                            this.ID = fights.get('id')
                            #print this.ID, "\n\n"
                            for fight in fights:
                                j = 0
                                fight_list['this.ID'] = {}
                                for fighters in fight:
                                    if j > 1 or fighters.get('id') is None:
                                        break
                                    brawler = objects.Fighter()
                                    brawler.ID = fighters.get('id')
                                    if fighters.get('height') is not None:
                                        brawler.height = fighters.get('height')
                                    else:
                                        brawler.height = random.int(63, 75)
                                    if fighters.get('weight') is not None:
                                        brawler.weight = fighters.get('weight')
                                    else:
                                        brawler.height = random.int(125, 265)
                                    if fighters.get('reach') is not None:
                                        brawler.reach = fighters.get('reach')
                                    else:
                                        brawler.reach = random.int(67, 77)
                                    brawler.stance = fighters.get('stance')
                                    if fighters.get('wins') is not None:
                                        brawler.wins = fighters.get('wins')
                                    else:
                                        brawler.wins = 0
                                    if fighters.get('losses') is not None:
                                        brawler.losses = fighters.get('losses')
                                    else:
                                        brawler.losses = 0
                                    if fighters.get('draw') is not None:
                                        brawler.draws = fighters.get('draws')
                                    else:
                                        brawler.draws = 0
                                    if fighters.get('no_contest') is not None:
                                        brawler.no_contest = fighters.get('no_contest')
                                    else:
                                        brawler.no_contest = 0
                                    #print "j", j
                                    #print "fighters ID???? ", fighters.get('id')
                                    this.fID[j] = deepcopy(fighters.get('id'))
                                    #print this.fID[j]
                                    j += 1
                                    for result in fights:
                                        if result.get('winner') == this.fID[0]:
                                            this.winner[0] = 1
                                            this.winner[1] = 0
                                        elif result.get('winner') == this.fID[1]:
                                            this.winner[1] = 1
                                            this.winner[0] = 0
                                        else:
                                            this.winner[0] = 0.5
                                            this.winner[1] = 0.5
                                            this.draw = result.get('draw')
                                    fight_list['this.ID']['brawler.ID'] = brawler
                                fight_list['this.ID']['results'] = this
        else:
            pass
    return fight_list
