#include <iostream>
#include <cmath>

#define show true

class QuadraticEquation {
    double a;
    double b;
    double c;
    double D;
    double x1;
    double x2;

public:
    QuadraticEquation() {
        this->a = 1;
        this->b = 1;
        this->c = 1;
    }

    QuadraticEquation (double a, double b, double c) {
        this->a = a;
        this->b = b;
        this->c = c;
        if (show) {
            std::cout << "Quadratic equation:\n";
            std::cout << a << " * x^2 + " << b << " * x + " << c << " = 0\n";
        }
    }

    double findDiscriminant() {
        D = pow(b, 2) - 4 * a * c;
        if (show) {
            std::cout << "\nDiscriminant is: \n";
            std::cout << "D = b^2 - 4ac\n";
            std::cout << "D = " << b << "^2 - 4 * " << a << " * " << c << '\n';
            std::cout << "D = " << D << '\n';
        }
    };

    double getDiscriminant() {
        return D;
    }

    void solve () {
        if (a == 0) {
            std::cout << "a can't be zero!!\n";
            std::cout << "Equation isn't quadratic!\n";
            return;
        }
        findDiscriminant();
        if (D < 0) {
            std::cout << "D < 0 !!!\n";
            std::cout << "No roots  in real numbers\n";
            return;
        }
        if (D != 0) {
            x1 = (-b + sqrt(D)) / 2 * a;
            x2 = (-b - sqrt(D)) / 2 * a;
        }
        else {
            x1 = -b / (2 * a);
            x2 = -b / (2 * a);
        }

        if (show) {
            std::cout << "Finding roots:\n";
            if (x1 != x2 || D != 0) {
                std::cout << "x1 = (-b + sqrt(D) ) / 2a\n";
                std::cout << "x1 = " << "(" << -b << " + sqrt(" << D << ")) / 2 * " << a << "\n";
                std::cout << "x1 = " << x1 << '\n';

                std::cout << "x2 = (-b - sqrt(D) ) / 2a\n";
                std::cout << "x2 = " << "(" << -b << " - sqrt(" << D << ")) / 2 * " << a << "\n";
                std::cout << "x2 = " << x2 << '\n';
                std::cout << "\tResult:\n";
                std::cout << "x1 = " << x1 << '\n';
                std::cout << "x2 = " << x2 << '\n';
            }
            else {
                std::cout << "Discriminant = 0!!\n";
                std::cout << "Then we have only 1 root!\n";
                std::cout << "x = -b / 2a\n";
                std::cout << "x = " << -b << " / 2 * " << a << '\n';
                std::cout << "x = " << x1 << '\n';
            }
        }
    }
};


void solveQuadratic() {
    double a, b, c;
    std::cout << "Enter a, b, c! \n";
    std::cout << "a = ";
    std::cin >> a;
    std::cout << "b = ";
    std::cin >> b;
    std::cout << "c = ";
    std::cin >> c;

    QuadraticEquation equation(a, b, c);
    equation.solve();
}


int main() {
    solveQuadratic();

    return 0;
}


