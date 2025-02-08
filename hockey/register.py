from gymnasium.envs.registration import register

register(
    id="Hockey-v0",
    entry_point="hockey.hockey_env_v2:HockeyEnv",
)
register(
    id="Hockey-One-v0-BasicOpponent",
    entry_point="hockey.hockey_env_v2:HockeyEnvBasicOpponent",
)
register(
    id="Hockey-One-v0-AIOpponent",
    entry_point="hockey.hockey_env_v2:HockeyEnvAIOpponent",
)

REGISTERED_ENVS = [
    "Hockey-v0",
    "Hockey-One-v0-BasicOpponent",
    "Hockey-One-v0-AIOpponent",
]
