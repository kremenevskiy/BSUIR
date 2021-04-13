//
// Created by Vladislav Kremenevskiy on 4/12/21.
//

#include "Register.h"


void Register::setBinary(const std::vector<int> &binArr) {
    binary = binArr;
    number = (int)(*this);
}


void Register::setNumber(const int num){
    number = num;
    binary = makeBinary(abs(num));
    if (num < 0) {
        twos_complement(binary);
    }
}


void Register::setRegister(const Register& reg) {
    number = reg.number;
    binary = reg.binary;
}



void Register::reverseBits(){
    reverseArrBits(binary);
    ++(*this);
}


Register Register::reverseBits(const Register& reg){
    Register reversed(reg.binary);
    reversed.reverseBits();
    return reversed;
}


void Register::twos_complement(std::vector<int>& bin){
    reverseArrBits(bin);
    int i = N-1;
    while(i >= 0){
        if (bin[i] == 1) {
            bin[i] = 0;
        }
        else {
            bin[i] = 1;
            break;
        }
        --i;
    }
}


void Register::printBits() const{
    for(int i = 0; i < N; ++i) {
        std::cout << binary[i];
    }
}


std::vector<int> Register::makeBinary(int num) {

    std::vector<int> binArr(N, 0);
    int i = 0;
    while(num > 0) {
        binArr[N-1-i] = num % 2;
        num /= 2;
        ++i;
    }
    return binArr;
}


void Register::reverseArrBits(std::vector<int> &arr) {
    for(int i = 0; i < N; ++i) {
        arr[i] == 1 ? arr[i] = 0 : arr[i] = 1;
    }
}


int Register::toInt(const Register& reg){
    int intNum = 0;
    intNum -= reg.binary[0] * pow(2, N - 1);
    for(int i = N - 1; i > 0; --i){
        if (reg.binary[i] == 0){
            continue;
        }
        intNum += pow(2, N-i-1);
    }
    return intNum;
}


Register::Register() {
    binary = std::vector<int>(N, 0);
    number = 0;
}


Register::Register(int num) : Register() {
    setNumber(num);
}


Register::Register(const std::vector<int> &bitsArr) : Register() {
    setBinary(bitsArr);
}


Register::Register(const Register& reg){
    setNumber(reg.number);
}


Register& Register::operator=(const Register& reg){
    setRegister(reg);
    return *this;
}


int& Register::operator[](const int index){
    return this->binary[index];
}


const int& Register::operator[](const int index) const {
    return this->binary[index];
}


Register& Register::operator++(){
    int i = N-1;
    while(i >= 0){
        if (binary[i] == 0){
            binary[i] = 1;
            break;
        }
        binary[i] = 0;
        --i;
    }
    return *this;
}


Register Register::operator++(int){
    Register temp(binary);
    ++(*this);
    return temp;
}


Register Register::operator+(const Register &reg_2){
    int r{};
    int r_prev{};
    Register result;
    if (show){
        std::cout << "---Сложение---\n";
        std::cout << "Первое число: " << int(*this) << " (" << this->binary << ")"<< '\n';
        std::cout << "Второе число: " << int(reg_2) << " (" << this->binary << ")"<< '\n';


        std::cout << std::setw(5);
        std::cout << "|num_1|" << " |num_2|" << " |CF|" << " |res|\n";
    }
    for(int i = N-1; i >= 0; --i) {
        r_prev = r;
        if ((this->binary[i] + reg_2[i] + r) == 1) {
            r = 0;
            result[i] = 1;
        }
        else if ((this->binary[i] + reg_2[i] + r) == 2) {
            r = 1;
            result[i] = 0;
        }
        else if(this->binary[i] + reg_2[i] + r == 3) {
            r = 1;
            result[i] = 1;
        }
        else{
            r = 0;
            result[i] = this->binary[i] + reg_2[i];
        }
        if (show){
            std::cout << std::setw(4) << binary[i];
            std::cout << std::setw(8) << reg_2[i];
            std::cout << std::setw(6) << r_prev;
            std::cout << std::setw(6) << result[i] << '\n';
        }

    }
    if ((this->binary[0] == reg_2[0]) && (this->binary[0] != result[0])){
        result.flags.OF = 1;
        std::cout << "Переполнение\n";
    }

    if(show){
        std::cout << (int)*this << " + " << (int)reg_2 << " = " << (int)result << '\n';
        std::cout << "Результат: " << (int)result << " (" << result.binary << ")\n";
    }

    return result;
}


Register Register::operator+(int& num){
    Register reg_2(num);
    Register result = *this + reg_2;
    return result;
}


Register operator+(int& num, Register& reg_2){
    Register result = reg_2 + num;
    return result;
}


Register Register::operator-(const Register& reg_2){
    if (show){
        std::cout << "---Вычитание---\n";
        std::cout << (int)*this << " - " << (int)reg_2 << '\n';
        std::cout << "Первое число: " << int(*this) << " (" << this->binary << ")"<< '\n';
        std::cout << "Второе число: " << int(reg_2) << " (" << this->binary << ")"<< '\n';
    }

    Register reg_2_temp(reg_2);
    reg_2_temp.reverseBits();
    if (show){
        std::cout << "Инвертирование 2 числа:\n";
        std::cout << "~ " << reg_2.binary << " = " << reg_2_temp.binary << " (" << (int)reg_2_temp << ")\n";
    }
    Register result = *this + reg_2_temp;
    return result;
}


Register Register::operator-(int& num){
    Register reg_2(num);
    Register result = *this - reg_2;
    return result;
}


Register operator-(int& num, Register& reg_2){
    Register reg_1(num);
    Register result = reg_1 - reg_2;
    return result;
}


Register::operator int() const {
    int intNum = 0;
    intNum -= this->binary[0] * (int)pow(2, N - 1);
    for(int i = N - 1; i > 0; --i){
        if (this->binary[i] == 0){
            continue;
        }
        intNum += pow(2, N-i-1);
    }
    return intNum;
}


std::ostream& operator<< (std::ostream &out, const Register& reg) {
    for(int i = 0; i < Register::N; ++i){
        out << reg[i] << ' ';
        if (i == 7){
            out  << ' ';
        }
    }
    out << '\n';
    return out;
}

std::ostream& operator<< (std::ostream &out, const std::vector<int>& bitsArr) {
    for(int i = 0; i < bitsArr.size(); ++i){
        out << bitsArr[i];
        if (i == 7){
            out  << ' ';
        }
    }
    return out;
}


std::istream& operator>> (std::istream &in, Register& reg){
    int num;
    in >> num;
    Register newRegister(num);
    reg = newRegister;
    return in;
}
