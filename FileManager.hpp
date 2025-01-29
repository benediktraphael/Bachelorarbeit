#pragma once
#include <vector>
#include <complex>
#include <fstream>
#include <iostream>
#include "AnalyseCQT.hpp"


std::vector<double> reader(std::string fileName);

void writerSpectralKernels(std::vector<std::complex<double>> data, std::string fileName);

void writer(std::vector<FinishedNotes> data, std::string fileName);