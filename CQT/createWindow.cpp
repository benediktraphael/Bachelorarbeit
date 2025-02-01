#include "createWindow.hpp"

constexpr double pi = 3.14159265358979323846;

std::vector<double> Rectangular(int size){

	std::vector<double> result(size, 1);
	return result;
}

std::vector<double> Hann(int size){

	std::vector<double> result(size);
	for (int i = 0; i < size; i++) {
		result.at(i) = 0.5 * (1 - cos(2.0 * pi * i / (size - 1)));
	}

	return result;
}

std::vector<double> Hamming(int size){
	std::vector<double> result(size);
	for (int i = 0; i < size; i++) {

		result.at(i) = 0.54 - 0.46 * (cos(2 * pi * i / (size - 1)));
	}

	return result;
}

//wird vermutlich noch zweiten Param brauchen
std::vector<double> Gaussian(int size){
	double sigma = size / 6.0;
	std::vector<double> result(size);
	for (int i = 0; i < size; i++) {
		result.at(i) = exp(-0.5 * pow((i - (size - 1) / 2.0) / sigma, 2));
	}

	return result;
}

std::vector<double> Blackman(int size){
	std::vector<double> result(size);
	for (int i = 0; i < size; i++) {
		result.at(i) = 0.42 - 0.5 * cos(2.0 * pi * i / (size - 1)) + 0.08 * cos(4.0 * pi * i / (size - 1));
	}

	return result;
}

std::vector<double> Exponential(int size){
	std::vector<double> result(size);
	for (int i = 0; i < size; i++) {
		double a = 1.0;
		result.at(i) = exp(-a * fabs(i - (size - 1) / 2.0));
	}

	return result;
}

std::vector<double> Triangular(int size){
	std::vector<double> result(size);
	for (int i = 0; i < size; i++) {
		result.at(i) = 1.0 - fabs(2.0 * (i / double(size - 1)) - 1.0);
	}

	return result;
}
//noch schauen..
std::vector<double> Tukey(int size){
	double alpha = 0.5;
	std::vector<double> result(size);
	for (int i = 0; i < size; i++) {
		result.at(i) = 0;
	}

	return result;
}