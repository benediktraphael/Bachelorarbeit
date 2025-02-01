#pragma once
#include <vector>
#include <complex>
#include <cmath>
#include "createWindow.hpp"

struct SpectralKernel {
	std::vector<std::complex<double>> specVals;
	int startPoint;
};


std::vector<SpectralKernel> calculate_spectralKernels(double f_0=27.5, int k_num=88);

SpectralKernel clipSpectralKernel(std::vector<std::complex<double>> spectralKernel);

std::vector<std::complex<double>> FFTcq(std::vector<std::complex<double>> data);