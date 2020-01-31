from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from datetime import datetime

class MyPage(Page):
    def vars_for_template(self) -> dict:
        # the first time the page is loaded, set element first seen time
        if self.player.element_first_seen == 0:
            self.player.element_first_seen = int(datetime.timestamp(datetime.now()))

        element_hiding_time = self.player.element_first_seen + Constants.element_display_time
        return {
            "element_hiding_time": element_hiding_time
        }


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
