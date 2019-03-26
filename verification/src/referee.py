from checkio_referee import RefereeRank


import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "mult_two"
    FUNCTION_NAMES = {
        "python_3": "mult_two",
        "js_node": "multTwo"
    }