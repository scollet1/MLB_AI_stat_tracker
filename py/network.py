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
TRAIN_FILE_NAME = "../train_data.csv"
FIGHT_FILE_NAME = "../predict_data.csv"
SAVE_MODEL = "../Trained.h5"

#def update_weights(agent, data):


#def backward_propagate(agent, data):


#def forward_propagate(agent, data):

def predict(agent, f1, f2):
	agent.model.load_weights(SAVE_MODEL)
	dataset = np.loadtxt(FIGHT_FILE_NAME, dtype={'names': ('name', 'weight', 'height', 'reach', 'wins', 'losses', 'draws', 'no_contest'),
          'formats': ('|S15', np.float, np.float, np.float, np.float, np.float, np.float, np.float)}, delimiter=',')
#	print dataset
	F1 = []
	F2 = []
#	print f1, f2
#	test = [2, 3, 4, 5, 6]
#	print test
	testing = 0
	no_f1 = True
	no_f2 = True
	if testing:
		for index, row in enumerate(dataset):
                	if index == f1:
                	        F1 = list(dataset[index])
                	elif index == f2:
                        	F2 = list(dataset[index])
	else:
		for row in dataset:
#			print row
#			print row[0]
			if row[0] == f1:
				F1 = list(row)
				no_f1 = False
#				print F1
			elif row[0] == f2:
				F2 = list(row)
				no_f1 = False
#				print F2
	
	if no_f1 and no_f2:
		print "Neither fighter exists in our database, try again!"
		sys.exit(1)
	elif no_f1:
		print "Fighter One does not exist in our database, try again!"
		sys.exit(1)
#	elif no_f2:
#		print "Fighter Two does not exist in our data base, try again!"
#		sys.exit(1)
	F1 = F1[1:]
	F2 = F2[1:]
#	print F1, F2
	X = np.array([F1 + F2])
#	print X, "\n"
	print agent.model.predict(X)

def train(agent):
	if SAVE_MODEL is not None:
		agent.model.load_weights(SAVE_MODEL)
	seed = 9
	np.random.seed(seed)
	dataset = np.loadtxt(TRAIN_FILE_NAME, delimiter=',')
	X = dataset[:,0:14]
	Y = dataset[:,14:]
#	print X, Y
	(X_train, X_test, Y_train, Y_test) = train_test_split(X, Y, test_size=0.33, random_state=seed)
	agent.model.fit(X_train, Y_train, validation_data=(X_test, Y_test), epochs=200, batch_size=5, verbose=0)
	for row in X_test:
#		print row
		this = np.array([row])		
		print agent.model.predict(this)
	agent.model.save_weights(SAVE_MODEL)
