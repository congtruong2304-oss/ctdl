function get_candidates(board, r, c)
    used = falses(9)
    # Kiểm tra hàng và cột
    for i in 1:9
        if board[r, i] != 0
            used[board[r, i]] = true
        end
        if board[i, c] != 0
            used[board[i, c]] = true
        end
    end
    # Kiểm tra khối 3x3
    br = div(r - 1, 3) * 3 + 1
    bc = div(c - 1, 3) * 3 + 1
    for i in 0:2
        for j in 0:2
            val = board[br + i, bc + j]
            if val != 0
                used[val] = true
            end
        end
    end
    return [num for num in 1:9 if !used[num]]
end

# 1. Quét tuần tự
function find_empty_sequential(board)
    for r in 1:9
        for c in 1:9
            if board[r, c] == 0
                return r, c
            end
        end
    end
    return 0, 0
end

function solve_sequential(board)
    calls = 0

    function backtrack()
        calls += 1
        r, c = find_empty_sequential(board)
        if r == 0
            return true
        end

        for val in get_candidates(board, r, c)
            board[r, c] = val
            if backtrack()
                return true
            end
            board[r, c] = 0 # Hoàn tác
        end
        return false
    end

    t0 = time_ns()
    backtrack()
    t1 = time_ns()
    return board, calls, (t1 - t0) / 1e6
end

# 2. Heuristic MRV
function find_empty_mrv(board)
    min_cands = 10
    best_r, best_c = 0, 0
    best_cands = Int[]

    for r in 1:9
        for c in 1:9
            if board[r, c] == 0
                cands = get_candidates(board, r, c)
                if isempty(cands)
                    return r, c, Int[]
                end
                if length(cands) < min_cands
                    min_cands = length(cands)
                    best_r, best_c = r, c
                    best_cands = cands
                    if min_cands == 1
                        return best_r, best_c, best_cands
                    end
                end
            end
        end
    end
    return best_r, best_c, best_cands
end

function solve_mrv(board)
    calls = 0

    function backtrack()
        calls += 1
        r, c, cands = find_empty_mrv(board)
        if r == 0
            return true
        end
        if isempty(cands)
            return false
        end

        for val in cands
            board[r, c] = val
            if backtrack()
                return true
            end
            board[r, c] = 0 # Hoàn tác
        end
        return false
    end

    t0 = time_ns()
    backtrack()
    t1 = time_ns()
    return board, calls, (t1 - t0) / 1e6
end

function main()
    grid_input = [
        5 3 0 0 7 0 0 0 0;
        6 0 0 1 9 5 0 0 0;
        0 9 8 0 0 0 0 6 0;
        8 0 0 0 6 0 0 0 3;
        4 0 0 8 0 3 0 0 1;
        7 0 0 0 2 0 0 0 6;
        0 6 0 0 0 0 2 8 0;
        0 0 0 4 1 9 0 0 5;
        0 0 0 0 8 0 0 7 9
    ]

    board_seq = copy(grid_input)
    _, calls_seq, t_seq = solve_sequential(board_seq)

    board_mrv = copy(grid_input)
    _, calls_mrv, t_mrv = solve_mrv(board_mrv)

    same_sol = (board_seq == board_mrv)

    println("="^55)
    println(rpad("Đại lượng", 26), "| ", rpad("Quét tuần tự", 14), "| ", rpad("MRV", 14))
    println("-"^55)
    println(rpad("Số lời gọi hàm đệ quy", 26), "| ", rpad(string(calls_seq), 14), "| ", rpad(string(calls_mrv), 14))
    println(rpad("Thời gian chạy", 26), "| ", rpad(string(round(t_seq, digits=2)) * " ms", 14), "| ", rpad(string(round(t_mrv, digits=2)) * " ms", 14))
    println(rpad("Lời giải tìm được", 26), "| ", same_sol ? "Giống nhau" : "Khác nhau")
    println("="^55)
end

main()
