# BigDataCourseExercises
This repository will contain all the exercises related to the course Big Data at SDU

# Useful commands:
See running containers and images
```console
$  docker ps
$  docker image ls -a
```

Stop all running containers or perform a full cleanup. 
```console
$  docker kill $(docker ps -q)
$  docker-compose down
$  docker system prune --all
```

Note that containers have been run with the "rm" argument which removes the container after it is terminated.