#!/bin/python3

class Player:
    def __init__(self, tickets, pos, name):
        self.tickets = tickets
        self.pos = pos
        self.nextMove = None
        self.name = name

    def __eq__(self, other):
        return self.pos == other.pos and self.tickets == other.tickets and self.name == other.name

    def move(self, transportation, new_nodeid):
        self.nextMove = (new_nodeid, transportation)
