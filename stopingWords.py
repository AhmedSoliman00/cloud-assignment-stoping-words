import re
from collections import Counter
import nltk
from nltk.corpus import stopwords

# Download NLTK stop words
nltk.download('stopwords')

# Function to read the contents of a file
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Function to remove stop words from text
def remove_stop_words(text):
    stop_words = set(stopwords.words('english'))
    words = re.findall(r'\b\w+\b', text.lower())
    return ' '.join(word for word in words if word not in stop_words)

# Function to count the frequency of each word
def count_word_frequency(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

# Main function
def main():
    file_path = "paragraphs.txt"
    # Read the contents of the file
    text = read_file(file_path)
    # Remove stop words
    text_without_stop_words = remove_stop_words(text)
    # Count word frequency
    word_freq_count = count_word_frequency(text_without_stop_words)
    # Display word frequency count
    print("Word Frequency Count:")
    for word, count in word_freq_count.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
