# Markov Decision Process in Reinforcement Learning

This project demonstrates the application of the **Markov Decision Process (MDP)** in training a reinforcement learning agent for autonomous navigation within a maze. Using Python, we simulate a 2D maze game where a robot learns to navigate to a target point while avoiding obstacles like walls and bombs.

The project explores the impact of key parameters, such as the **Exploration Rate (ε)** and **Discount Factor (γ)**, on the agent's performance and learning efficiency. Through experiments, we analyze how balancing exploration and exploitation improves decision-making and training outcomes.

> **Note**: The codebase is used for experiments for myself and may be difficult to follow due to modifications made during the project's testing and experimentation. **For a clearer understanding of the project, please refer to the attached PDF report (`ESTR2018_Final_Report.pdf`).**

---

## File Descriptions

Here is a brief description of the files in this project:

- **`env.py`**:  
  Used for creating the environment (the maze) where the agent is trained.
  
- **`agent.py`**:  
  Implements the MDP algorithm and defines the behavior of the agent.

- **`main.py` / `main2.py`**:  
  Scripts for running the entire program, including the training and evaluation processes.

- **`vis.py`**:  
  Generates animations to visualize the learning process of the agent.

---

## Contributors

This project was developed by:
- Poonyapat Sriroth
- Shuwei Zhao
