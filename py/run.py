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
FILE_NAME = "../fight_data.csv"

'''
def feed(data):
    network = objects.Network()
    for episode in range(EPOCHS):
        pass

def run(query):
    if query == "MMA":
        get.MMA()
        parse('data.xml')
    elif query == "parse":
        parse('data.xml') # NOTE : THIS DOES NOT REFLECT THE END IMPLEMENTATION !!!
    else:
        sys.exit(0)
    #parse(data)
    #feed(data)
'''

#run(sys.argv[1])
#get.MMA_EVENTS()
#fighter_list = parse('data.xml')
#feed(fighter_list)
#def pull(data_file):

def write_to_file(fight_data):
    with open(FILE_NAME, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter = ',')
        for each, fight in fight_data:
            for each, fighter in fight_data:
                writer.write(fighter.weight)
                writer.write(fighter.weight)
                writer.write(fighter.weight)
                writer.write(fighter.weight)
                writer.write(fighter.weight)
                writer.write(fighter.weight)
                writer.write(fighter.weight)
                writer.write(fighter.weight)
            writer.write()
            writer.write('\n')

def run():
    agent = objects.Agent(14, 2)
    fight_data = {}
    #data['fighters'] = construct.fighters('data.xml')
    fight_data = construct.fights('schedule.xml')
    #for each, fight in fight_data.items():
    #    print each
#   sys.exit(0)
#   write_to_file(fight_data)
    network.train(agent, fight_data)

run()
