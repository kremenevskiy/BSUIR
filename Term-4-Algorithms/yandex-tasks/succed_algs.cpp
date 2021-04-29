//
// Created by Vladislav Kremenevskiy on 4/27/21.
//

#include <vector>
#include <iostream>

using std::pair;
using std::vector;



// task 1

void make_set(vector<int>& parent, int v){
    parent[v] = v;
}

int find_set(vector<int>& parent, int v){
    if(v == parent[v]){
        return v;
    }
    return find_set(parent, parent[v]);
}

void union_sets(vector<int>& parent, int a, int b){
    a = find_set(parent, a);
    b = find_set(parent, b);
    if ( a != b) {
        parent[b] = a;
    }
}

void solve_adding(){
    int N, M;
    std::cin >> N >> M;
    vector<int> parent(N);
    for(int i = 0; i < N; ++i){
        parent[i] = i;
    }
    int v1, v2;
    for(int i = 0; i < M; ++i){
        std::cin >> v1 >> v2;
        union_sets(parent, v1-1, v2-1);
    }

    int ans = 0;
    for(int i = 0; i < parent.size() - 1; ++i){
        int p1 = find_set(parent, i);
        int p2 = find_set(parent, i+1);
        if (p1 != p2){
            ++ans;
            union_sets(parent, p1, p2);
        }
    }
    std::cout << ans;
}


// task 2

void simple_task(){
    int N;
    std::cin >> N;
    std::vector<long long> nums(N);

    long long big_pos = 0;
    long long big_neg = -1;
    for(int i = 0; i < N; ++i){
        std::cin >> nums[i];
        if (nums[i] < big_neg) {
            big_neg = nums[i];
        }
        else if(nums[i] > big_pos) {
            big_pos = nums[i];
        }
    }

    long long max_mul{};
    long long paired_pos{};
    long long paired_neg{};

    if (N == 2) {
        max_mul = (long long)nums[0] * (long long)nums[1];
        std::cout << max_mul;
        return;
    }
    else {
        for (int i = 0; i < N; ++i) {
            if (nums[i] > paired_pos || nums[i] < paired_neg) {
                if (big_pos == nums[i] || big_neg == nums[i])
                    continue;
                if (big_neg * nums[i] > max_mul) {
                    max_mul = big_neg * nums[i];
                    paired_neg = nums[i];
                    continue;
                } else if (big_pos * nums[i] > max_mul) {
                    max_mul = big_pos * nums[i];
                    paired_pos = nums[i];
                    continue;
                }
            }
        }
    }

    std::cout << max_mul;
}



// task 3

void max_k_mul(){
    const long long raund = (long long)(pow(10, 9) + 7);
    int N, K;
    std::cin >> N >> K;
    std::vector<long long> nums(N);
    for(int i = 0; i < N; ++i){
        std::cin >> nums[i];
    }

    std::sort(nums.begin(), nums.end());
    long long mul = 1;

    int h = (int)nums.size() - 1;
    int l = 0;
    if (nums[h] < 0) {
        if (K % 2 == 1) {
            while (K > 0) {
                mul = mul * nums[h] % raund;
                --h;
                --K;
            }
            std::cout << (mul + raund) % raund;
            return;
        } else if (K % 2 == 0) {
            while (K > 0) {
                mul *= nums[l] * nums[l + 1] % raund;
                K -= 2;
                l += 2;
            }
            std::cout << (mul + raund) % raund;
            return;
        }
    } else {
        if (K % 2 == 0) {
            while (K > 0) {
                if (nums[l] * nums[l + 1] >= nums[h] * nums[h - 1]) {
                    mul = (mul * (nums[l] * nums[l + 1] % raund)) % raund;
                    K -= 2;
                    l += 2;
                } else if (nums[l] * nums[l + 1] < nums[h] * nums[h-1]) {
                    mul = (mul * (nums[h] * nums[h - 1] % raund)) % raund;
                    K -= 2;
                    h -= 2;
                }
            }
            std::cout << (mul + raund) % raund;
            return;
        }
    }
    if (K % 2 == 1) {
        long long biggest = nums[h];
        --h;

        while (K > 1) {
            if (nums[l] * nums[l + 1] >= nums[h] * nums[h-1]) {
                mul = (mul * (nums[l] * nums[l + 1] % raund)) % raund;
                K -= 2;
                l += 2;
            } else if (nums[l] * nums[l + 1] < nums[h] * nums[h-1]) {
                mul = (mul * (nums[h] * nums[h - 1] % raund)) % raund;
                K -= 2;
                h -= 2;
            }
        }
        mul = (mul * biggest) % raund;
        std::cout << (mul + raund) % raund;
        return;
    }
}


// task 4

bool check_move(const vector<vector<int>>& chess, int i_check, int j_check){
    if (i_check >= 0 && i_check < chess.size() && j_check >= 0 && j_check < chess[0].size() && !chess[i_check][j_check])
        return true;
    return false;
}


void horse_travel(){

    vector<pair<int,int>> vecs{{2,-1}, {2,1}, {1,2}, {-1, 2},
                               {-2, 1}, {-2, -1}, {-1, -2},{1, -2} };

    int n, m;
    std::cin >> n >> m;
    vector<vector<int>> chess(n, vector<int>(m, 0));

    int i, j;
    std::cin >> i >> j;
    i = n - i + 1; // convert i-vector to standard right->down direction
    --i, --j;

    std::pair<int, int> current{n-1, 0};
    std::pair<int, int> aim{i, j};

    vector<pair<int, int>> to_visit(0);
    to_visit.push_back(current);
    int moves = 0;

    if (current == aim){
        std::cout << moves;
        return;
    }

    while(!to_visit.empty()){

        vector<pair<int, int>> to_visit_level;
        for(int k = 0; k < to_visit.size() || to_visit.begin() != to_visit.end(); ++k){
            to_visit_level.push_back(to_visit[0]);
            to_visit.erase(to_visit.begin());
        }

        while(!to_visit_level.empty()){
            current = to_visit_level.front();
            to_visit_level.erase(to_visit_level.begin());
            int i_now = current.first;
            int j_now = current.second;
            for(auto& dir : vecs){
                int i_move = i_now + dir.first;
                int j_move = j_now + dir.second;
                if (check_move(chess, i_move, j_move)){
                    if (i_move == i && j_move == j){
                        std::cout << moves + 1;
                        return;
                    }

                    to_visit.push_back({i_move, j_move});
                    chess[i_move][j_move] = true;
                }
            }
        }
        ++moves;
    }
    std::cout << "NEVAR";
}
