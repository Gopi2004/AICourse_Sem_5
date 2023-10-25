#AP21110010167 - MEDISETTY GOPICHAND

def sort_words_in_sentence(sentence):
    # Split the sentence into words and sort them in dictionary order
    words = sentence.split()
    sorted_words = sorted(words, key=lambda x: x.lower())  # Sort case-insensitively
    return ' '.join(sorted_words)

def sort_sentences(input_file, output_file):
    with open(input_file, 'r') as infile:
        sentences = infile.read().splitlines()

        # Sort the sentences based on the sorted words within each sentence
        sorted_sentences = [sort_words_in_sentence(sentence) for sentence in sentences]

    with open(output_file, 'w') as outfile:
        # Write the sorted sentences to the output file
        outfile.write('\n'.join(sorted_sentences))

if __name__ == "__main__":
    input_file = "input2.txt"  # Replace with your input file name
    output_file = "output2.txt"  # Replace with your output file name

    sort_sentences(input_file, output_file)
    print("Sentences with sorted words written to", output_file)

