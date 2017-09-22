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
from sklearn.model_selection import train_test_split

EPOCHS = 1
FILE_NAME = "../fight_data.csv"

#def update_weights(agent, data):


#def backward_propagate(agent, data):


#def forward_propagate(agent, data):


def train(agent):
	seed = 9
	np.random.seed(seed)
	dataset = np.loadtxt(FILE_NAME, delimiter=',')
	X = dataset[:,0:14]
	Y = dataset[:,14:]
	print X, Y
	(X_train, X_test, Y_train, Y_test) = train_test_split(X, Y, test_size=0.33, random_state=seed)
	agent.model.fit(X_train, Y_train, validation_data=(X_test, Y_test), nb_epoch=200, batch_size=5, verbose=0)
