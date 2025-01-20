#include "Transformationen.hpp"
#include <iostream>
#include <cmath>
#include "calcSpektral.hpp"

constexpr double pi = 3.14159265358979323846;


std::vector<std::complex<double>> FT(std::vector<double> data) {
	std::cout << "Starte die Fourier Transformation...\n" << std::endl;

	const size_t numberDataPoints = data.size();

	std::vector<std::complex<double>> ft(numberDataPoints);


	for (int i = 0; i < numberDataPoints; i++) {

		for (int j = 0; j < numberDataPoints; j++) {
			const std::complex<double> _omega= std::exp(std::complex<double>(0, -2.0 * pi * i * j / numberDataPoints));//(std::cos(-2 * pi *  i * j / numberDataPoints), std::sin(-2 * pi * i * j / numberDataPoints));
			ft.at(i) += data.at(j) * _omega;
		}

		//ft.at(i) *= 1 / sqrt(numberDataPoints);
	}


	std::cout << "Fourier Transformation erfolgreich beendet!\n" << std::endl;
	return ft;
}


std::vector<std::complex<double>> FFT(std::vector<std::complex<double>> data) {


	if (data.size() == 1) {
		return data;
	}


	std::vector<std::complex<double>> gerade(data.size()/2);
	std::vector<std::complex<double>> ungerade(data.size() / 2);
	for (size_t i = 0; i < data.size() / 2; i++) {
		gerade.at(i) = data.at(2 * i);
		ungerade.at(i) = data.at(2 * i + 1);
	}

	std::vector<std::complex<double>> Agerade = FFT(gerade);
	std::vector<std::complex<double>> Aungerade = FFT(ungerade);

	std::vector<std::complex<double>> ergebnis(data.size());

	for (size_t i = 0; i < Agerade.size(); i++) {
		std::complex<double> _omega(std::cos(-2 * pi * i / ergebnis.size()), std::sin(-2 * pi * i / ergebnis.size()));

		ergebnis.at(i) = Agerade.at(i) + _omega * Aungerade.at(i);
		ergebnis.at(i + Agerade.size()) = Agerade.at(i) - _omega * Aungerade.at(i);
	}


	return ergebnis;
}


std::vector<std::complex<double>> PrepareFFT(std::vector<double> data)
{	
	//Wandle die reellen Datenpunkte in komplexe Datenpunkte
	std::vector<std::complex<double>> complexData(data.size());
	
	for (size_t i = 0; i < complexData.size(); i++) {
		complexData.at(i) = std::complex<double>(data.at(i), 0);
	}

	//Padde die Daten, damit diese eine 2-Potenz bilden.
	int potenz = 2;
	while (potenz < complexData.size()) {
		potenz <<= 1;//Shift-Operator (äquivalent zu *= 2)
	}

	complexData.resize(potenz, std::complex<double>(0, 0));

	return complexData;
}

/*
* Ein Vektor, der die einzelnen Zeitstreifen als Vektoren beinhaltet.
* Jeder ZeitstreifenVektor beinhaltet das Frequenzspektrum. 
*/
std::vector <std::vector<std::complex<double>>> STFT(std::vector<std::complex<double>> data, std::vector<double> window) {


	int mengeZeitstreifen = 2 * int(data.size() / window.size()) - 1;
	std::vector <std::vector<std::complex<double>>> Ergebnis(mengeZeitstreifen);


	//windowSize/2, da ich 50% Überlappung haben möchte.
	for (size_t k = 0; k < data.size()-window.size(); k += (window.size() / 2)) {

		//wir erstellen hier die einzelnen Zeitstreifen und führen die FFT auf diesen aus.
		std::vector<std::complex<double>> timeStrip(window.size());
		for (int i = 0; i < window.size(); i++) {
			timeStrip.at(i) = data.at(k + i) * window.at(i);
		}
		Ergebnis.at(k) = timeStrip;


	}

	return Ergebnis;
}


std::vector<std::vector<std::complex<double>>> CQT(std::vector<std::complex<double>> data, std::vector<std::vector<std::complex<double>>> spectralKernels, std::vector<int> startIndizes,  double f_0, int k_num) {

	std::vector<std::vector<std::complex<double>>> CQ;



	int Q = ceil(1.0 / (std::pow(2, (1.0 / 12.0)) - 1.0));
	int N_0 = Q * ceil(44100.0 / f_0);//Window of f_0

	int p = ceil(log2(N_0));
	int fft_len = std::pow(2, p);

	double f_max = f_0 * std::pow(2, (k_num - 1) / 12.0);
	int N_f_max = ceil(Q * 44100 / f_max);
	int hop_len = int(N_f_max / 2);

	
	for (int hop = 0; hop < data.size()-fft_len; hop += hop_len) {
		std::vector<std::complex<double>> data_time_strip(fft_len, 0);

		for (int m = 0; m < fft_len; m++) {
			data_time_strip.at(m) = data.at(hop + m);
		}

		std::vector<std::complex<double>> spectral_data_time_strip = FFT(data_time_strip);

		//create TimeStrip
		std::vector<std::complex<double>>timeStrip(k_num);

		for (int freqbin = 0; freqbin < k_num; freqbin++) {

			std::complex<double> sum = 0;

			for (int n = 0; n < spectralKernels[freqbin].size(); n++) {
				sum += spectral_data_time_strip[n + startIndizes[freqbin]] * spectralKernels[freqbin][n];
			}
			timeStrip.at(freqbin) = sum;
		}

		CQ.push_back(timeStrip);


		if (abs(timeStrip.at(48)) < 2000) {
			continue;
		}
	}

	return CQ;
}



std::vector<std::complex<double>> PrepareCQT(std::vector<double> data, double f_0, int k_num){

	


	int Q = ceil(1.0 / (std::pow(2, (1.0 / 12.0)) - 1.0));
	int N_0 = Q * ceil(44100.0 / f_0);//Window of f_0



	int p = ceil(log2(N_0));
	int fft_len = std::pow(2, p);

	//pad the data
	std::vector<std::complex<double>> complexData(data.size() + fft_len, 0);
	for (int i = 0; i < data.size(); i++) {
		complexData.at(i) = std::complex<double>(data.at(i), 0);
	}





	return complexData;
}


//Make the Values absolute

std::vector<std::vector<double>> changeCQT(std::vector<std::vector<std::complex<double>>> CQ) {


	std::vector<std::vector<double>> Changed_CQ(CQ.size());
	for (int i = 0; i < CQ.size(); i++) {
		std::vector<double> changed_timestrip(CQ.at(i).size());
		for (int j = 0; j < CQ.at(i).size(); j++) {
			changed_timestrip.at(j) = abs(CQ.at(i).at(j));
		}

		Changed_CQ.at(i) = changed_timestrip;
	}


	return Changed_CQ;
}