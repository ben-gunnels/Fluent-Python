import random
import time
import threading
import logging
from collections import namedtuple
from queue import PriorityQueue

# Configure logging
logging.basicConfig(filename="thread_safe_servers_logging.txt", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

thread_stop_flag = False

# Holds the priority queue to service customers
customer_q = PriorityQueue(maxsize=4)

# Used to generate unique priority values for each customer
all_priorities = set(range(0, 101))
seen_priorities = set()

# Define the customer data type
Customer = namedtuple("Customer", ("priority", "ip", "service_time"))

# Standard prefix for customers
ip_prefix = "192.168."

def hub():
    global thread_stop_flag
    try:
        while True:
            try:
                pri = assign_priority()
                ip = ip_prefix + str(random.randrange(1, 255)) + "." + str(random.randrange(1, 255))
                service_time = random.randint(1, 7)  # Generate a random time between 1 and 7 seconds
                logging.info(f"Hub adding {ip} with priority: {pri} and service time: {service_time}")
                customer_q.put(Customer(pri, ip, service_time))
            except ValueError as err:
                logging.error("Cannot create a valid customer: %s", err)
            logging.info(f"# Customers in queue: {customer_q.qsize()}")
            time.sleep(1)  # Wait for more traffic to come
    except KeyboardInterrupt:
        thread_stop_flag = True
        logging.warning("\nCtrl + C detected. Exiting gracefully.")

def assign_priority():
    available = list(all_priorities - seen_priorities)
    if available:
        pri = random.choice(available)
        seen_priorities.add(pri)
        return pri
    else:
        raise ValueError("No valid priorities available.")

def server(name: int):
    global thread_stop_flag
    while not thread_stop_flag:
        if customer_q.qsize():
            pri, ip, service_time = customer_q.get()
            logging.info(f"Server {name} servicing customer: {ip} with priority: {pri} for: {service_time} seconds.")
            time.sleep(service_time)
            logging.info(f"Server {name} finished servicing customer: {ip} with priority: {pri}. Ready for next task.")

def main():
    # Create threads for the two servers
    s1 = threading.Thread(target=server, args=[1], daemon=True)
    s2 = threading.Thread(target=server, args=[2], daemon=True)

    # Begin the background threads
    s1.start()
    s2.start()
    
    # Run the main loop
    hub()

    # Join the background threads
    s1.join()
    s2.join()

    logging.info("Servers shut down successfully.")



if __name__ == "__main__":
    main()