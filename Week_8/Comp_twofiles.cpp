#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <unordered_set>
#include <iomanip>

using namespace std;

unordered_set<string> tokenizeText(const string& text) {
    unordered_set<string> words;
    istringstream iss(text);
    string word;
    
    while (iss >> word) {
        // Remove punctuation and convert to lowercase
        for (char& c : word) {
            if (ispunct(c)) {
                c = ' ';
            } else {
                c = tolower(c);
            }
        }
        words.insert(word);
    }
    
    return words;
}

double calculateSimilarityIndex(const string& content1, const string& content2) {
    unordered_set<string> words1 = tokenizeText(content1);
    unordered_set<string> words2 = tokenizeText(content2);

    size_t commonWords = 0;
    for (const string& word : words1) {
        if (words2.count(word)) {
            commonWords++;
        }
    }

    size_t totalWords = words1.size() + words2.size();

    if (totalWords > 0) {
        return static_cast<double>(commonWords) / totalWords;
    } else {
        return 0.0;
    }
}

int main() {
    // Replace these filenames with your file paths
    string file1Path = "file1.txt";
    string file2Path = "file2.txt";

    ifstream file1(file1Path);
    ifstream file2(file2Path);

    if (file1 && file2) {
        stringstream content1Stream;
        content1Stream << file1.rdbuf();
        string content1 = content1Stream.str();

        stringstream content2Stream;
        content2Stream << file2.rdbuf();
        string content2 = content2Stream.str();

        double similarityIndex = calculateSimilarityIndex(content1, content2);

        cout << setprecision(2) << fixed;
        cout << "Similarity Index: " << similarityIndex << endl;
    } else {
        cerr << "One or both files not found." << endl;
    }

    return 0;
}
