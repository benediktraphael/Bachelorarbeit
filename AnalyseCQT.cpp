#include "AnalyseCQT.hpp"

std::vector<AppearingNote> locate_Notes(std::vector<std::vector<double>> dB_CQ, double th_volume, int th_many, int th_few) {

	std::vector<AppearingNote> appearingNotes;
	AppearingNote x;
	int start_of_note = -1;
	int count = 0;
	int max = -1000;
	int max_midi = -1;

	for (size_t timeStrip = 0; timeStrip < dB_CQ.size(); timeStrip++) {

		for (size_t frequencyBin = 0; frequencyBin < dB_CQ[timeStrip].size(); frequencyBin++) {

			count += (th_volume < dB_CQ[timeStrip][frequencyBin]) ? 1 : 0;
			max_midi = (max < dB_CQ[timeStrip][frequencyBin]) ? frequencyBin : max_midi;
			max = (max < dB_CQ[timeStrip][frequencyBin]) ? dB_CQ[timeStrip][frequencyBin] : max;
		}

		if (start_of_note == -1 && count >= th_many) {
			start_of_note = timeStrip;
		}

		else if (start_of_note != -1 && count < th_few) {

			x.midi = max_midi;
			x.start = start_of_note;

			appearingNotes.push_back(x);
			start_of_note = -1;
		}

		max = -1000;
		count = 0;

	}
	//This is to pass the information of db_CQ.size()
	x.midi = -1;
	x.start = dB_CQ.size();

	appearingNotes.push_back(x);
	


	return appearingNotes;
}


std::vector<FinishedNotes> calculate_Note_Values(std::vector<AppearingNote> notes) {

	
	std::vector<FinishedNotes> result(notes.size()-1);
	FinishedNotes Note;

	//translate start-points into durations
	std::vector<int> note_duration(notes.size()-1);
	for (size_t n = 0; n < notes.size() - 1; n++) {
		note_duration[n] = notes[n + 1].start - notes[n].start;
	}
	

	double min = note_duration[0], avg = 0, max = 0;
	for (size_t n = 0; n < note_duration.size(); n++) {
		min = (min > note_duration[n]) ? note_duration[n] : min;
		max = (max < note_duration[n]) ? note_duration[n] : max;
		avg += note_duration[n];
	}
	avg /= note_duration.size();

	double avg_value = calculate_avg_val(min, avg, max);


	double value;
	for (size_t note = 0; note < note_duration.size(); note++) {
		//value is = 1/2 or 1/4 or 1/8 or 1/16
		value = std::pow(2, std::floor(std::log2((double)note_duration[note] / avg) + 0.5)) * avg_value;

		Note.midi = notes[note].midi + 21;
		Note.noteValue = value * 16;

		result[note] = Note;
	}


	return result;
}


double calculate_avg_val(double min, double avg, double max) {

	if (std::floor(std::log2(max / avg) + 0.5) == 3) {
		return (1.0 / 16.0);
	}
	if (std::floor(std::log2(avg / min) + 0.5) == 3) {
		return (1.0 / 2.0);
	}
	if (2 * std::floor(std::log2(max / avg) + 0.5) >
		std::floor(std::log2(max / min) + 0.5)) {
		return (1.0 / 8.0);
	}
	return (1.0 / 4.0);
}