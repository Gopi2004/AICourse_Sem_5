#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cctype>

using namespace std;

int main() {
    string file_path = "input.txt"; // Replace with your file path
    ifstream file(file_path);

    if (!file.is_open()) {
        cerr << "Failed to open the file." << endl;
        return 1;
    }

    int character_count = 0;
    int number_count = 0;
    int word_count = 0;

    string line;
    while (getline(file, line)) {
        character_count += line.size();
        
        istringstream iss(line);
        string word;
        while (iss >> word) {
            word_count++;
            bool is_number = true;
            for (char c : word) {
                if (!isdigit(c)) {
                    is_number = false;
                    break;
                }
            }
            if (is_number) {
                number_count++;
            }
        }
    }

    file.close();

    cout << "Number of characters: " << character_count << endl;
    cout << "Number of numbers: " << number_count << endl;
    cout << "Number of words: " << word_count << endl;

    return 0;
}
