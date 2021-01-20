echo 'Removing turtle_race container'
docker rm turtle_race

echo 'Removing turtle_race_build image'
docker rmi turtle_race_build

echo 'Removing all images with <none> tag'
docker rmi $(docker images -f 'dangling=true' -q)
