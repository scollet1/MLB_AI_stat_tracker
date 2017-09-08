# **************************************************************************** #
#									   #
#							  :::	   ::::::::    #
#	construct.py					:+:	 :+:	:+:    #
#						  	+:+ +:+		  +:+	   #
#	By: scollet <marvin@42.fr>		+#+  +:+	   +#+		   #
#						+#+#+#+#+#+	+#+		   #
#	Created: 2017/09/06 14:58:34 by scollet	   	#+#	  #+#		   #
#	Updated: 2017/09/06 14:58:35 by scollet	###	########.fr		   #
#										   #
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
	for i in range(171):
		if os.path.isfile(str(i) + '.xml'):
			schedule = ET.parse(str(i) + '.xml').getroot()
			fight_list = {}
			for summary in schedule:
				for events in summary:
					for event in events:
						for fights in event:
							this = objects.Fight()
							this.ID = fights.get('id')
							for fight in fights:
								j = 0
								fight_list[this.ID] = {}
								for fighters in fight:
									if j > 1 or fighters.get('id') is None:
										break
									brawler = objects.Fighter()
									brawler.ID = fighters.get('id')
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
									if fighters.get('reach') is not None or fighers.get('reach'):
#										print fighters.get('reach')
										pass
#										brawler.reach = float(fighters.get('reach'))
									else:
										brawler.reach = random.randint(67, 77)
									brawler.stance = fighters.get('stance')
									if fighters.get('wins') is not None:
										brawler.wins = float(fighters.get('wins'))
									else:
										brawler.wins = 0
									if fighters.get('losses') is not None:
										brawler.losses = float(fighters.get('losses'))
									else:
										brawler.losses = 0
									if fighters.get('draw') is not None:
										brawler.draws = float(fighters.get('draws'))
									else:
										brawler.draws = 0
									if fighters.get('no_contest') is not None:
										brawler.no_contest = float(fighters.get('no_contest'))
									else:
										brawler.no_contest = 0
									this.fID[j] = deepcopy(fighters.get('id'))
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
									fight_list[this.ID][brawler.ID] = brawler
								fight_list[this.ID]['results'] = this
		else:
			pass
	return fight_list
