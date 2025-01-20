#pragma once
#include <vector>
#include <complex>

std::vector<double> reader(std::string fileName);

void writer(std::vector<std::complex<double>> data, std::string fileName);