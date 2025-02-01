#pragma once
#include <vector>
#include <cmath>

/*
* start = timeStrip, in which the note starts
* midi = the Midinumber
*/

struct AppearingNote {
	int start;
	int midi;
};


struct FinishedNotes {

	int noteValue;
	int midi;

};


std::vector<AppearingNote> locate_Notes(std::vector<std::vector<double>> dB_CQ, double th_volume = -40.0, int th_many = 35, int th_few = 22);

std::vector<FinishedNotes> calculate_Note_Values(std::vector<AppearingNote> notes);


double calculate_avg_val(double min, double avg, double max);