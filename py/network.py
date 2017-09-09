# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    agent.py         	                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: scollet <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/09/06 14:18:36 by scollet           #+#    #+#              #
#    Updated: 2017/09/06 14:18:37 by scollet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import sys

EPISODES = 750


#def update_weights(agent, data):


#def backward_propagate(agent, data):


#def forward_propagate(agent, data):


def train(agent, fight_data):
	#print "hello???"
	for e in range(1):
		for each, fight in fight_data.items():
			print "fight id : ", each
			X = []
			j = 0
			for this, fighter in fight.items():
				if this == 'results':
					break
				print "fighter id : ", this
				X.append(fighter.weight)
				X.append(fighter.height)
				X.append(fighter.reach)
				X.append(fighter.wins)
				X.append(fighter.losses)
				X.append(fighter.draws)
				X.append(fighter.no_contest)
			print "clues thar be - ", X
			X = np.array(X)
			X = X.reshape((1, 14))
			#print X
			y = fight['results'].winner
			y = np.array(y)
#			print y
			y = np.reshape(y, (1, 2))
			#print y
			agent.train(X, y)
			score = agent.model.evaluate(X, y, batch_size=128)
			print "accuracy --- ", score[1], "time --- ", e
