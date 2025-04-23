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
    State vector_y_0;
    vector_y_0.y1 = vector_y_star.y1 + EPS;
    vector_y_0.y2 = vector_y_star.y2 + EPS;
    vector_y_0.y3 = vector_y_star.y3 + EPS;
    return vector_y_0;
}

State compute_stationary_solutions(){
    State y_star;
    y_star.y2 = sqrt(D*M + sqrt(D*D*M*M - 4*M*M*M + 3*M*M));
    y_star.y1 = -M/y_star.y2;
    y_star.y3 = D/2 + M/(y_star.y2*y_star.y2)*(1-M);
    return y_star;
}

// Right side of the system
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
    while (t <= TN + STEP) {
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

void writeToCSV(const TimeSeries& data, std::ofstream& file) {
    for (const auto& pair : data) {
        double time = pair.first;
        const State& state = pair.second;
        file << time << "," << state.y1 << "," << state.y2 << "," << state.y3 << "\n";
    }
}


int main(){
    std::ofstream file(FILENAME);
    if (!file.is_open()) {
        std::cerr << "Error with opening file!" << std::endl;
        return 1;
    }    
    file << "Time,y1,y2,y3\n";

    TimeSeries vector_y = runge_kutta_4_system();
    
    writeToCSV(vector_y, file);

    std::cout << "Data succesfully write to " << FILENAME << std::endl;
    file.close();
    return 0;
}