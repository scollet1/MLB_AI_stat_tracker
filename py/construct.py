# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    construct.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: scollet <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/09/08 12:54:51 by scollet           #+#    #+#              #
#    Updated: 2017/09/08 12:54:53 by scollet          ###   ########.fr        #
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
		#print float(fighters.get('id')
	fighter_list['brawler.ID'] = deepcopy(brawler)
	return fighter_list
'''

def fights(data_file):
	fight_list = {}
	for i in range(171):
		if os.path.isfile("../xml_data/" + str(i) + '.xml'):
			schedule = ET.parse("../xml_data/" + str(i) + '.xml').getroot()
			for summary in schedule:
				for events in summary:
					for event in events:
						#print event.get('id')
						for fights in event:
							this = objects.Fight()
							this.ID = fights.get('id')
							#print this.ID
							fight_list[this.ID] = {}
							for fight in fights:
								j = 0
								for fighters in fight:
									if j > 1 or fighters.get('id') is None:
										break
									brawler = objects.Fighter()
#									fight_list[this.ID][brawler.ID] = {}
									brawler.ID = fighters.get('id')
#									if fighters.get('name') is None:
#										break
									brawler.name = fighters.get('first_name') + fighters.get('last_name')
									if fighters.get('height') is not None and fighters.get('height'):
#										print fighters.get('height')
#										print float(fighters.get('height'))
										brawler.height = float(fighters.get('height'))
									else:
										brawler.height = random.randint(63, 75)
									if fighters.get('weight') is not None:
										brawler.weight = float(fighters.get('weight'))
									else:
										brawler.height = random.int(125, 265)
									if fighters.get('reach') is not None and fighters.get('reach'):
#										print fighters.get('reach')
										brawler.reach = float(fighters.get('reach'))
									else:
										brawler.reach = random.randint(67, 77)
									brawler.stance = fighters.get('stance')
									for record in fighters:
										if record.get('wins') is not None:
											brawler.wins = float(record.get('wins'))
										else:
											brawler.wins = 0
										if record.get('losses') is not None:
											brawler.losses = float(record.get('losses'))
										else:
											brawler.losses = 0
										if record.get('draw') is not None:
											brawler.draws = float(record.get('draws'))
										else:
											brawler.draws = 0
										if record.get('no_contest') is not None:
											brawler.no_contest = float(record.get('no_contest'))
										else:
											brawler.no_contest = 0
									this.fID[j] = deepcopy(fighters.get('id'))
									#print j
									j += 1
									fight_list[this.ID][brawler.ID] = deepcopy(brawler)
									#print "wins : ", fight_list[this.ID][brawler.ID].wins
#									if this.ID == "94c2f012-03a8-423a-a47e-a4f0c5f9a991" or this.ID == "65be909f-f2f6-4361-b317-6ada02ded8aa":
#										print "mark ---- ", this.ID, brawler.ID
#									else:
#										print this.ID, brawler.ID
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
							#print this.ID
							fight_list[this.ID]['results'] = this
							#print fight_list[this.ID]['results'].winner
		else:
			pass
	return fight_list
