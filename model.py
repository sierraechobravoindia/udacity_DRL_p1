import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        "*** YOUR CODE HERE ***"
        self.input_size = state_size
        self.output_size = action_size
        self.hidden_size_1 = 64
        self.hidden_size_2 = 32
        
        self.fc1 = torch.nn.Linear(self.input_size, self.hidden_size_1)
        self.fc2 = torch.nn.Linear(self.hidden_size_1, self.hidden_size_2)
        self.fc3 = torch.nn.Linear(self.hidden_size_2, self.output_size)
        
        self.relu = torch.nn.ReLU()
        

    def forward(self, state):
        """Build a network that maps state -> action values."""
        x = self.fc1(state)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        return x
      
    
class DDQN(nn.Module):
    def __init__(self, state_size, action_size, seed):
        super(DDQN, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.state_size = state_size
        self.action_size = action_size
        self.common_size = 256
        self.value_size = 128
        self.advantage_size = 128
        self.fc_common = nn.Linear(state_size, self.common_size)
        self.fc_v_in = nn.Linear(self.common_size, self.value_size)
        self.fc_v_out = nn.Linear(self.value_size, 1)
        self.fc_a_in = nn.Linear(self.common_size, self.advantage_advatage_size)
        self.fc_a_out = nn.Linear(self.advantage_size, self.action_size)
        self.relu = torch.nn.ReLU()
        
        
    def forward(self, state):
        common = self.relu(self.fc_common(state))
        value = self.relu(self.fc_v_in(common))
        advantage = self.relu(self.fc_a_in(common))
        value = self.fc_v_out(value)
        advantage = self.fc_a_out(advantage)
        out = value + advantage - advantage.mean(dim=1).unqueeze(1) 
        return out
    
