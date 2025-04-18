#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <utility>

#include "constants.h"

struct State {
    double y1, y2, y3;
};


typedef std::pair<double, State> TimeStatePair;
typedef std::vector<TimeStatePair> TimeSeries;

State compute_begining_values(State& vector_y_star){
    double y1_0 = vector_y_star.y1 + EPS;
    double y2_0 = vector_y_star.y2 + EPS;
    double y3_0 = vector_y_star.y3 + EPS;

    State vector_y_0;
    vector_y_0.y1 = y1_0;
    vector_y_0.y2 = y2_0;
    vector_y_0.y3 = y3_0;
    return vector_y_0;
}

State compute_stationary_solutions(double D,double M){
    State y;

    double y2_star = sqrt(D*M + sqrt(D*D*M*M -4*M*M*M + 3*M*M));
    double y1_star = -M/y2_star;
    double y3_star = D/2 + M/(y2_star*y2_star)*(1-M);

    y.y1 = y1_star;
    y.y2 = y2_star;
    y.y3 = y3_star;
    return y;
}

// Правая часть системы
State func(double t, State y,double D, double M) {
    State dy;

    dy.y1 = y.y1 - (D / 2.0) * y.y2 + y.y2 * (y.y3 + y.y1 * y.y1);
    dy.y2 = (D / 2.0) * y.y1 + y.y2 + y.y1 * (3 * y.y3 - y.y1 * y.y1);
    dy.y3 = -2.0 * y.y3 * (M + y.y1 * y.y2);

    return dy;
}

TimeSeries runge_kutta_4_system(double D,double M){
    State vector_y_star = compute_stationary_solutions(D,M);
    State vector_y_0 = compute_begining_values(vector_y_star);
    double t = T0;
    State y = vector_y_0;
    TimeSeries results;
    // std::cout << "OK" << std::endl;
    while (t <= TN) {
        results.push_back({t, y});

        State k1 = func(t, y, D, M);
        State k2 = func(t + STEP/2, { y.y1 + STEP/2 * k1.y1, y.y2 + STEP/2 * k1.y2, y.y3 + STEP/2 * k1.y3 }, D, M);
        State k3 = func(t + STEP/2, { y.y1 + STEP/2 * k2.y1, y.y2 + STEP/2 * k2.y2, y.y3 + STEP/2 * k2.y3 }, D, M);
        State k4 = func(t + STEP,   { y.y1 + STEP * k3.y1,  y.y2 + STEP * k3.y2,  y.y3 + STEP * k3.y3  }, D, M);

        y.y1 += STEP/6 * (k1.y1 + 2*k2.y1 + 2*k3.y1 + k4.y1);
        y.y2 += STEP/6 * (k1.y2 + 2*k2.y2 + 2*k3.y2 + k4.y2);
        y.y3 += STEP/6 * (k1.y3 + 2*k2.y3 + 2*k3.y3 + k4.y3);

        t += STEP;
    }
    return results;
}

void writeToCSV(const TimeSeries& data, const std::string& filename) {
    // Открываем файл для записи
    std::ofstream outFile(filename);
    
    if (!outFile.is_open()) {
        std::cerr << "Ошибка при открытии файла!" << std::endl;
        return;
    }

    // Записываем заголовок CSV
    outFile << "Time,y1,y2,y3\n";

    // Проходим по всем данным в TimeSeries и записываем их в файл
    for (const auto& pair : data) {
        double time = pair.first;
        const State& state = pair.second;
        
        // Записываем время и значения состояний в CSV формате
        outFile << time << "," << state.y1 << "," << state.y2 << "," << state.y3 << "\n";
    }

    // Закрываем файл
    outFile.close();
}


int main(){
    double D,M;
    for (double D = 0.0; D < TN; D = D + STEP){
        for (double M = 0.0; M < TN;M = M + STEP){
            TimeSeries vector_y = runge_kutta_4_system(D,M);
            
            // Записываем данные в файл "output.csv"
            writeToCSV(vector_y, "output.csv");
        }
    }
    std::cout << "Данные успешно записаны в файл output.csv" << std::endl;
    return 0;
}