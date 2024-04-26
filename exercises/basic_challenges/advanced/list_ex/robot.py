'''
Robotics 

There is a robotics factory. The current project is assembly-line robots. 

Each robot has a processing time – it is the time in seconds the robot needs to process a product. When a robot is free, it should take a product for processing and log its name, product, and processing start time. 

Each robot processes a product coming from the assembly line. A product is coming from the line each second (so the first product should appear at [start time + 1 second]). If a product passes the line and there is not a free robot to take it, it should be queued at the end of the line again. 

The robots are standing in the line in the order of their appearance. 

Input 

On the first line, you will receive the robots' names and their processing times in the format "robotName-processTime;robotName-processTime;robotName-processTime..." 

On the second line, you will get the starting time in the format "hh:mm:ss" 

Next, until the "End" command, you will get a product on each line. 

Output  

Every time a robot takes a product, you should print: "{robotName} - {product} [hh:mm:ss]" 

Examples 

Input 

Output 

ROB-15;SS2-10;NX8000-3 

8:00:00 

detail 

glass 

wood 

apple 

End 

ROB - detail [08:00:01] 

SS2 - glass [08:00:02] 

NX8000 - wood [08:00:03] 

NX8000 - apple [08:00:06] 

ROB-8 

7:59:59 

detail 

glass 

wood 

sock 

End 

ROB - detail [08:00:00] 

ROB - wood [08:00:08] 

ROB - glass [08:00:16] 

ROB - sock [08:00:24] 



'''


def main():
    robots = input().split(";")
    robots = {robot.split("-")[0]: int(robot.split("-")[1])
              for robot in robots}
    try:
        start_time = input().split(":")
        start_time = [int(x) for x in start_time]
        start_time = start_time[0] * 3600 + start_time[1] * 60 + start_time[2]
    except ValueError:
        print("Invalid time format. Please enter time in the format 'hh:mm:ss'")
        return
    robots = {robot: [robots[robot], 0] for robot in robots}
    products = []
    while True:
        product = input()
        if product == "End":
            break
        products.append(product)
    while products:
        start_time += 1
        for robot in robots:
            if robots[robot][1] == 0 and products:
                product = products.pop(0)
                robots[robot][1] = robots[robot][0]
                print(f"{robot} - {product} [{start_time // 3600:02d}:{
                      start_time // 60 % 60:02d}:{start_time % 60:02d}]")
            if robots[robot][1] > 0:
                robots[robot][1] -= 1


if __name__ == '__main__':
    main()
