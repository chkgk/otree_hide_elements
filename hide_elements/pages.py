from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from datetime import datetime

class MyPage(Page):
    def vars_for_template(self) -> dict:
        # the first time the page is loaded, set chat start time
        if self.player.element_start_time == 0:
            self.player.element_start_time = int(datetime.timestamp(datetime.now()))

        element_end_time = self.player.element_start_time + Constants.display_time
        return {
            "element_available_until": element_end_time
        }


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
