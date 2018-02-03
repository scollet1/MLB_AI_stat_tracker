# MMA Fight Predictor
rolls off the tongue, doesn't it?

MMA Fight Predictor is my implementation of a neural network classifier with data from the Sportsradar API. The algorithm analyzes fighter staistics and runs simulated fights in order to classify who is a winner in any fight. The data is pulled from real-world sources via XML get requests.

I programmed this entirely on the computers at my school's lab. Due to the restrictions on user privileges, dependencies were near impossible to install. To make environment setup easier, I recommend using Docker.

In short, Docker is like a virtual machine that runs a simulated environment. This makes version management easier and allows us to run the same code with as little issues as possible.

You can get that [here](https://www.docker.com/).

After you've successfully installed Docker, you're going to need to start a docker container. I use default, so my commands are as follows.

If you do not have a machine ready to go:
```
docker-machine create default
```
Run to start the machine
```
docker-machine start default
```
Set the environment variables.
```
eval $(docker-machine env default)
```

Here is the [image](https://hub.docker.com/r/scollet42/python-slim/) I used for this project.

Here is the command to pull it.
Finally we can start the environment and simulate some fights!

```
docker run -it --rm --name Sim -v ~/root:/root scollet42/python-slim:latest bin/bash
```

```
git clone https://github.com/scollet1/MMA_Fight_Predictor.git Sim
cd Sim
cd py
```
Now you're ready to start predicting!

The program is not finished as of late, but it accepts two arguments.
```
python run.py --train
```
and for predictions...
```
python run.py --predict "Fighter Name" "Fighter Name"
```
You should see a result like this

![alt text](https://github.com/scollet1/scollet1.github.io/blob/master/images/Screen%20Shot%202017-09-26%20at%208.31.25%20PM.png)

### Enjoy!


## TODO - Flaskerizing the program to run from web!
