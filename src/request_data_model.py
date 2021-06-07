class FantasyTeamsRequestParams:
    def __init__(self, lang="en"):
        self.tour_id = 1
        self.lang = lang

class FantasyFixturesRequestParams:
    def __init__(self, lang="en"):
        self.tour_id = 1
        self.lang = lang

class FantasyPlayersRequestParams:
    def __init__(self, matchday_id=1, lang="en"):
        self.tour_id = 1
        self.lang = lang
        self.matchdayId = matchday_id

class PlayersRankingRequestParams:
    def __init__(self,
                 competitionId="NTC",
                 languageSet="EN",
                 offset=0,
                 seasonYear="current",
                 statisticSet="FIELD_POSITION_SET",
                 limit=2157):
        self.competitionId = competitionId
        self.languageSet = languageSet
        self.offset = offset
        self.seasonYear = seasonYear
        self.statisticSet = statisticSet
        self.limit = limit


ENTITY_PARAMS_MAP = {
    "players"     : FantasyPlayersRequestParams(),
    "teams"       : FantasyTeamsRequestParams(),
    "fixtures"    : FantasyFixturesRequestParams(),
    "players_rank": PlayersRankingRequestParams()
}