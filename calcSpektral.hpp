#include <vector>
#include <ccomplex>


std::tuple<std::vector<std::vector<std::complex<double>>>, std::vector<int>> spectralKernels(double f_min= 27.50, int k_num=88);
std::vector<std::complex<double>> FFTcq(std::vector<std::complex<double>> data);
std::tuple<int, std::vector<std::complex<double>>> clipSpectralKernel(std::vector<std::complex<double>> spectralKernel);