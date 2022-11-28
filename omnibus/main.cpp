#include "Atlas.h"

#include <fstream>
#include <iostream>
#include <stdexcept>

int main(int argc, char** argv) {
    if(argc != 2) {
        std::cout << "USAGE: " << argv[0] << " [data-file]\n";
        std::exit(1);
    }

    Atlas* atlas = nullptr;
    try {
        std::ifstream file(argv[1]);
        if(file.fail()) {
            throw std::runtime_error("Could not open file.");
        }

        atlas = Atlas::create(file);
    }
    catch(const std::exception& e) {
        std::cout << "Error reading file: " << e.what() << '\n';
        std::exit(1);
    }

    std::string sname;
    std::string dname;

    std::cout << "From: ";
    while(std::getline(std::cin, sname)) {
        std::cout << "To:   ";
        if(!std::getline(std::cin, dname)) {
            break;
        }

        try {
            Trip trip = atlas->route(sname, dname);
            std::cout << "Start at " << trip.start << '\n';
            for(const Trip::Leg& leg: trip.legs) {
                std::cout << " - " << leg.line << " to " << leg.stop << '\n';
            }
        }
        catch(const std::exception& e) {
            std::cout << "Error: " << e.what() << '\n';
        }

        std::cout << "From: ";
    }

    delete atlas;
    return 0;
}
