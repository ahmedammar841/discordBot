import os
import discord
import asyncio
import logging
import random

class Hangman:
    chosen_word = ""
    guessed_letters = ""
    remaining_guesses = 6
    words = {1: 'cs125', 2: 'angrave', 3: 'java'}

    def start_game(self):
        key = random.randint(1, 3)
        self.chosen_word = self.words[key]
        self.guessed_letters = self.chosen_word

    def return_game_status(self):
        message = '{} guesses left \n'.format(self.remaining_guesses)
        message += self.guessed_letters
        return message