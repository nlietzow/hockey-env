from gymnasium.envs.registration import register

register(
    id="Hockey-v0",
    entry_point="hockey.hockey_env:HockeyEnv",
    kwargs={"mode": 0},
)
register(
    id="Hockey-One-v0",
    entry_point="hockey.hockey_env:HockeyEnvWithOpponent",
    kwargs={"mode": 0, "checkpoint": None},
)

REGISTERED_ENVS = ["Hockey-v0", "Hockey-One-v0"]
