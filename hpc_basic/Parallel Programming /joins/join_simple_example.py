import time
from threading import Thread

# Define a function that represents the work done by the child thread
def child():
    print("Child Thread doing work...")  # Inform that the child thread has started working
    time.sleep(5)  # Simulate some work with a 5-second delay
    print("Child Thread done...")  # Inform that the child thread has completed its work

# Define a function that represents the parent thread's behavior
def parent():
    # Create a thread to execute the 'child' function
    # The 'args=()' is used to pass arguments, but here it's empty as 'child' takes no arguments
    t = Thread(target=child, args=())  
    
    t.start()  # Start the child thread
    print("Parent Thread is waiting...")  # Inform that the parent thread is waiting for the child

    t.join()  # Block the parent thread until the child thread completes
    print("Parent Thread is unblocked...")  # Inform that the parent thread has resumed execution

# Execute the parent function
parent()
