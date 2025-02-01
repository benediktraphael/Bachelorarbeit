#pragma once
#include <complex>
#include <vector>
#include <cmath>
#include "calcSpektral.hpp"

std::vector<std::complex<double>> DFT(std::vector<double> data);

std::vector<std::complex<double>> FFT(std::vector<std::complex<double>> data);

std::vector<std::vector<std::complex<double>>> STFT(std::vector<std::complex<double>> data, std::vector<double> window);

std::vector<std::vector<std::complex<double>>> CQT(std::vector<std::complex<double>> data, std::vector<SpectralKernel> spectralKernels,  double f_0 = 27.5, int k_num = 88);


std::vector<std::complex<double>> prepare_FFT(std::vector<double> data);

std::vector<std::complex<double>> PrepareCQT(std::vector<double> data, double f_0 = 27.5, int k_num = 88);

