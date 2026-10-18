# Reinforcement learning for radiotherapy scheduling

This directory contains the environments, PPO trainers, saved checkpoints,
evaluation notebooks, result tables, figures, and report source used for the
radiotherapy scheduling study.

## Setup

Run commands from `report_files`. The EMT6-Ro simulator must be available in
the sibling directory `../EMT6-Ro`, with its Python package built under
`../EMT6-Ro/build/python`.

Install the Python dependencies and both local packages with:

```bash
python -m pip install -r requirements.txt
```

Alternatively, create the Python 3.9 Conda environment:

```bash
conda env create -f environment.yml
conda activate rl4radiotherapy
```

## Third-party code

The `TumorGrowthEnv/` package is derived from
[Agnieszka Ilnicka's TumorGrowthEnv](https://github.com/ailnicka/TumorGrowthEnv).
The original project provides an OpenAI Gym interface to the EMT6-Ro tumour
simulation. It was modified for this study.

EMT6-Ro is a separate dependency developed by Rafał Banaś. 
Its source is available in the
[EMT6-Ro repository](https://github.com/banasraf/EMT6-Ro/).

## Repository structure

- `TumorGrowthEnv/` contains the model-specific Gym environments.
- `train_*_PPO.py` trains each PPO variant from a new model.
- `baselines/` and `fig05_compare_model_at_steps.ipynb` reproduce Figures 2–7.
- `baselines/results/models/` contains checkpoints grouped by PPO model.
- `check_ppo_choices.py` summarizes complete protocols selected by PPO models.
- `report/` contains the Quarto report source.

## PPO training

| Trainer | Environment | Default training steps |
|---|---|---:|
| `train_paper_PPO.py` | Paper PPO environment | 25,000 |
| `train_normalized_PPO.py` | Shared environment, normalized profile | 50,000 |
| `train_fract_PPO.py` | Shared environment, fraction profile | 50,000 |
| `train_mesh_PPO.py` | Shared environment, mesh profile | 25,000 |
| `train_cnn_mesh_PPO.py` | CNN Mesh PPO environment | 50,000 |

Run one trainer at a time:

```bash
python train_paper_PPO.py
python train_normalized_PPO.py
python train_fract_PPO.py
python train_mesh_PPO.py
python train_cnn_mesh_PPO.py
```

By default, training starts from a new model, uses seed 0, ten parallel
simulations, 24-hour treatment availability, and no appointment delays.
Checkpoints are saved every 1,000 steps under
`baselines/results/models/<model>/` together with logs and `settings.json`.

The environment option `appointment_delays=False` disables appointment
delays. Setting it to `True` enables the fixed positive-only delay distribution
used in the appointment-delay evaluation.

## Evaluation and figures

| Figure | Source | Purpose |
|---|---|---|
| 2 | `baselines/fig02_baselines_10x10_24h.ipynb` | Compare 25k PPO checkpoints with reference protocols over 10 rounds |
| 3 | `baselines/fig03_baselines_30x10_24h.ipynb` | Compare final PPO checkpoints with reference protocols over 30 rounds |
| 4 | `baselines/fig04_compare_ppo_checkpoints.ipynb` | Plot Paper, Normalized, Fract, and Mesh PPO performance from 1k to 25k steps |
| 5 | `fig05_compare_model_at_steps.ipynb` | Plot Normalized, Fract, and CNN Mesh PPO performance from 1k to 50k steps |
| 6 | `baselines/fig06_baselines_app_delays.ipynb` | Evaluate models and protocols with appointment delays |
| 7 | `baselines/fig07_baselines_10h.ipynb` | Evaluate models and protocols with a 10-hour daily treatment window |

Figures 6 and 7 compare their evaluation summaries with the normal 24-hour
results. Generate the final comparison plots with:

```bash
python baselines/fig06_plot_app_delay_comparison.py
python baselines/fig07_plot_10h_comparison.py
```

Evaluation outputs are written to `baselines/results/`. Filenames beginning
with `fig01` through `fig07` correspond to the figure numbers in the report.
In result filenames, `10x10` and `30x10` mean evaluation rounds × parallel
simulations.

To calculate how often PPO selects each complete treatment protocol, run:

```bash
python check_ppo_choices.py
```
