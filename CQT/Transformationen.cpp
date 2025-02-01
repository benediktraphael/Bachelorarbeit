#include "Transformationen.hpp"


constexpr double pi = 3.14159265358979323846;

std::vector<std::complex<double>> DFT(std::vector<double> data) {
	
	const size_t N = data.size();
	std::complex<double> FourierTerm;
	std::vector<std::complex<double>> ft(N);


	for (size_t k = 0; k < N; k++) {

		for (size_t n = 0; n < N; n++) {
			FourierTerm = std::exp(std::complex<double>(0, -2.0 * pi * k * n / N));
			ft.at(k) += data.at(n) *FourierTerm;
		}
		//normalisation
		//ft.at(k) *= 1 / sqrt(N);
	}

	return ft;
}

std::vector<std::complex<double>> FFT(std::vector<std::complex<double>> data) {


	if (data.size() == 1) {
		return data;
	}

	std::vector<std::complex<double>> gerade(data.size() / 2);
	std::vector<std::complex<double>> ungerade(data.size() / 2);
	for (size_t i = 0; i < data.size() / 2; i++) {
		gerade.at(i) = data.at(2 * i);
		ungerade.at(i) = data.at(2 * i + 1);
	}

	std::vector<std::complex<double>> ft_gerade = FFT(gerade);
	std::vector<std::complex<double>> ft_ungerade = FFT(ungerade);

	std::vector<std::complex<double>> ergebnis(data.size());

	for (size_t i = 0; i < ft_gerade.size(); i++) {
		//std::complex<double> _omega(std::cos(-2 * pi * i / ergebnis.size()), std::sin(-2 * pi * i / ergebnis.size()));
		std::complex<double> FourierTerm = std::exp(std::complex<double>(0, -2.0 * pi * i / ergebnis.size()));
		ergebnis.at(i) = ft_gerade.at(i) + FourierTerm * ft_ungerade.at(i);
		ergebnis.at(i + ft_gerade.size()) = ft_gerade.at(i) - FourierTerm * ft_ungerade.at(i);
	}

	return ergebnis;
}

std::vector <std::vector<std::complex<double>>> STFT(std::vector<std::complex<double>> data, std::vector<double> window) {


	int mengeZeitstreifen = 2 * int(data.size() / window.size()) - 1;
	std::vector <std::vector<std::complex<double>>> Ergebnis(mengeZeitstreifen);
	//wir erstellen hier die einzelnen Zeitstreifen und führen die FFT auf diesen aus.
	std::vector<std::complex<double>> timeStrip(window.size());

	//windowSize/2, da ich 50% Überlappung haben möchte.
	for (size_t k = 0; k < data.size()-window.size(); k += (window.size() / 2)) {

		for (size_t i = 0; i < window.size(); i++) {
			timeStrip.at(i) = data.at(k + i) * window.at(i);
		}
		Ergebnis.at(k) = timeStrip;

	}

	return Ergebnis;
}

std::vector<std::vector<std::complex<double>>> CQT(std::vector<std::complex<double>> data, std::vector<SpectralKernel> spectralKernels,  double f_0, int k_num) {

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

			for (int n = 0; n < spectralKernels[freqbin].specVals.size(); n++) {
				sum += spectral_data_time_strip[n + spectralKernels[freqbin].startPoint] * spectralKernels[freqbin].specVals[n];
			}

			timeStrip.at(freqbin) = sum;
		}

		CQ.push_back(timeStrip);
	}

	return CQ;
}


std::vector<std::complex<double>> prepare_FFT(std::vector<double> data)
{
	//Wandle die reellen Datenpunkte in komplexe Datenpunkte
	std::vector<std::complex<double>> complexData(data.size());

	for (size_t i = 0; i < complexData.size(); i++) {
		complexData.at(i) = std::complex<double>(data.at(i), 0);
	}

	//Padde die Daten, damit diese eine 2-Potenz bilden.
	int potenz = 2;
	while (potenz < complexData.size()) {
		potenz <<= 1;
	}

	complexData.resize(potenz, std::complex<double>(0, 0));

	return complexData;
}

std::vector<std::complex<double>> PrepareCQT(std::vector<double> data, double f_0, int k_num){


	int Q = ceil(1.0 / (std::pow(2, (1.0 / 12.0)) - 1.0));
	int N_0 = Q * ceil(44100.0 / f_0);//Window of f_0

	int p = ceil(log2(N_0));
	int fft_len = std::pow(2, p);

	std::vector<std::complex<double>> complexData(data.size() + fft_len, 0);
	for (int i = 0; i < data.size(); i++) {
		complexData.at(i) = std::complex<double>(data.at(i), 0);
	}

	return complexData;
}

