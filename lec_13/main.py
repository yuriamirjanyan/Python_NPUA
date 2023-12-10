import os
import time
import threading
import multiprocessing

# funkciayi katarman jamanaky chapox dekorator
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        return result, execution_time
    return wrapper

# randok naxadasutyunneric txt file stexcox funkcia
def generate_large_text_file(file_path, num_sentences):
    # A list of words to generate random sentences
    words = ["apple", "banana", "cherry", "dog", "elephant", "fox", "grape", "hat", "iguana", "jazz"]
    sentences = [" ".join([words[i % len(words)] for i in range(10)]) for _ in range(num_sentences)]
    
    with open(file_path, 'w') as file:
        file.write(" ".join(sentences))

# Bareri qanaky hashvox funkcia
@timing_decorator
def count_words(filename):
    word_freq = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

# Function to count words using multithreading
@timing_decorator
def count_words_multithread(filename, num_threads):
    word_freq = {}

    # Function to process a chunk of lines and update local word frequency
    def process_chunk(chunk):
        local_word_freq = {}
        for line in chunk:
            words = line.split()
            for word in words:
                local_word_freq[word] = local_word_freq.get(word, 0) + 1
        return local_word_freq

    with open(filename, 'r') as file:
        lines = file.readlines()

    min_chunk_size = max(1, len(lines) // num_threads)
    chunks = [lines[i:i + min_chunk_size] for i in range(0, len(lines), min_chunk_size)]

    threads = []
    # Create threads to process each chunk of lines concurrently
    for chunk in chunks:
        thread = threading.Thread(target=lambda: word_freq.update(process_chunk(chunk)))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return word_freq

# Function to process a chunk of lines and update word frequency in a shared dictionary
def process_chunk(chunk, result_dict):
    local_word_freq = {}
    for line in chunk:
        words = line.split()
        for word in words:
            local_word_freq[word] = local_word_freq.get(word, 0) + 1
    for key, value in local_word_freq.items():
        result_dict[key] = result_dict.get(key, 0) + value

# Function to count words using multiprocessing
@timing_decorator
def count_words_multiprocess(filename, num_processes):
    word_freq = multiprocessing.Manager().dict()

    with open(filename, 'r') as file:
        lines = file.readlines()

    min_chunk_size = max(1, len(lines) // num_processes)
    chunks = [lines[i:i + min_chunk_size] for i in range(0, len(lines), min_chunk_size)]

    processes = []
    # Create processes to process each chunk of lines concurrently using multiprocessing
    for chunk in chunks:
        process = multiprocessing.Process(target=process_chunk, args=(chunk, word_freq))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    return dict(word_freq)

if __name__ == "__main__":
    file_sizes = [10**5, 10**6, 10**7]  # Adjust file sizes based on your system's capacity
    num_threads = 8
    num_processes = 8

    for size in file_sizes:
        file_path = f"large_file_{size}.txt"
        generate_large_text_file(file_path, size)

        # Sequential
        _, seq_time = count_words(file_path)

        # Multithreading
        _, mt_time = count_words_multithread(file_path, num_threads)

        # Multiprocessing
        _, mp_time = count_words_multiprocess(file_path, num_processes)

        print(f"File Size: {size} words")
        print(f"Sequential Execution Time: {seq_time:.4f} seconds")
        print(f"Multithreading Execution Time: {mt_time:.4f} seconds")
        print(f"Multiprocessing Execution Time: {mp_time:.4f} seconds")

        speedup_mt = seq_time / mt_time
        speedup_mp = seq_time / mp_time

        print(f"Multithreading Speedup: {speedup_mt:.2f}x")
        print(f"Multiprocessing Speedup: {speedup_mp:.2f}x")
        