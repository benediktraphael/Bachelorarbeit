#pragma once

#include <complex>
#include <vector>


std::vector<std::complex<double>> FT(std::vector<double> data);

std::vector<std::complex<double>> FFT(std::vector<std::complex<double>> data);


std::vector<std::complex<double>> PrepareFFT(std::vector<double> data);


std::vector<std::vector<std::complex<double>>> STFT(std::vector<std::complex<double>> data, std::vector<double> window);


std::vector<std::vector<std::complex<double>>> CQT(std::vector<std::complex<double>> data, std::vector<std::vector<std::complex<double>>> spectralKernels, std::vector<int> startIndizes,  double f_0 = 27.5, int k_num = 88);

std::vector<std::complex<double>> PrepareCQT(std::vector<double> data, double f_0 = 27.5, int k_num = 88);



std::vector<std::vector<double>> changeCQT(std::vector<std::vector<std::complex<double>>> CQ);