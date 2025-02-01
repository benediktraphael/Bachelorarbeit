#include <iostream>
#include "FileManager.hpp"
#include "Transformationen.hpp"
#include "calcSpektral.hpp"
#include "AnalyseCQT.hpp"
#include "changeCQ.hpp"

int main() {

	std::string filename;
	std::cout << "Wie heißt das zu verarbeitende file? ";
	std::getline(std::cin, filename);
	std::cout << "Reader" << std::endl;
	std::vector<double> samples = reader(filename);
	std::cout << "spec" << std::endl;
	std::vector<SpectralKernel> spectralKernels = calculate_spectralKernels();
	std::cout << "CQT" << std::endl;
	std::vector<std::vector<std::complex<double>>> cq = CQT(PrepareCQT(samples), spectralKernels);
	std::cout << "dB" << std::endl;
	std::vector<std::vector<double>> dB_cq = CQ_to_dB(CQ_to_real_values(cq));
	std::cout << "notes" << std::endl;
	std::vector<AppearingNote> notes = locate_Notes(dB_cq);
	std::cout << "finished notes" << std::endl;
	std::vector<FinishedNotes> finished_notes = calculate_Note_Values(notes);
	std::cout << "write" << std::endl;
	writer(finished_notes, "test");
	return 0;
}