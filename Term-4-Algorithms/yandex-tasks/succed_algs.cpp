//
// Created by Vladislav Kremenevskiy on 4/27/21.
//

#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <unordered_map>


using std::pair;
using std::vector;
using std::string;
using std::cin;
using std::map;


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


// task 5
void shortest_way() {

    long long N, M;
    std::cin >> N >> M;

    vector<vector<pair<long long, long long>>> adjList(N);
    for (int i = 0; i < M; ++i) {
        long from, to, weight;
        std::cin >> from >> to >> weight;
        --from, --to;
        adjList[from].push_back({to, weight});
        adjList[to].push_back({from, weight});
    }

    long long start, end;
    std::cin >> start >> end;
    --start, --end;

    std::set<pair<long, long>> to_visit;

    vector<long long> dekstra(N, INT64_MAX);

    to_visit.insert({0, start});
    dekstra[start] = 0;
    while (!to_visit.empty()) {
        int popped = to_visit.begin()->second;
        to_visit.erase(to_visit.begin());

        for (auto &element : adjList[popped]) {
            long long from = popped;
            long long to = element.first;
            long long weight = element.second;

            if (dekstra[to] > dekstra[from] + weight) {
                to_visit.erase({dekstra[to], to});
                dekstra[to] = dekstra[from] + weight;
                to_visit.insert({dekstra[to], to});
            }
        }
    }
    std::cout << dekstra[end];
}


// chess game
bool moveIsPossible(int whereX, int whereY, int X, int Y){
    if (whereX == X && whereY == Y) {
        return false;
    }
    if (whereX == X || whereY == Y
            ){
        return true;
    }
    return false;
}

void chess_game() {
    int N, M;
    std::cin >> N >> M;
    int X1, Y1, X2, Y2;
    std::cin >> X1 >> Y1 >> X2 >> Y2;

    vector<pair<int, int>> vec {{1, 1}, {-1, -1}, {1, -1}, {-1, 1}};

    for (auto dir : vec) {
        int newX2 = X2 + dir.first;
        int newY2 = Y2 + dir.second;
        while(newX2 <= N && newY2 <= M && newX2 >= 1 && newY2 >= 1) {

//            std::cout << "diag: " << newX2 << " " << newY2 << "\n";

            if (moveIsPossible(newX2, newY2, X1, Y1)){
                if (X1 < X2 && Y1 < Y2){
                    if (newX2 > X2 || newY2 > Y2){
                        newX2 += dir.first;
                        newY2 += dir.second;
                        continue;
                    }
                }
                if (X1 < X2 && Y1 > Y2){
                    if (newX2 > X2 || newY2 < Y2){
                        newX2 += dir.first;
                        newY2 += dir.second;
                        continue;
                    }
                }
                if (X1 > X2 && Y1 > Y2){
                    if (newX2 < X2 || newY2 < Y2){
                        newX2 += dir.first;
                        newY2 += dir.second;
                        continue;
                    }
                }
                if (X1 > X2 && Y1 < Y2){
                    if (newX2 < X2 || newY2 > Y2){
                        newX2 += dir.first;
                        newY2 += dir.second;
                        continue;
                    }
                }
//                std::cout << "Can go here and beat: " << newX2 << " " << newY2 << " Player: " << X1 << " " << Y1;
                std::cout << "YES";
                return;
            }

            newX2 += dir.first;
            newY2 += dir.second;

        }
    }
    std::cout << "NO";
}


void maxPalindrom() {
    string str;
    cin >> str;

    // check if all same
    char first = str[0];
    bool same = true;
    for(int i = 0; i < str.length(); ++i) {
        if (str[i] != first) {
            same = false;
            break;
        }
    }
    if (same){
        std::cout << -1;
        return;
    }

    // check if is it palindrome
    bool isPalindrome = true;

    for(int i = 0; i < str.length() / 2; ++i) {
        if (str[i] != str[str.length() - 1 - i]){
            isPalindrome = false;
        }
    }

    if (isPalindrome) {
        std::cout << str.length() - 1;
    }
    else {
        std::cout << str.length();
    }


}


void visokosniy() {
    int year;
    cin >> year;

    if (year % 4 == 0 && year % 400 == 0){
        std::cout << "YES";
        return;
    }
    if (year % 4 == 0 && year % 100 == 0) {
        std::cout << "NO";
        return;
    }
    if (year % 4 == 0) {
        std::cout << "YES";
    }
    else {
        std::cout << "NO";
    }

}


void multBigNum() {


    long long numToFind = 1087388483;

    long long N;
    cin >> N;

    long long nums[N];
    for (int i = 0; i < N; i++) {
        cin >> nums[i];
    }

    std::unordered_map<int,int> map;

    for(int i = 0; i < N; ++i) {
        if (nums[i] == 0){
            continue;
        }
        if (numToFind % nums[i] == 0){
            if (map.find(numToFind / nums[i]) == map.end()){
                vector<pair<int, int>> keys;
                for(auto kv : map){
                    keys.push_back(kv);
                }
                for (auto kv : keys){
                    if (numToFind / (kv.second * nums[i]) >= 1) {
                        map[numToFind / (kv.second * nums[i])] = nums[i] * kv.second;
                    }
                }
                map[numToFind / nums[i]] = nums[i];
                if (map.find(1) != map.end()){
                    std::cout << "YES";
                    return;
                }
            }
            else {
                std::cout << "YES";
                return;
            }
        }
    }
    std::cout << "NO";
}




// next permutation

void next() {
    string num;
    cin >> num;
    int len = num.length();
    if (len == 1) {
        std::cout << -1;
        return;
    }

    std::set<int> unique;
    vector<long long> toSort(0);

    int index_changed = len - 1;
    for(int i = len - 2; i >= 0; --i) {

        int right = num[i+1] - '0';
        int right_left = num[i] - '0';
        unique.insert(right);
        toSort.push_back(right);

        bool find_less = false;

        if (*(--unique.end()) > right_left){
            for(auto k = unique.begin(); k != unique.end(); k++){
                if (*k > right_left){
                    // delete first from sorted
                    auto it = std::find(toSort.begin(), toSort.end(), *k);

                    toSort.erase(it);
                    toSort.push_back(right_left);
                    find_less = true;
                    num[i] = *k + '0';
                    index_changed = i;
                    break;
                }
            }
            if (find_less) {
                break;
            }
        }

        if (i == 0){
            std::cout << -1;
            return;

        }
    }


    for(int i = 0; i <= index_changed; i++){
        std::cout << num[i];
    }

    std::sort(toSort.begin(), toSort.end());


    for(auto el : toSort) {
        std::cout << el;
    }
}



void bigCush(){
    long long X;
    cin >> X;

    if (X % 10 == 0) {
        std::cout << "NO";
    }
    else{
        std::cout << X % 10;
    }
}



void make_set_del(vector<int>& parent, int v){
    parent[v] = v;
}

int find_set_del(vector<int>& parent, int v){
    if(v == parent[v]){
        return v;
    }
    return find_set_del(parent, parent[v]);
}

void union_sets_del(vector<int>& parent, int a, int b){
    a = find_set_del(parent, a);
    b = find_set_del(parent, b);
    if ( a != b) {
        parent[b] = a;
    }
}

void deletionEdge(){
    int N, M;
    std::cin >> N >> M;

    if (M == 1 && N == 1) {
        std::cout << -1;
        return;
    }

    vector<int> parent(N);
    for(int i = 0; i < N; ++i){
        parent[i] = i;
    }
    int v1, v2;
    for(int i = 0; i < M; ++i){
        std::cin >> v1 >> v2;
        union_sets_del(parent, v1-1, v2-1);
    }

    for(int i = 0; i < parent.size() - 1; ++i) {
        int p1 = find_set_del(parent, parent[i]);
        int p2 = find_set_del(parent, parent[i+1]);
        if (p1 != p2) {
            std::cout << -1;
            return;
        }
    }

    int edges_enough = N - 1;
    int need_to_delete = M - edges_enough;
    std::cout << need_to_delete;

}




void inverting() {
    string s;
    cin >> s;
    int len = s.size();

    vector<int> shouldInvert(len, 0);

    int cnt_requests;
    cin >> cnt_requests;

    for(int i = 0; i < cnt_requests; ++i) {
        int start, end;
        cin >> start >> end;

        if (start >= end) {
            std::swap(start, end);
        }
        shouldInvert[start-1]++;
        shouldInvert[end]--;
    }

    for(int i = 1; i < len+1; ++i) {
        shouldInvert[i] += shouldInvert[i-1];
    }

    for(int i = 0; i < len; ++i) {
        if (shouldInvert[i] % 2 == 1) {
            char ch = s[i];
            s[i] = ch >= 'a' ? s[i] - 32 : s[i] + 32;
        }
        std::cout << s[i];
    }
}



long long merge(vector<int>& arr, vector<int>& left, vector<int>& right) {
    int i = 0, j = 0;
    long long count = 0;

    while(i < left.size() || j < right.size()) {
        if (i == left.size()){
            arr[i+j] = right[j];
            ++j;
        }
        else if (j == right.size()) {
            arr[i+j] = left[i];
            ++i;
        }
        else if(left[i] <= right[j]){
            arr[i+j] = left[i];
            ++i;
        }
        else {
            arr[i+j] = right[j];
            ++j;
            count += left.size() - i;
        }

    }
    return count;
}


long long merge_inv(vector<int>& arr){
    if (arr.size() < 2) {
        return 0;
    }

    int m = (arr.size() + 1) / 2;
    vector<int> left;
    for(int i = 0; i < m; i++) {
        left.push_back(arr[i]);
    }

    vector<int> right;
    for(long long i = m; i < arr.size(); i++) {
        right.push_back(arr[i]);
    }

    return merge_inv(left) + merge_inv(right) + merge(arr, left, right);
}



void find_inv(){
    int N;
    cin >> N;
    vector<int> perm(N);
    for(int i = 0; i < N; ++i) {
        cin >> perm[i];
    }

    std::cout << merge_inv(perm);
}



void alignment() {
    int N;
    cin >> N;

    long long prev;
    cin >> prev;

    long long max = prev;
    long long ans = 0;

    for(int i = 1; i < N; i++) {
        int current;
        cin >> current;

        if (max < current) {
            ans += current - max;
            max = current;
        }
        else {
            if (current < prev) {
                ans += prev - current;
            }
        }
        prev = current;
    }

    std::cout << ans;
}




const long long module = 1000000007;
vector<vector<long long>> multMatrix(const vector<vector<long long>>& arr_1, const vector<vector<long long>>& arr_2) {
    const long long N = arr_1.size();
    vector<vector<long long>> result (N, vector<long long>(N, 0));

    for(int i = 0; i < N; ++i) {
        for(int k = 0; k < N; ++k) {
            for(int l = 0;l < N; l++) {
                result[i][k] = (result[i][k] + (arr_1[i][l] * arr_2[l][k]) % module) % module;
            }
        }
    }

    return result;
}


vector<vector<long long>> binpow(vector<vector<long long>> matrix, int n) {
    if (n == 0) {
        vector<vector<long long>> ret(matrix[0].size(), vector<long long> (matrix[0].size(), 0));
        for (int i = 0; i < matrix.size(); i++) {
            ret[i][i] = 1;
        }
        return ret;
    }

    if (n % 2 == 1) {
        return multMatrix(binpow(matrix, n-1), matrix);
    }
    else {
        auto b = binpow(matrix, n/2);
        return multMatrix(b, b);
    }
}


void number_ways() {

    int N, M;
    cin >> N >> M;
    int U, V;
    cin >> U >> V;

    long long L;
    cin >> L;

    vector<vector<long long>> idMatrix(N, vector<long long> (N, 0));

    for(int i = 0; i < M; ++i) {
        int v1, v2;
        cin >> v1 >> v2;
        idMatrix[v1-1][v2-1] ++;
        idMatrix[v2-1][v1-1] ++;

    }

    auto result = binpow(idMatrix, (int)L);


//    for(int i = 0; i < N; i++) {
//        for(int j = 0; j < N; j++) {
//            std::cout << result[i][j]  << " ";
//        }
//        std::cout << '\n';
//    }
    std::cout << result[U-1][V-1] % module;
}