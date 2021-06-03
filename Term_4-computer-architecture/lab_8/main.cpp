#include <iostream>
#include <cmath>

class FindSumFunc{
public:
    double a;
    double b;
    double h;
    double e;
    double S;
    double x;
    double Y;
    int iteration_cnt;

    FindSumFunc(double a, double b, double h, double e) {
        this->a = a;
        this->b = b;
        this->h = h;
        this->e = e;
        this->Y = 0;
        this->S = 0;
        this->iteration_cnt = 0;
    }

    double find_y(double xx) {
        double y = 1/2 - M_PI / 4 * abs(sin(xx));
        return y;
    }

    double find_s(int k) {
        double s = cos(2 * k * this->x) / (4 * k * k - 1);
        return s;
    }


    double solve() {
        std::cout << "\t\tФункции варианта 14: \n\n";
        std::cout << "S = sum ( cos(2kx) / (4*k*k - 1) )\n";
        std::cout << "Y = 1/2 - PI/4 * | sin(x) |\n\n";
        std::cout << "|Y(x) - S(x)|   стремиться к 0.5. (при количестве итераций -> бесконечности)\n";
        std::cout << "Исходные данные: \n";
        std::cout << "a = " << a << " | b = " << b << " | h = " << h << " | e = " << e << "\n\n";
        x = a;
        for(int k = 1; x <= b; x += h) {
            std::cout << "\tx = " << x << '\n';

            Y = find_y(x);
            std::cout << "\tY = " << Y << '\n';

            iteration_cnt = 0;
            double sum = 0;
            double diff = 0;
            do {
                ++iteration_cnt;
                sum += find_s(iteration_cnt);
                diff = abs(Y - sum);
                std::cout << iteration_cnt << ". S = " << sum << " | diff = " << diff << '\n';
            }
            while(abs(diff - 0.5) > e);
            std::cout << "Для достижения необходимой точночти понадобилось\nитераций = " << iteration_cnt << '\n';
            std::cout << "\n";
        }
    }

};



void preprocessing(){
    double a;
//    std::cout << "a = ";
//    std::cin >> a;
//
//    double b;
//    std::cout << "b = ";
//    std::cin >> b;
//
//    double h;
//    std::cout << "h = ";
//    std::cin >> h;
//
//    double e;
//    std::cout << "e = ";
//    std::cin >> e;

    FindSumFunc task(-1000.3, -1000, 0.1 , 0.00000001);
    task.solve();
}


int main() {
//    FindSumFunc a(2, 2, 2, 2);
//    a.solve();
    preprocessing();
}
