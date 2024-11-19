import os
from os.path import isdir, join  # Import functions to work with file paths
from threading import Lock, Thread  # Import threading utilities

# Initialize a mutex (lock) for thread-safe operations
mutex = Lock()

# Shared list to store matching file paths
matches = []


# Define a recursive function to search for a file in a directory and its subdirectories
def file_search(root, filename):
    print("Searching in:", root)  # Print the directory currently being searched

    child_threads = []  # List to hold child threads for subdirectory searches

    # Iterate over all files and directories in the current directory
    for file in os.listdir(root):
        full_path = join(root, file)  # Get the full path of the file/directory

        # Check if the filename matches the search term
        if filename in file:
            mutex.acquire()  # Acquire the mutex to ensure thread-safe addition to the shared list
            matches.append(full_path)  # Add the matching file path to the shared list
            mutex.release()  # Release the mutex

        # If the current item is a directory, create a new thread to search within it
        if isdir(full_path):
            t = Thread(target=file_search, args=(full_path, filename))  # Recursive call in a new thread
            t.start()  # Start the child thread
            child_threads.append(t)  # Add the thread to the list of child threads

    # Wait for all child threads to finish
    for t in child_threads:
        t.join()


# Define the main function that initiates the search
def main():
    # Create a thread to start the file search from the specified root directory
    # Replace "/Users" and "README.md" with valid paths/filenames on your system
    t = Thread(target=file_search, args=("/Users", "README.md"))  # Example for macOS
    # For Windows, use a valid directory: Thread(target=file_search, args=("C:/tools", "README.md"))
    t.start()  # Start the search thread
    t.join()  # Wait for the main search thread to complete

    # Print all the matching file paths found during the search
    for m in matches:
        print("Matched:", m)


# Execute the main function when the script is run directly
if __name__ == "__main__":
    main()
