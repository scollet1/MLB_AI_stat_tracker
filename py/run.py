# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    run.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: scollet <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/09/05 21:56:10 by scollet           #+#    #+#              #
#    Updated: 2017/09/05 21:56:13 by scollet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import xml.etree.ElementTree as ET
#import get
import sys
import random
import objects
import requests
import construct
import network
import csv
from copy import deepcopy
#class Person_Object():

#class Agent():
EPOCHS = 500
TRAIN_FILE_NAME = "../train_data.csv"
FIGHT_FILE_NAME = "../predict_data.csv"
#run(sys.argv[1])
#get.MMA_EVENTS()
#fighter_list = parse('data.xml')
#feed(fighter_list)
#def pull(data_file):

def write_file(fight_data, fname):
    with open(fname, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter = ',')
	if fname == TRAIN_FILE_NAME:
	        for each, fight in fight_data.items():
			windex = 0
			array = []
			for each, fighter in fight.items():
				if each == 'results':
                	    		continue
		                array.append(fighter.weight)
        		        array.append(fighter.height)
				array.append(fighter.reach)
       	        	 	array.append(fighter.wins)
      	 	         	array.append(fighter.losses)
       	       		  	array.append(fighter.draws)
               	 		array.append(fighter.no_contest)
            		array.append(fight['results'].winner[0])
	            	array.append(fight['results'].winner[1])
			writer.writerow(array)
	elif fname == FIGHT_FILE_NAME:
		i = 0
#		sorted(fight_data)
		for each, fight in fight_data.items():
			windex = 0
#			sorted(fight)
			for each, fighter in fight.items():
				i += 1
#				print i
	                        array = []
				if each == 'results':
                                        continue
                                array.append(fighter.name.replace(" ", ""))
				array.append(fighter.weight)
                                array.append(fighter.height)
                                array.append(fighter.reach)
                                array.append(fighter.wins)
                                array.append(fighter.losses)
                                array.append(fighter.draws)
                                array.append(fighter.no_contest)
                        	writer.writerow(array)

def run(arg, f1, f2):
	if arg == '--train':
		agent = objects.Agent(14, 2)
           	fight_data = construct.fights('../xml_data/schedule.xml')
            	write_file(fight_data, TRAIN_FILE_NAME)
	        network.train(agent)
	elif arg == '--predict':
		agent = objects.Agent(14, 2)
		fight_data = construct.fights('../xml_data/schedule.xml')
		write_file(fight_data, FIGHT_FILE_NAME)
		network.predict(agent, f1.replace(" ", ""), f2.replace(" ", ""))
	print "Arguments Processed!"

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2], sys.argv[3])
