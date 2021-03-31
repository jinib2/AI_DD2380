# import math

from baum_welch_functions import f_create_matrix
from baum_welch_functions import f_alpha_pass
from baum_welch_functions import f_beta_pass
from baum_welch_functions import f_comp_gamma
from baum_welch_functions import f_re_estimate
from baum_welch_functions import f_prob_log


def main():
    input_file = open("hmm_c_N1000.in")
    #input_file = open("hmm_c_N10000.in")

    read = input_file.read()
    lst = list(read.split())[1:]
    print(lst)
    l_obs_seq = list(map(int, lst))  # Observation sequence
    print("l_obs_seq: " + str(l_obs_seq))

    #Original initialization
    '''l_trans_matrix_A = [[0.7, 0.05, 0.25], [0.1, 0.8, 0.1], [0.2, 0.3, 0.5]]
    l_obs_matrix_B = [[0.7, 0.2, 0.1, 0], [0.1, 0.4, 0.3, 0.2], [0, 0.1, 0.2, 0.7]]
    l_init_prob_pi = [[1, 0, 0]]'''

    #Slight change initialization
    '''l_trans_matrix_A = [[0.7, 0.03, 0.28], [0.1, 0.85, 0.15], [0.15, 0.35, 0.5]]
    l_obs_matrix_B = [[0.7, 0.1, 0.2, 0], [0.1, 0.45, 0.25, 0.2], [0, 0.15, 0.2, 0.65]]
    l_init_prob_pi = [[0.9, 0.1, 0]]'''

    #Given probabilities
    '''l_trans_matrix_A = [[0.54, 0.26, 0.20], [0.19, 0.53, 0.28], [0.22, 0.18, 0.6]]
    l_obs_matrix_B = [[0.5, 0.2, 0.11, 0.19], [0.22, 0.28, 0.23, 0.27], [0.19, 0.21, 0.15, 0.45]]   
    l_init_prob_pi = [[0.3, 0.2, 0.5]]'''

    # Uniform distribution
    '''l_trans_matrix_A = [[0.333, 0.333, 0.333], [0.333, 0.333, 0.333], [0.333, 0.333, 0.333]]
    l_obs_matrix_B = [[0.25, 0.25, 0.25, 0.25], [0.25, 0.25, 0.25, 0.25], [0.25, 0.25, 0.25, 0.25]] 
    l_init_prob_pi = [[0.333, 0.333, 0.333]]'''

    #Random_close to 1/n and 1/m
    l_trans_matrix_A = [[0.30, 0.35, 0.35], [0.30, 0.35, 0.35], [0.42, 0.28, 0.30]]
    l_obs_matrix_B = [[0.25, 0.25, 0.30, 0.20], [0.35, 0.25, 0.25, 0.15], [0.25, 0.25, 0.30, 0.20]]
    l_init_prob_pi = [[0.30, 0.30, 0.40]]



    # We are flipping the observation sequence because the Beta pass
    # operations are the same as the alpha pass operations
    # The output of Beta pass needs to be flipped so that the index will
    # correspond to the right time stamp

    l_M = len(set(l_obs_seq))         # Count of unique elements in obs seq
    l_N = len(l_trans_matrix_A)
    l_T = len(l_obs_seq)

    l_iter_cnt = 0
    l_max_iters = 2100
    l_old_log_prob = float("-inf")
    l_log_prob = 1

    while l_iter_cnt < l_max_iters and l_log_prob > l_old_log_prob:
        l_iter_cnt += 1
        # print("Iteration count : ", str(l_iter_cnt))
        if l_iter_cnt != 1:
            l_old_log_prob = l_log_prob

        l_alpha_vals, l_c_val = f_alpha_pass(l_trans_matrix_A, l_obs_matrix_B, l_init_prob_pi, l_obs_seq, l_N, l_T)

        l_c_beta = l_c_val[::-1]
        l_seq_beta = l_obs_seq[::-1]
        l_beta_flip = f_beta_pass(l_trans_matrix_A, l_obs_matrix_B, l_init_prob_pi, l_seq_beta, l_c_beta, l_N, l_T)
        l_beta_vals = l_beta_flip[::-1]

        l_gamma_list, l_gamma_ij_list = f_comp_gamma(l_trans_matrix_A, l_obs_matrix_B, l_obs_seq, l_alpha_vals,
                                                     l_beta_vals, l_N, l_T)

        l_init_prob_pi, l_trans_matrix_A, l_obs_matrix_B = f_re_estimate(l_gamma_list, l_gamma_ij_list, l_obs_seq, l_M,
                                                                         l_N, l_T)

        l_log_prob = f_prob_log(l_c_val, l_T)
    print("l_iter_cnt: " + str(l_iter_cnt))

    for i in range(len(l_trans_matrix_A)):
        l_trans_matrix_A[i] = [round(num, 3) for num in l_trans_matrix_A[i]]
    # print("a_n: "  + str(l_trans_matrix_A))

    A = [item for sublist in l_trans_matrix_A for item in sublist]
    t_str_A = ' '.join([str(l_elem) for l_elem in A])
    print(l_N, l_N, t_str_A)

    for i in range(len(l_obs_matrix_B)):
        l_obs_matrix_B[i] = [round(num, 3) for num in l_obs_matrix_B[i]]
    # print("b_n: "  + str(l_obs_matrix_B))

    B = [item for sublist in l_obs_matrix_B for item in sublist]
    t_str_B = ' '.join([str(l_elem) for l_elem in B])
    print(l_N, l_M, t_str_B)

    for i in range(len(l_init_prob_pi)):
        l_init_prob_pi[i] = [round(num, 3) for num in l_init_prob_pi[i]]

    PI = [item for sublist in l_init_prob_pi for item in sublist]
    t_str_PI = ' '.join([str(l_elem) for l_elem in PI])
    print(len(PI), t_str_PI)

if __name__ == "__main__":
    main()
