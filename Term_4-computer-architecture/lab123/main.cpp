#include <iostream>
#include <cmath>
#include <utility>
#include <vector>
#include "Register.h"





int main() {
    std::vector<int> bin_1{0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1};
    std::vector<int> bin_2{1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
    Register reg_1(-5);
    Register reg_2(2);

    Register result = reg_1 - reg_2;



    return 0;
}


// переполнение при сложении