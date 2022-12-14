# Docker exercise, UE 2022
This Github repository was prepared to pass an exercise about docker containers. Here you can find Flask-based web application that generates quadratic formula plot based on provided parameters: a, b, c and ranges of the plot: xlim and ylim of matplotplib.pyplot plot object.

# Instructions
1. Clone this repository onto your computer's disk.
2. Start Docker Desktop and wait until Docker Engine will be running.
3. Open Powershell and get into cloned repository folder on your computer using 'cd' command.
4. Generate docker image by using following command:
```
docker build -t quadratic_app:v1.0 .
```
5. After image was generated, run it with command:
```
docker run --rm -it -p 5000:5000 quadratic_app:v1.0
```
6. Open your web browser and enter http://localhost:5000/ to see the app running.
7. To generate plot with provided parameters, add 'plot' after / mark, then ? and list all parameters with values separated with & just like in the example:
http://localhost:5000/plot?a=-2&b=3&c=5&xmin=-10&xmax=10&ymin=-10&ymax=10
8. After finish of the work with the application, clean up docker images with command that will remove generated image:
```
docker image rm quadratic_app:v1.0
```
