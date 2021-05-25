#include <iostream>
#include <ctime>
#include "RBTree.h"
#include <iomanip>
#include <vector>
#include <cstdio>
#include <chrono>
#include <set>
#include <unordered_set>
#include <map>

const int MAX = 10000;

std::vector<int> generateArr(const int N) {
    std::vector<int> arr(N, 0);
    for (int i = 0; i < N; ++i) {
        arr[i] = rand() % MAX;
    }
    return arr;
}


void insertTask(RBTree<int> &tree, std::vector<int> &nums) {
    for (int i = 0; i < nums.size(); ++i) {
        tree.insert(nums[i]);
    }
}


std::vector<std::pair<int, int>> generateContainer(const int N) {
    std::vector<std::pair<int, int>> container(N);
    for(int i = 0; i < N; ++i) {
        int num = rand() % MAX;
        container[i].first = num;
        container[i].second = num;
    }
    return container;
}



void insertMapTest(std::map<int, int> map, std::vector<std::pair<int, int>> & container){
    for(int i = 0; i < container.size(); ++i) {
        map.insert({container[i].first, container[i].second});
    }
}


void deleteTask(RBTree<int> &tree, const int N) {
    for(int i = 0; i < 100; ++i) {
        int num = rand() % MAX;
        tree.remove(num);
    }
}


int main() {
    srand(time(nullptr));

    const int N = 1000000;
    const int N_delete = N;

    RBTree<int> bst;
    std::vector<int> nums = generateArr(N);


    std::map<int, int> tree;
    std::vector<std::pair<int, int>> container = generateContainer(N);


    auto start = clock();
    {
        insertTask(bst, nums);
//        deleteTask(bst, N_delete);
//        insertMapTest(tree, container);
    }
    auto end = clock();
    double time_taken = std::difftime(end, start) / CLOCKS_PER_SEC;

    std::cout << "Time taken: " << time_taken << "\n";
    std::cout << "Execution time: " << std::setprecision(6) << std::fixed << time_taken << " sec\n";

    return 0;
}
