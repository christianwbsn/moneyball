FANTASY_BASE_URL    = "https://gaming.uefa.com/en/uefaeuro2020fantasyfootball/services/api/Feed/"
PLAYERS_ENDPOINT    = "players"
TEAMS_ENDPOINT      = "teams/"
FIXTURES_ENDPOINT   = "fixtures"

PLAYERS_RANKING_URL = "https://performancezone.uefa.com/api/v3/rankings"


entity_url_map = {
    "players"     : FANTASY_BASE_URL + PLAYERS_ENDPOINT,
    "teams"       : FANTASY_BASE_URL + TEAMS_ENDPOINT,
    "fixtures"    : FANTASY_BASE_URL + FIXTURES_ENDPOINT,
    "players_rank": PLAYERS_RANKING_URL
}