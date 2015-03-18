matrix = [['x','o','x'],['x','o','x'],['x','x','o']]

def check_column(matrix):
         for col in range(0,3):
             if matrix[0][col]==matrix[1][col]==matrix[2][col]:
                 return True
             return false
print check_column(matrix)
         

def check_diagnals(matrix):
    diag1 = []
    diag2 = []
    for i in range(0,3):
        diag1.append(matrix[i][i])
        diag2.append(matrix[i][2-i])

        if diag1 ==['x','x','x'] or diag1 ==['o','o','o']:
            return True
        elif diag2 ==['x','x','x'] or diag2 ==['o','o','o']:
            return True
        else:
            return False

print check_diagnals(matrix)
            
            
