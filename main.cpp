#include <iostream>
#include "FileManager.hpp"
#include "Transformationen.hpp"
#include <chrono> //Zeitmessung
#include "calcSpektral.hpp"
#include <tuple>


void test(std::vector<std::complex<double>> ft);
std::vector<double> s();

int main() {

	int Q = int(ceil(1.0 / (std::pow(2, (1.0 / 12.0)) - 1.0)));
	int N_0 = Q * ceil(44100.0 / 27.5);//Window of f_0#
	int N_f_max = N_0 * 1.0 / (std::pow(2, ((88.0 - 1.0) / 12.0)));

	double fk = 27.5 * std::pow(2, ((87.0) / 12.0));
	int N_k = Q * ceil(44100.0 / fk);//Window of f_0#
	/*
	std::vector<std::vector<std::complex<double>>>kernels = spectralKernels();
	for (int i = 0; i < kernels[1].size(); i++) {

	std::cout << kernels[1][i] << "\n";
	}
	*/

	std::vector<double> data = reader("signal_data");

	std::tuple<std::vector<std::vector<std::complex<double>>>, std::vector<int>> specResult = spectralKernels();
	std::vector<std::vector<std::complex<double>>> spectral_Kernels = std::get<0>(specResult);
	std::vector<int> startIndizes = std::get<1>(specResult);
	
	std::vector<std::complex<double>> complexData = PrepareCQT(data);

	std::vector<std::vector<std::complex<double>>> cq = CQT(complexData, spectral_Kernels, startIndizes);
	//std::vector<std::vector<double>> changed = changeCQT(cq);


	//std::vector<std::vector<std::complex<double>>>test = CQT(data);

	std::vector<std::vector<double>> changed = changeCQT(cq); 
	return 0;


	std::cout << "Hello World" << std::endl;
	
	std::vector<double> input = {
		1,2,3,4,5,6,7,8,8,7,6,5,4,3,2
	};

	//std::vector<double> data = reader("Tonleiter");

	//auto start = std::chrono::high_resolution_clock::now();

	//std::vector<std::complex<double>> ft = FFT(PrepareFFT(data));

	/*
	for (int i = 0; i < ft.size(); i++) {
		std::cout << ft.at(i) << "\n";
	}
	*/

	//auto end = std::chrono::high_resolution_clock::now();

	//auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);

	//std::cout << "Dauer: " << duration.count() << " ms" << std::endl;


	//std::vector<double> data = s();

	std::vector<std::complex<double>> ergebnis = FT(input);
	for (int i = 0; i < ergebnis.size(); i++) {
		std::cout << i << ": " << ergebnis.at(i) << "\n";
	}
	std::vector<std::complex<double>> ergebnis2 = FFT(PrepareFFT(input));
	for (int i = 0; i < ergebnis2.size(); i++) {
		std::cout << i << ": " << ergebnis2.at(i) << "\n";
	}



	return 0;
}


void test(std::vector<std::complex<double>> ft) {


	for (int i = 1; i < ft.size() / 2; i++) {
		if (ft.at(i).real() != ft.at(ft.size() - i).real() || ft.at(i).imag() != -1 * ft.at(ft.size() - i).imag()) {
			std::cout << i << "Error: " << ft.at(i) << ft.at(ft.size() - i) << std::endl;
			return;
		}
	}

}


std::vector<double> s() {
	std::vector<double> ergebnis(1000);
	for (int i = 0; i < ergebnis.size(); i++) {
		ergebnis.at(i) = sin(2 * 3.14 * 5.0 * i  / 1000);
	}

	return ergebnis;
}