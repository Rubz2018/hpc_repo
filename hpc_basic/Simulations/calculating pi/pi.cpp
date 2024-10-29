#include <iostream>
#include <random>
#include <chrono>

int main()
{
    int n = 10000000; // Total number of points
    int count = 0;    // Points inside the circle
    double x, y, r;

    // Set up random number generation
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(-1.0, 1.0);

    // Start timer
    auto start_time = std::chrono::high_resolution_clock::now();

    // Monte Carlo simulation
    for (int j = 0; j < n; ++j)
    {
        x = dis(gen); // Random x in [-1, 1]
        y = dis(gen); // Random y in [-1, 1]
        r = x * x + y * y;

        if (r <= 1.0)
        {
            count++;
        }
    }

    // Estimate Pi
    double pi = 4.0 * static_cast<double>(count) / n;

    // End timer
    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end_time - start_time;

    // Output results
    std::cout << "pi: " << pi << ", i: " << count << ", n: " << n << std::endl;
    std::cout << "The elapsed time: " << elapsed.count() << " seconds" << std::endl;

    return 0;
}
