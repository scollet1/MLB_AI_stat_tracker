# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    get.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: scollet <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/09/05 21:56:29 by scollet           #+#    #+#              #
#    Updated: 2017/09/05 21:56:30 by scollet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import xml.etree.ElementTree as ET
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#~~~~ Mixed Martial Arts ~~~~~#

MMA_SCHEDULE = 'http://api.sportradar.us/mma-t1/schedule.xml?api_key=cpw46kyxtj5upqgn3xm57au2'
#MMA_RESULTS = ''
MMA_PARTICIPANTS = 'http://api.sportradar.us/mma-t1/profiles.xml?api_key=cpw46kyxtj5upqgn3xm57au2'
#MMA_PROFILE =


#def MMA_EVENTS():
    #schedule = requests.get(MMA_SCHEDULE)
    #with open('schedule.xml', 'w') as f:
    #    f.write(schedule.text)
    #for i in range(1):

def MMA():
    data = {}
    #schedule = request.get(MMA_SCHEDULE)
    #results = request.get(MMA_RESULTS)
    participants = requests.get(MMA_PARTICIPANTS)
    #profile = request.get(MMA_PROFILE)
    #data['schedule'] = schedule
    #data['participants'] = participants
    with open('data.xml', 'w') as f:
        f.write(participants.text)
    #return data

def NHL():
    pass

def MLB():
    pass


'''
THE IDEA IS TO MAKE A GET:REQUEST TO THE DATABSE AND STORE THE RESULTS IN A DICTIONARY \
WHICH WE CAN THEN USE TO POPULATE OUR OBJECTS LATER ON ::

FOR NOW I AM SIMPLY SAVING THE RAW XML FORMAT ON A HANDFUL OF DATA AND WORKING WITH THIS IN MIND
'''

def get_XML():
    schedule = ET.parse('').getroot()
    number = 0
    for i in range(1):
        for events in schedule:
            for event in events:
                get_req = event.get('id')
                this_event = requests.get(
                'http://api.sportradar.us/mma-t1/events/' +
                get_req + '/summary.xml?api_key=cpw46kyxtj5upqgn3xm57au2')
                with open(str(number) + '.xml', 'w') as f:
                    f.write(this_event.text)
                number += 1

    pull('schedule.xml')

get_XML()
