from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Christian König gen. Kersting'

doc = """
A code snippet to show how elements can be hidden permanently, i.e. they do not reappear and restart the timer 
when the page is reloaded.
"""


class Constants(BaseConstants):
    name_in_url = 'hide_elements'
    players_per_group = None
    num_rounds = 1

    element_display_time = 15 # seconds

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    element_first_seen = models.IntegerField(initial=0)
