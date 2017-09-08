# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    agent.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: scollet <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/09/06 14:18:36 by scollet           #+#    #+#              #
#    Updated: 2017/09/06 14:18:37 by scollet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

EPISODES = 750


#def update_weights(agent, data):


#def backward_propagate(agent, data):


#def forward_propagate(agent, data):


def train(agent, fight_data):
    #print "hello???"
    for each, fight in fight_data.items():
        print each
        X = []
        j = 0
        for fighter in fight.items():
            #print each
            if each == 'results':
                break
            X.append(fighter.weight)
            X.append(fighter.height)
            X.append(fighter.reach)
            X.append(fighter.wins)
            X.append(fighter.losses)
            X.append(fighter.draws)
            X.append(fighter.no_contest)
            #print j
            #j += 1
        X = np.asarray(X)
        print X
        y = fight['results'].winner
        print y
        #print fight['results'].winner[0]
        #if fight.fID[0] in data['fighters']:
        #        print data['fighters'][fight.fID[0]].height
        agent.train(X, y)
        score = model.evaluate(X, y, batch_size=128)
