#include "Dictionary.h"

#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>

// This file provides an interactive loop.
// It's much easier to use in conjunction with helper.py.
// See the hints section in the readme for details.


std::vector<Point> read_points(const std::string& line) {
    Point point;
    std::vector<Point> results;
    std::istringstream stream(line);
    while(stream >> point.x) {
        if(!(stream >> point.y)) {
            throw std::runtime_error("Odd number of points.");
        }

        results.push_back(point);
    }

    if(results.size() == 0) {
        throw std::runtime_error("No points given.");
    }

    return results;
}

int main(int argc, char** argv) {
    if(argc != 2) {
        std::cout << "USAGE: " << argv[0] << " [words-file]\n";
        std::exit(1);
    }

    // Change these to test different cases!
    size_t maxcount = 5;
    float  cutoff   = 0;

    // Read in the words file
    Dictionary* dictionary = nullptr;
    try {
        std::ifstream stream(argv[1]);
        dictionary = new Dictionary(stream);
    }
    catch(const std::exception& e) {
        std::cout << "Error reading words file: " << e.what() << '\n';
        std::exit(1);
    }

    // Set floating point format
    std::cout << std::setprecision(3);
    std::cout << std::fixed;

    // Interactive loop
    std::string line;
    std::cout << "> ";
    while(std::getline(std::cin, line)) {
        try {
            auto points = read_points(line);
            auto heap   = dictionary->correct(points, maxcount, cutoff);

            std::vector<Heap::Entry> entries;
            while(heap.count() > 0) {
                entries.push_back(heap.pop());
            }

            for(auto itr = entries.rbegin(); itr != entries.rend(); ++itr) {
                std::cout << " - " << itr->score << ": " << itr->value << '\n';
            }
            if(entries.size() == 0) {
                std::cout << " (no results)\n";
            }
        }
        catch(const std::exception& e) {
            std::cout << "Error: " << e.what() << '\n';
        }

        std::cout << "> ";
    }

    delete dictionary;
    return 0;
}
