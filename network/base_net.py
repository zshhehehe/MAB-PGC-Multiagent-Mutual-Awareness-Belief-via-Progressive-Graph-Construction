import torch.nn as nn
import torch.nn.functional as f
import torch

class RNN(nn.Module):
    # Because all the agents share the same network, input_shape=obs_shape+n_actions+n_agents
    def __init__(self, input_shape, args):
        super(RNN, self).__init__()
        self.args = args

        self.fc1 = nn.Linear(input_shape, args.rnn_hidden_dim)
        self.rnn = nn.GRUCell(args.rnn_hidden_dim, args.rnn_hidden_dim)
        self.fc2 = nn.Linear(args.rnn_hidden_dim, args.n_actions)

    def forward(self, obs, hidden_state):
        x = f.relu(self.fc1(obs))

        h = self.rnn(x, hidden_state)

        return h , x
    def forward2(self,mess,h):
        q = self.fc2(torch.add(mess,h.cuda()))
        return q
class selfAttention(nn.Module):
    def __init__(self,hidden_dim,n_agent):
        super(selfAttention,self).__init__()
        self.hidden_dim = hidden_dim
        self.n_agent = n_agent

    def forward(self,query,k,v):
        q = query
        k = k.reshape(-1,self.hidden_dim,self.n_agent)
        x = torch.softmax(torch.matmul(q,k),dim=-1) #(bs,n_agents,hidden_dim)
        mess = torch.matmul(x,v)

        # mess = self.conv(mess)
        # mess = mess.squeeze(1)
        mess = mess.reshape(-1,self.hidden_dim)
        return mess
class queryModule(nn.Module):
    def __init__(self,states_shape,n_agent,hidden_dim,):
        super(queryModule, self).__init__()
        self.k = None
        self.v = None
        self.hidden_dim = hidden_dim
        self.n_state = states_shape
        self.n_agent = n_agent
        self.exchange = selfAttention(hidden_dim,n_agent)
        self.updateK = nn.Linear(2*hidden_dim,hidden_dim)

        self.updateV = nn.Linear(2*hidden_dim,hidden_dim)
        self.Norm = nn.BatchNorm1d(hidden_dim)
    def forward(self,hidden):
        #query mess

        mess = self.exchange(hidden,self.k,self.v)
        #update agent_i mess
        return mess
    def initKV(self,bs):
        self.k = torch.zeros((bs,self.n_agent,self.hidden_dim)).cuda()
        self.v = torch.zeros((bs,self.n_agent,self.hidden_dim)).cuda()

    def updateKV(self,x):

        #(bs*n,hidden_dim)
        # x = x.unsqueeze(1)
        # x = self.deconv(x)
        # xv = torch.matmul(self.v,torch.matmul(self.k.T,x))

        # print(torch.max(xv))
        # xk = torch.matmul(self.k,torch.matmul(self.v.T,x))


        self.k = self.updateK(torch.cat([self.k,x],dim=-1))
        self.v = self.updateV(torch.cat([self.v,x],dim=-1))


# Critic of Central-V
class Critic(nn.Module):
    def __init__(self, input_shape, args):
        super(Critic, self).__init__()
        self.args = args
        self.fc1 = nn.Linear(input_shape, args.critic_dim)
        self.fc2 = nn.Linear(args.critic_dim, args.critic_dim)
        self.fc3 = nn.Linear(args.critic_dim, 1)

    def forward(self, inputs):
        x = f.relu(self.fc1(inputs))
        x = f.relu(self.fc2(x))
        q = self.fc3(x)
        return q
