#include "FileManager.hpp"


std::vector<double> reader(std::string fileName) {

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
    return dataPoints;
}


void writerSpectralKernels(std::vector<std::complex<double>> data, std::string fileName) {


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
    return;
}


void writer(std::vector<FinishedNotes> data, std::string fileName) {

    std::string filePath = "../Projects/" + fileName + "_rd.txt";

    std::ofstream outFile;
    outFile.open(filePath);

    if (outFile.fail()) {
        std::cout << "Fehler beim öffnen der Datei " + fileName << filePath << std::endl;
        return;
    }

    for (int i = 0; i < data.size(); i++) {
        
        std::string note = "(" + std::to_string(data[i].noteValue) + "," + std::to_string(data[i].midi) + "," + "0)";
        outFile << note  << std::endl;
    }


    outFile.close();
    std::cout << "Done writing..." << std::endl;
    return;
}