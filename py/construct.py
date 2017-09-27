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
									brawler.ID = fighters.get('id')
									brawler.name = fighters.get('first_name') + fighters.get('last_name')
									if fighters.get('height') is not None and fighters.get('height'):
										brawler.height = float(fighters.get('height'))
									else:
										brawler.height = random.randint(63, 75)
									if fighters.get('weight') is not None:
										brawler.weight = float(fighters.get('weight'))
									else:
										brawler.height = random.int(125, 265)
									if fighters.get('reach') is not None and fighters.get('reach'):
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
									j += 1
									fight_list[this.ID][brawler.ID] = deepcopy(brawler)
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
							fight_list[this.ID]['results'] = this
		else:
			pass
	return fight_list
