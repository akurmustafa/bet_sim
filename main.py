
import matplotlib.pyplot as plt
import numpy as np


def main():
    # parameters ###############
    n_sim = int(1e4)
    n_play = int(1e3)
    odd_min = 1.0  # assumes odd is uniform distrubuted
    odd_max = 4.0
    prob_win_coeff = 0.9
    strategies = np.arange(1, 10)
    print_every = 1
    # parameters ###############
    odd_range = odd_max-odd_min
    n_strategy = int(strategies.shape[0])
    money_received = np.zeros((n_sim, n_play, n_strategy))
    for i in range(n_sim):
        for k, n_cur_strategy in zip(range(n_strategy), strategies):
            cur_odds = np.random.rand(n_play, n_cur_strategy)*odd_range+odd_min
            cur_win_probs = (1.0/cur_odds)*prob_win_coeff
            cur_outcome = np.random.rand(n_play, n_cur_strategy)
            success_indices = np.where(np.sum(((cur_win_probs-cur_outcome)>0).astype(np.int32), axis=1) == n_cur_strategy)[0]
            money_received[i, success_indices, k] = np.prod(cur_odds, axis=1)[success_indices]
        if i%print_every == print_every-1:
            print('progress: {}/{}'.format(i+1, n_sim))
    profit_ratio = np.mean(money_received, axis=1).reshape((n_sim, n_strategy))
    for k, n_cur_strategy in zip(range(n_strategy), strategies):
        plt.figure()
        plt.hist(profit_ratio[:, k], int(n_sim**0.5))
        plt.title('Strategy: '+str(n_cur_strategy))
    plt.show()
    pass


if __name__ == '__main__':
    main()
