import logging
from gymnasium.envs.registration import register

REGISTERED_ENVS = False

try:
    register(
        id="Hockey-v0",
        entry_point="hockey.hockey_env:HockeyEnv",
        kwargs={"mode": 0},
    )
    register(
        id="Hockey-One-v0",
        entry_point="hockey.hockey_env:HockeyEnv_BasicOpponent",
        kwargs={"mode": 0, "weak_opponent": False},
    )
    register(
        id="Hockey-One-SB3-v0",
        entry_point="hockey.hockey_env:HockeyEnvSB3Opponent",
        kwargs={"mode": 0, "weak_opponent": False},
    )
    REGISTERED_ENVS = True
except Exception as e:
    logging.error("Error registering environments in hockey:", e)
