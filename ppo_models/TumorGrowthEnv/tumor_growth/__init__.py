from gym.envs.registration import register

SHARED_ENVIRONMENT = (
    "tumor_growth.envs.tumor_growth_env_normal_fract_mesh:TumorGrowthEnv"
)

ENVIRONMENTS = {
    "tumor-growth-paper-ppo-v0": (
        "tumor_growth.envs.tumor_growth_env_paper_ppo:TumorGrowthEnv",
        {},
    ),
    "tumor-growth-normalized-ppo-v0": (
        SHARED_ENVIRONMENT,
        {"ppo_type": "normalized"},
    ),
    "tumor-growth-fract-ppo-v0": (
        SHARED_ENVIRONMENT,
        {"ppo_type": "fract"},
    ),
    "tumor-growth-mesh-ppo-v0": (
        SHARED_ENVIRONMENT,
        {"ppo_type": "mesh"},
    ),
    "tumor-growth-cnn-mesh-ppo-v0": (
        "tumor_growth.envs.tumor_growth_env_cnn_mesh_ppo:TumorGrowthEnv",
        {},
    ),
}

for environment_id, (entry_point, kwargs) in ENVIRONMENTS.items():
    register(id=environment_id, entry_point=entry_point, kwargs=kwargs)
