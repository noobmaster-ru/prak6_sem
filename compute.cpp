#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <utility>
#include <iomanip>

#include "constants.h"

struct State {
    double y1, y2, y3;
};


typedef std::pair<double, State> TimeStatePair;
typedef std::vector<TimeStatePair> TimeSeries;

State compute_begining_values(State& vector_y_star){
    State vector_y_0;
    vector_y_0.y1 = vector_y_star.y1 + EPS;
    vector_y_0.y2 = vector_y_star.y2 + EPS;
    vector_y_0.y3 = vector_y_star.y3 + EPS;
    return vector_y_0;
}

State compute_stationary_solutions(){
    State y_star;
    y_star.y2 = sqrt(D*M + sqrt(D*D*M*M -4*M*M*M + 3*M*M));
    y_star.y1 = -M/y_star.y2;
    y_star.y3 = D/2 + M/(y_star.y2*y_star.y2)*(1-M);
    return y_star;
}

// Правая часть системы
State func(double t, State y) {
    State dy;
    dy.y1 = y.y1 - (D / 2.0) * y.y2 + y.y2 * (y.y3 + y.y1 * y.y1);
    dy.y2 = (D / 2.0) * y.y1 + y.y2 + y.y1 * (3 * y.y3 - y.y1 * y.y1);
    dy.y3 = -2.0 * y.y3 * (M + y.y1 * y.y2);
    return dy;
}

TimeSeries runge_kutta_4_system(){
    State vector_y_star = compute_stationary_solutions();
    State vector_y_0 = compute_begining_values(vector_y_star);
    double t = T0;
    State y = vector_y_0;
    TimeSeries results;
    while (t <= TN+EPS) {
        results.push_back({t, y});

        State k1 = func(t, y);
        State k2 = func(t + STEP/2, { y.y1 + STEP/2 * k1.y1, y.y2 + STEP/2 * k1.y2, y.y3 + STEP/2 * k1.y3 });
        State k3 = func(t + STEP/2, { y.y1 + STEP/2 * k2.y1, y.y2 + STEP/2 * k2.y2, y.y3 + STEP/2 * k2.y3 });
        State k4 = func(t + STEP,   { y.y1 + STEP * k3.y1,  y.y2 + STEP * k3.y2,  y.y3 + STEP * k3.y3  });

        y.y1 += STEP/6 * (k1.y1 + 2*k2.y1 + 2*k3.y1 + k4.y1);
        y.y2 += STEP/6 * (k1.y2 + 2*k2.y2 + 2*k3.y2 + k4.y2);
        y.y3 += STEP/6 * (k1.y3 + 2*k2.y3 + 2*k3.y3 + k4.y3);

        t += STEP;
    }
    return results;
}

void writeToCSV(const TimeSeries& data, const std::string& filename,int traj_id = -1) {
    std::ofstream file(filename, std::ios::app); // 👈 режим добавления
    if (!file.is_open()) {
        std::cerr << "Ошибка открытия файла " << filename << "\n";
        return;
    }
    // Можно вставить комментарий или индекс траектории
    // if (traj_id >= 0)
    //     file << "# Trajectory " << traj_id << "\n";


    for (const auto& pair : data) {
        double time = pair.first;
        const State& state = pair.second;
        // file << std::fixed << std::setprecision(6)
        file << time << "," << state.y1 << "," << state.y2 << "," << state.y3 << "\n";
    }
    // Пустая строка для отделения траекторий
    // file << "\n";

    file.close();
    // // Проходим по всем данным в TimeSeries и записываем их в файл
    // for (const auto& pair : data) {
    //     double time = pair.first;
    //     const State& state = pair.second;
        
    //     // Записываем время и значения состояний в CSV формате
    //     file << time << "," << state.y1 << "," << state.y2 << "," << state.y3 << "\n";
    // }
}


int main(){
    // Открываем файл для записи
    std::string filename = "data.csv";
    // 💡 при первом запуске можно добавить заголовок (если нужно)
    static bool first_time = true;
    if (first_time) {
        std::ofstream header_file(filename, std::ios::app); // без app: перезаписываем
        if (header_file.tellp() == 0) {
            header_file << "Time,y1,y2,y3\n";
        }
        header_file.close();
        first_time = false;
    }
    // // Открываем файл для записи
    // std::ofstream file("data.csv");
    // if (!file.is_open()) {
    //     std::cerr << "Ошибка при открытии файла!" << std::endl;
    //     return 1;
    // }    
    // // Записываем заголовок CSV
    // file << "Time,y1,y2,y3\n";


    TimeSeries vector_y = runge_kutta_4_system();
    
    // Записываем данные в файл "output.csv"
    writeToCSV(vector_y, filename,NUM_TRAJECTORY);

    std::cout << "Данные успешно записаны в файл data.csv\n" << std::endl;
    // // Закрываем файл
    // file.close();
    return 0;
}