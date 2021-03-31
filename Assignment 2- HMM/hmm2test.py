def f_create_matrix(p_matrix_item):
    #l_matrix_list   = list(p_matrix_item.split())
    l_matrix_elem   = list(map(float, p_matrix_item[2:]))
    l_rows          = int(p_matrix_item[0])
    l_cols          = int(p_matrix_item[1])
    l_matrix        = []
    for i_row in range(l_rows):
        t_row_list = []
        for i_col in range(l_cols):
            if l_matrix_elem[i_col] not in l_matrix:
                t_row_list.append(l_matrix_elem[l_cols * i_row + i_col])
        l_matrix.append(t_row_list)
    return l_matrix


a = [float(x) for x in input().split()]
b = [float(x) for x in input().split()]
pi = [float(x) for x in input().split()]
e = [int(x) for x in input().split()]

trans_matrix_A    = f_create_matrix(a)
obs_matrix_B      = f_create_matrix(b)
init_prob_pi      = f_create_matrix(pi)
obs_seq   = e[1:]




'''def create_matrix(n_rows, n_col, data_list):
    mat = []
    for i in range(n_rows):
        row_list = []
        for j in range(n_col):
            if data_list[j] not in mat:
                row_list.append(data_list[n_col * i + j])
        mat.append(row_list)
    return mat


input_file = open("hmm2_01.in")
matrices_list = input_file.read().splitlines()
print(matrices_list)

first_matrix = matrices_list[0]
second_matrix = matrices_list[1]
third_matrix = matrices_list[2]
obs_seq = matrices_list[3]

# Creating the State transition matrix A
lst_1 = list(first_matrix.split())
A_rows = int(lst_1[0])
A_col = int(lst_1[1])
a_str = lst_1[2:]
A = list(map(float, a_str))  # Transition matrix
print(A)

# Creating the Emission matrix B
lst_2 = list(second_matrix.split())
B_rows = int(lst_1[0])
B_col = int(lst_1[1])
b_str = lst_2[2:]
B = list(map(float, b_str))  # Emission matrix
print(B)

# Creating the Initial state distribution matrix pi
lst_3 = list(third_matrix.split())
pi_str = lst_3[2:]
pi = list(map(float, pi_str))  # Initial probabilities
print(pi)
pi_col = len(pi)

# Extracting the observation sequence
lst_4 = list(obs_seq.split())
obs_str = lst_4[1:]
obs_seq = list(map(int, obs_str))  # Observation sequence
print(obs_seq)

trans_matrix_A = create_matrix(A_rows, A_col, A)
obs_matrix_B = create_matrix(B_rows, B_col, B)
init_prob_pi = create_matrix(1, pi_col, pi)'''


N = len(trans_matrix_A[0])
T = len(obs_seq)

alpha_list = []
t = 0

# FORWARD ALGORITHM

for t in range(T):
    print(t)
    alpha_temp_list = []
    for i in range(N):
        b_temp = obs_matrix_B[i]
        if t == 0:
            pi_temp = init_prob_pi[0]
            print(pi_temp)
            alpha = init_prob_pi[0][i] * obs_matrix_B[i][obs_seq[t]]
            print(alpha)
            alpha_list.append(alpha)
            print("alpha_list: " + str(alpha_list))
        else:
            print(alpha_list)
            sum_term = 0
            for j in range(N):
                #trans_temp = trans_matrix_A[i]
                sum_term += alpha_list[j] * trans_matrix_A[j][i]## * b_temp[obs_seq[t]]
                # print("sum_term: " + str(sum_term))
            alpha_temp_list.append(sum_term * b_temp[obs_seq[t]])
            print(alpha_temp_list)
    if t > 0:
        alpha_list = alpha_temp_list
    print("alpha_list: " + str(alpha_list))

total_prob = 0
for ele in range(0, len(alpha_list)):
    total_prob = total_prob + alpha_list[ele]
print("total_prob: " + str(total_prob))
