# README
This repo contains my solution for the first project of the udacity Deep Reinforcement Learning Nanodegree.
The code and implementation is based on my solution to the udacity Deep Q-Learning algorithm coding exercise which I adopted from the open AI Gym environment to the UnityAgents environment.  

# Short Description of the environment

The environment is a 2-dimensional rectangular bounded world with yellow and blue bananas scattered around. The goal of the agent is to collect as many yellow bananas as possible and try to avoid the blue bananas. The corresponding reward function gives a reward of +1 for every yellow banana collected end a penalty of -1 for every blue banana touched. The task is episodic. 

## State Space

The state space consists of 37 continuous dimensions including the the agent's velocity and a LIDAR-like ray-based scan of objects in the agent's forward direction.

## Action Space

The action space is discrete and contains 4 possible actions:

- **`0`** - forward
- **`1`** - backward
- **`2`** - left turn
- **`3`** - right turn

## Solution criterion

The environment is considered to be solved, if the agent scores on average +13 on 100 consecutive episodes 


# Files in the Repository

Interesting files in the repo are: 

- `DQN_Navigation.ipynb`: Notebook used to control and train the agent 
- `dqn_agent.py`: Create an Agent class that interacts with and learns from the environment 
- `model.py`: class used to map state to action values 
- `checkpoint_DDQN`: Saved weights for dueling network model
- `checkpoint_DQN`: Saved weights for conventional network model
- `report.pdf`: Project report including explanation of the two algorithms used and a short discussion of the results. 


# Getting Started, Installation and Dependencies

Installing all required dependencies to run the code locally was not an easy task. This project was completed on the provided workspace on AWS.

## Dependencies and Environment

The code requires Python 3. The  necessary dependencies can be found in `./python/requirements.txt` 
Batch installation is done like so: 
```
pip install ./python/requirements.txt
``` 
The necessasry Unity environment can be downloaded from the following locations:

- Windows 64-bit: [link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)
- Linux : [link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
- OS X : [link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)

## Execution

Once you have cloned this repository and istalled the dependencies and the environment, the main entry point for execution is the Jupyter-notebook `DQN_Navigation.ipynb`.



# Reference and Credits

The implementation is based on code from the coding exercice of the same chapter and adopted to the new environment. The complete list of references can be found in the project report.
