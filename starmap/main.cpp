#include "StarMap.h"

#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>


// This file provides an interactive loop.
// Edit it to change the number of stars returned.


std::ostream& operator << (std::ostream& stream, const Star& star) {
    return (stream
        << "Star " << star.id
        << " ("    << star.x
        << ", "    << star.y
        << ", "    << star.z
        << ')'
    );
}


int main(int argc, char** argv) {
    if(argc != 2) {
        std::cout << "USAGE: " << argv[0] << " [data-file]\n";
        std::exit(1);
    }

    // Edit this bit!
    size_t count = 5;
    StarMap* map;

    try {
        std::ifstream file(argv[1]);
        map = StarMap::create(file);
    }
    catch(const std::exception& e) {
        std::cout << "Error reading file: " << e.what() << '\n';
        std::exit(1);
    }

    std::string line;
    std::cout << "xyz> ";
    while(std::getline(std::cin, line)) {
        try {
            float x, y, z;
            std::istringstream coords(line);
            if(!(coords >> x >> y >> z)) {
                throw std::runtime_error("Could not read line.");
            }

            std::vector<Star> stars = map->find(count, x, y, z);
            for(const Star& star: stars) {
                std::cout << " - " << star << '\n';
            }
            if(stars.size() == 0) {
                std::cout << " (no results)\n";
            }
        }
        catch(const std::exception& e) {
            std::cout << "Error: " << e.what() << '\n';
        }

        std::cout << "xyz> ";
    }

    delete map;
    return 0;
}
