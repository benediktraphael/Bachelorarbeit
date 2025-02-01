#pragma once
#include <vector>
#include <complex>
#include <cmath>

struct GuterName {
	std::vector<std::vector<double>> cq;
	double refValue;
};

GuterName CQ_to_real_values(std::vector<std::vector<std::complex<double>>> CQ);

std::vector<std::vector<double>> CQ_to_dB(GuterName gN);