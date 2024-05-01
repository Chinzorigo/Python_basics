'''
Robotics
There is a robotics factory. The current project is assembly-line robots.
Each robot has a processing time – it is the time in seconds the robot needs to process a product. When a robot is free, it should take a product for processing and log its name, product, and processing start time.
Each robot processes a product coming from the assembly line. A product is coming from the line each second (so the first product should appear at [start time + 1 second]). If a product passes the line and there is not a free robot to take it, it should be queued at the end of the line again.
The robots are standing in the line in the order of their appearance.
Input
•	On the first line, you will receive the robots' names and their processing times in the format "robotName-processTime;robotName-processTime;robotName-processTime..."
•	On the second line, you will get the starting time in the format "hh:mm:ss"
•	Next, until the "End" command, you will get a product on each line.
Output 
•	Every time a robot takes a product, you should print: "{robotName} - {product} [hh:mm:ss]"
Examples
input

ROB-15;SS2-10;NX8000-3
8:00:00
detail
glass
wood
apple
End

output
ROB - detail [08:00:00]
ROB - wood [08:00:08]
ROB - glass [08:00:16]
ROB - sock [08:00:24]


'''

from collections import deque
from datetime import datetime, timedelta

robots = input().split(";")
robots = {robot.split("-")[0]: int(robot.split("-")[1]) for robot in robots}
robots = {k: [v, None] for k, v in robots.items()}
robots = deque(robots.items())
time = datetime.strptime(input(), "%H:%M:%S")
products = deque()

while True:
    product = input()
    if product == "End":
        break
    products.append(product)

while products:
    time += timedelta(seconds=1)
    current_product = products.popleft()
    for robot in robots:
        if robot[1][1] is None and robot[1][0] > 0:
            robot[1][1] = time
            robot[1][0] -= 1
            print(
                f"{robot[0]} - {current_product} [{time.strftime('%H:%M:%S')}]")
            break
    else:
        products.append(current_product)
    for robot in robots:
        if robot[1][1] is not None:
            robot[1][0] -= 1
            if robot[1][0] == 0:
                robot[1][1] = None

# Explanation:
# We start by creating a dictionary of robots with their names as keys and their processing times as values.
# We set the processing start time of each robot to None. We create a queue of robots. We get the starting time and convert
# it to a datetime object. We create a queue of products. We iterate over the products and simulate the processing of each product.
# We iterate over the robots and check if a robot is free to take a product. If a robot is free, we log the robot's name, the product,
# and the processing start time. If a robot is not free, we add the product back to the queue of products. We then iterate over the robots and simulate the processing of each product. If a robot has finished processing a product, we set its processing start time to None.
# In the example, we have three robots: ROB, SS2, and NX8000. The processing times of the robots are 15, 10, and 3 seconds, respectively. The starting time is 8:00:00. We have four products: detail, glass, wood, and apple. The products are processed by the robots in the order they appear. The first product is processed by the ROB robot at 8:00:00. The second product is processed by the ROB robot at 8:00:08. The third product is processed by the ROB robot at 8:00:16. The fourth product is processed by the ROB robot at 8:00:24
