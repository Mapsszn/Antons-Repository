def relationship_status(from_member, to_member, social_graph):
    dictionary_1 = social_graph[from_member]['following']
    dictionary_2 = social_graph[to_member]['following']
    if from_member in dictionary_2 and to_member in dictionary_1:
        return('friends')
    elif from_member in dictionary_2:
        return('followed by')
    elif to_member in dictionary_1:
        return('follower')
    else:
        return('no relationship')

def tic_tac_toe(board):
    board_size = len(board)
    y = 0
    for i in range(0, board_size):
        for x in range(0, board_size-1):
            if board[i][x] == board[i][x+1]:
                y += 1
            else:
                y = 0
            if y == board_size-1:
                if board[i][x+1] == "":
                    y = 0
                else:
                    return(board[i][x+1])
                    break
        if y == board_size-1:
            break
    
                      
    for i in range(0, board_size):
        if y == board_size-1:
            break
        for x in range(0, board_size-1):
            if board[x][i] == board[x+1][i]:
                y += 1
            else:
                y = 0
            if y == board_size-1:
                if board[x+1][i] == "":
                    y = 0
                else:
                    return(board[x+1][i]) 
                    break


    for i in range(0, board_size-1):
        if y == board_size-1:
            break
        if board[i][i] == board[i+1][i+1]:
            y += 1
        else:
            y = 0
        if y == board_size-1:
            if board[i+1][i+1] == "":
                y = 0
            else: 
                return(board[i+1][i+1])
                break


    for i in range(0, board_size-1):
        if board[board_size-1-i][i] == board[board_size-i-2][i+1]:
            y += 1
        else:
            y = 0
        if y == board_size-1:
            if board[board_size-1-i][i] == "":
                y = 0
            else:
                return(board[board_size-1-i][i])
                break
        
    if y != board_size-1:
        return("NO WINNER")

def eta(first_stop, second_stop, route_map):
    time = 0
    current_stop = first_stop
    while current_stop != second_stop:
        for (from_stop, to_stop), leg_info in route_map.items():
            if from_stop == current_stop:
                time += leg_info['travel_time_mins']
                current_stop = to_stop
                break
    return(time)

                

    

    