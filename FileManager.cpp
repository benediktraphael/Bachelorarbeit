#include <fstream>
#include <iostream>
#include "FileManager.hpp"



std::vector<double> reader(std::string fileName) {

    std::cout << "Reader..." << std::endl;
    std::string filePath =fileName + ".txt";

    std::vector<double> dataPoints;


    std::ifstream inFile;

    inFile.open(filePath);

    if (inFile.fail()) {
        std::cout << "Fehler beim öffnen der Datei " + fileName << std::endl;
        return dataPoints;
    }


    double point;
    while (!inFile.eof()) {
        inFile >> point;
        dataPoints.push_back(point);
    }

    inFile.close();
    std::cout << "Reader finished...";
    return dataPoints;
}

//outFile.open(filePath, std::ofstream::app) to append.

void writer(std::vector<std::complex<double>> data, std::string fileName) {


    

    std::cout << "Writing..." << std::endl;
    std::string filePath =fileName + ".txt";

    std::ofstream outFile;
    outFile.open(filePath);

    if (outFile.fail()) {
        std::cout << "Fehler beim öffnen der Datei " + fileName << filePath << std::endl;
        return;
    }

    for (int i = 0; i < data.size(); i++) {
        outFile << data.at(i) << std::endl;
    }


    outFile.close();
    std::cout << "Done writing..." << std::endl;
    return;
}