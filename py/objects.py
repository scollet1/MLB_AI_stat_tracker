# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    objects.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: scollet <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/09/05 22:24:21 by scollet           #+#    #+#              #
#    Updated: 2017/09/05 22:24:22 by scollet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras import backend as K

HIDDEN_LAYERS = 2
NEURAL_DENSITY = 32
LEARNING_RATE = 0.001

class Agent():
	def __init__(self, input_size, output_size):
		self.input_size = input_size
		self.output_size = output_size
		self.learning_rate = LEARNING_RATE
		self.model = self._build_model()
		self.target_model = self._build_model()
		self.update_target_model()
	def _huber_loss(self, target, prediction):
		error = prediction - target
		return K.mean(K.sqrt(1 + K.square(error)) - 1, axis = -1)
	def _build_model(self):
		model = Sequential()
		model.add(Dense(NEURAL_DENSITY, input_dim=self.input_size, activation='relu'))
		for i in range(HIDDEN_LAYERS):
			model.add(Dense(NEURAL_DENSITY, activation='relu'))
		model.add(Dense(self.output_size, activation='softmax'))
		model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
		return model
	def update_target_model(self):
		self.target_model.set_weights(self.model.get_weights())
	def train(self, feed, target):
		self.model.fit(feed, target, epochs=1, verbose=0)
	def load(self, name):
		self.model.load_weights(name)
	def save(self, name):
		self.model.save_weights(name)


class Training():
    def __init__(self):
        self.t_list = []
    def t_list(self):
        return self._t_list

class Fight():
    def __init__(self):
        self.ID = None
        self.fID = [None] * 2
        self.winner = np.array([0.5, 0.5])
        self.draw = None
    def ID(self):
        return self._ID
    def fID(self):
        return self._f1ID
    def winner(self):
        return self._winner
    def draw(self):
        return self._draw

class Fighter():
    def __init__(self):
        self.ID = None
        self.height = None
        self.weight = None
        self.reach = None
        self.stance = None
        self.wins = None
        self.losses = None
        self.draws = None
        self.no_contest = None
    def ID(self):
        return self._ID
    def height(self):
        return self._height
    def weight(self):
        return self._weight
    def reach(self):
        return self._reach
    def stance(self):
        return self._stance
    def wins(self):
        return self._wins
    def losses(self):
        return self._losses
    def draws(self):
        return self._draws
    def no_contest(self):
        return self._no_contest
