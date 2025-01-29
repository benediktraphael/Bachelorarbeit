#include "changeCQ.hpp"


/*
* This function computes the real values of each CQ-Element.
* It also finds the refValue, so the Dezibel-Variant can be calculated.
*/
GuterName CQ_to_real_values(std::vector<std::vector<std::complex<double>>> CQ) {

	double refValue = 0;

	std::vector<std::vector<double>> newCQ(CQ.size());
	std::vector<double> newTimestrip(CQ.at(0).size());

	for (size_t timeStrip = 0; timeStrip < CQ.size(); timeStrip++) {

		for (size_t frequenzyBin = 0; frequenzyBin < newTimestrip.size(); frequenzyBin++) {

			newTimestrip[frequenzyBin] = abs(CQ[timeStrip][frequenzyBin]);
			refValue = (newTimestrip[frequenzyBin] > refValue) ? newTimestrip[frequenzyBin] : refValue;
		}

		newCQ[timeStrip] = newTimestrip;
	}

	GuterName result;
	result.cq = newCQ;
	result.refValue = refValue;

	return result;
}


std::vector<std::vector<double>> CQ_to_dB(GuterName gN) {


	std::vector<std::vector<double>> dB_CQ(gN.cq.size());
	std::vector<double> dB_TimeStrip(gN.cq[0].size());

	for (size_t timeStrip = 0; timeStrip < gN.cq.size(); timeStrip++) {

		for (size_t frequenzyBin = 0; frequenzyBin < gN.cq[timeStrip].size(); frequenzyBin++) {

			dB_TimeStrip[frequenzyBin] = 20 * std::log10((double)gN.cq[timeStrip][frequenzyBin] / gN.refValue);
			
		}

		dB_CQ[timeStrip] = dB_TimeStrip;
	}


	return dB_CQ;
}