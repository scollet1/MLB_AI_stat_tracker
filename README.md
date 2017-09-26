# MMA Fight Predictor
rolls off the tongue, doesn't it?

I programmed this entirely on the computers at my school's lab. Due to the restrictions on user privileges, dependencies were near impossible to install. To make environment setup easier, I recommend using Docker.

In short, Docker is like a virtual machine that runs a simulated environment. This makes version management easier and allows us to run the same code with as little issues as possible.

You can get that [here](https://www.docker.com/).

After you've successfully installed Docker, you're going to need to start a docker container. I use default, so my commands are as follows.

If you do not have a machine ready to go:
```
docker-machine create default
```

I usually start by resetting my machine.
```
docker-machine restart default
```
Set the environment variables.
```
eval $(docker-machine env default)
```
Docker uses a thing called an "image" in order to construct the environment. I have made a custom image with all the dependencies I need for this project. You're welcome to modify it to suit your needs.

Here is the [image](https://hub.docker.com/r/scollet42/python-slim/).

Here is the command to pull it.

```
docker pull scollet42/python-slim
```
Finally we can start the environment and simulate some fights!
```
docker run -it --rm --name Sim -v ~/root:/root -p 3000:3000 scollet42/python-slim:latest bin/bash
```
If using scollet42/python-slim:latest" 
doesn't work, try the following:
```
docker images
```
This will give a list of all docker images. Look for something that says "IMAGE ID" and use that instead of "scollet42/python-slim:latest"

You should now see a bash terminal ready to go. The next step is git cloning this very repository!

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
### Enjoy!

## TODO - Flaskerizing the program to run from web!
Keep an eye on this
