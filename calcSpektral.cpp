#include "calcSpektral.hpp"
#include "createWindow.hpp"
#include <cmath>
#include <iostream>
#include <tuple>


constexpr double pi = 3.14159265358979323846;


/*
* @brief Calculates the spectral kernels
* 
* This function only needs to run once, to calculate the spectral kernels. 
* 
* @param f_0 The lowest frequency-bin
* @param k_num The Number of analised/calculated frequency-bins
* 
* @return all spectral kernels (already sparsed?)
*/

std::tuple<std::vector<std::vector<std::complex<double>>>, std::vector<int>> spectralKernels(double f_0, int k_num) {

	int Q = ceil(1.0 / (std::pow(2, (1.0 / 12.0)) - 1.0));
	int N_0 = Q * ceil(44100.0 / f_0);//Window of f_0

	int p = ceil(log2(N_0));
	int fft_len = std::pow(2, p);


	std::vector<std::vector<std::complex<double>>> spectralKernels(k_num);
	std::vector<int> startIndizes(k_num);
	

	for (int k = 0; k < k_num; k++) {
		double f_k = 27.5 * std::pow(2, (k - 1) / 12.0);
		int N_k = ceil(Q * 44100.0 / f_k);

		std::vector<double> hamming = Hamming(N_k);

		std::vector<std::complex<double>> temporalKernel(fft_len, 0);
		

		for (int n = 0; n < N_k; n++) {
			temporalKernel.at(n) = ((1.0 / N_k) * (hamming.at(n) * std::exp(std::complex<double>(0, -2.0 * pi * n * Q / N_k))));//(1.0 / N_k)*
		}
		std::vector<std::complex<double>> spectralKernel = FFTcq(temporalKernel);

		for (int t = 0; t < spectralKernel.size(); t++) {
			if (abs(spectralKernel.at(t)) < 0.0054) {
				spectralKernel.at(t) = 0;
			}
		}
		std::tuple<int, std::vector<std::complex<double>>> cliped_spectral_kernel = clipSpectralKernel(spectralKernel);

		spectralKernels.at(k) = std::get<1>(cliped_spectral_kernel);
		startIndizes.at(k) = std::get<0>(cliped_spectral_kernel);
	}

	return { spectralKernels, startIndizes };

}



std::tuple<int, std::vector<std::complex<double>>> clipSpectralKernel(std::vector<std::complex<double>> spectralKernel) {

	
	int start = 0;
	while (spectralKernel.at(start) == std::complex<double>(0, 0)) {
		start++;

	}

	int truestart = start;
	std::vector<std::complex<double>> cliped_spectralKernel;
	while (spectralKernel.at(start) != std::complex<double>(0, 0)) {
		cliped_spectralKernel.push_back(spectralKernel.at(start++));
	}


	return { truestart, cliped_spectralKernel };

}




std::vector<std::complex<double>> FFTcq(std::vector<std::complex<double>> data) {


	if (data.size() == 1) {
		return data;
	}


	std::vector<std::complex<double>> gerade(data.size() / 2);
	std::vector<std::complex<double>> ungerade(data.size() / 2);
	for (size_t i = 0; i < data.size() / 2; i++) {
		gerade.at(i) = data.at(2 * i);
		ungerade.at(i) = data.at(2 * i + 1);
	}

	std::vector<std::complex<double>> Agerade = FFTcq(gerade);
	std::vector<std::complex<double>> Aungerade = FFTcq(ungerade);

	std::vector<std::complex<double>> ergebnis(data.size());

	for (size_t i = 0; i < Agerade.size(); i++) {
		std::complex<double> _omega(std::cos(2 * pi * i / ergebnis.size()), std::sin(2 * pi * i / ergebnis.size()));

		ergebnis.at(i) = Agerade.at(i) + _omega * Aungerade.at(i);
		ergebnis.at(i + Agerade.size()) = Agerade.at(i) - _omega * Aungerade.at(i);
	}


	return ergebnis;
}
