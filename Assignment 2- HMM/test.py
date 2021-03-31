def create_matrix(mat_val):
    temp = [0] * len(mat_val);
    ## print(temp);
    for x in range(len(mat_val)):
        temp[x] = float(mat_val[x]);
    ## print("TEMP : ",temp);
    n_rows = int(temp[0]);
    n_cols = int(temp[1]);
    ## print("ROWS : ",n_rows);
    ## print("COLS : ",n_cols);
    mat = [[0] * n_cols]*n_rows;
    k = 2;
    for row in range(n_rows):
        temp2 = [0] * n_cols;
        for col in range(n_cols):
            temp2[col] = temp[k];
            k = k + 1;
        mat[row] = temp2;
    print(mat);
    return mat


def mat_mul(mat1,mat2):
    mat1_r = len(mat1);
    mat1_c = len(mat1[0]);
    mat2_r = len(mat2);
    mat2_c = len(mat2[0]);
    prod   = [[0]*mat2_c]*mat1_r;

    for row in range(mat1_r):
        ## print("ROW : ",row);
        temp = [0]*mat2_c;
        for col in range(mat2_c):
            ## print("COL : ",col);
            total = 0;
            for i in range(0,mat1_c):
                ## print("i : ",i);
                ## print(mat1[row][i],"*",mat2[i][col]);
                total += mat1[row][i] * mat2[i][col];
                ## print(total);
            temp[col] = round(total,4);
        prod[row] = temp;
    print(prod);        
    return prod


def main():
    inp_file = open("C:\\Users\\Naveen\\Downloads\\sample_00.in", "r");
    data = inp_file.readlines();
    inp_file.close();
    ## print(len(data))
    mat_a_val  = data[0].split();
    mat_b_val  = data[1].split();
    mat_pi_val = data[2].split();
    ## print(mat_a_val);
    ## print(type(mat_a_val[0]));
    print("CREATE : MATRIX A");    
    A  = create_matrix(mat_a_val);
    print("CREATE : MATRIX B"); 
    B  = create_matrix(mat_b_val);
    print("CREATE : MATRIX C");  
    pi = create_matrix(mat_pi_val);

    prodpiA   = mat_mul(pi,A);
    prodABpi = mat_mul(prodpiA, B);

if __name__== "__main__":
    main()
