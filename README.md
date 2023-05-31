<!--
MARKDOWN IMAGES & BADGES
* https://www.markdownguide.org/basic-syntax/#reference-style-links
* https://github.com/Ileriayo/markdown-badges

EMOJIS
* https://gist.github.com/rxaviers/7360908
  
Find and replace the following text with the name of the project:
	pai
-->

<div align="center" id="readme-top">

<img src="https://user-images.githubusercontent.com/30636259/235979806-03ed419c-5748-45eb-b5bb-1ab401ddd267.png" alt="Logo" width="120"/>

<!-- omit in toc -->
# PAI's project
Code and documentation for a UGV that can work and be teleoperated in a cultivate.

[**Explore the docs »**](https://cychitivav.github.io/pai)

[View Demo](https://github.com/cychitivav/pai) · [Report Bug](https://github.com/cychitivav/pai/issues) · [Request Feature](https://github.com/cychitivav/pai/issues)

[![Contributors](https://img.shields.io/github/contributors/cychitivav/pai.svg?style=for-the-badge)](https://github.com/cychitivav/pai/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/cychitivav/pai.svg?style=for-the-badge)](https://github.com/cychitivav/pai/network/members)
[![Stargazers](https://img.shields.io/github/stars/cychitivav/pai.svg?style=for-the-badge)](https://github.com/cychitivav/pai/stargazers)
[![Issues](https://img.shields.io/github/issues/cychitivav/pai.svg?style=for-the-badge)](https://github.com/cychitivav/pai/issues)
[![MIT License](https://img.shields.io/github/license/cychitivav/pai.svg?style=for-the-badge)](https://github.com/cychitivav/pai/blob/main/LICENSE)


</div>


<!-- TABLE OF CONTENTS -->
<!-- omit in toc -->
## :pencil:Table of contents
- [:pushpin:About The Project](#pushpinabout-the-project)
	- [Built With](#built-with)
- [:checkered\_flag:Getting Started](#checkered_flaggetting-started)
	- [Prerequisites](#prerequisites)
	- [Installation](#installation)
- [:balloon:Usage](#balloonusage)
- [:roller\_coaster:Roadmap](#roller_coasterroadmap)
- [:busts\_in\_silhouette:Contributing](#busts_in_silhouettecontributing)
- [:key:License](#keylicense)
- [:pencil2:Authors](#pencil2authors)
- [:tada:Acknowledgments](#tadaacknowledgments)



<!-- ABOUT THE PROJECT -->
## :pushpin:About The Project

<div align="center">
	<img src="https://user-images.githubusercontent.com/30636259/235977670-f7890966-2141-477a-a577-54380ec47c93.png" alt="Logo" width="80%" style="min-width: 400px;" />
</div>

Welcome to the <package_name> ROS 1 package repository! This package contains source code and documentation for a UGV that can work in a field. This project is part of the *PAI* subject at the Universidad Nacional de Colombia.

> __Note__: This package is being developed using ROS noetic 

<!-- BADGES
https://github.com/Ileriayo/markdown-badges -->
### Built With
* [![ROS](https://img.shields.io/badge/ros-%230A0FF9.svg?style=for-the-badge&logo=ros&logoColor=white)](ros.org)



<!-- GETTING STARTED -->
## :checkered_flag:Getting Started

This is an example of how you may give instructions on setting up your project locally.
	To get a local copy up and running follow these simple example steps.

### Prerequisites
In order to avoid installing ROS on your local machine, we will be using a docker image to run ROS. So, you will just need to install [Docker](https://docs.docker.com/get-docker/) in your local machine.

### Installation

1. Clone the repo
	```bash
	git clone https://github.com/cychitivav/pai.git
	```
2. Build the docker image
	```bash
	docker build -t pai:latest .
	```
3. Run the docker image
	```bash
	docker run -it \
     		   --rm \
			   -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
               -v $PWD:/root/catkin_ws/src/pai \
			   --name pai \
			   pai:latest
	```
	> __Note__: If you have troubles with the display, try to run the following command before running the docker image:
	> ```bash
	> xhost +local:root
	> ```


<!-- USAGE EXAMPLES -->
## :balloon:Usage
In order to run the package, you will need to follow the next steps from the workspace directory (`catkin_ws`):

1. Compile packages
```bash
catkin build
```
1. Source the workspace
```bash
source devel/setup.bash
```
1. Launch the package
```bash
roslaunch pai view_robot.launch
```



<!-- ROADMAP -->
## :roller_coaster:Roadmap

- [ ] Feature 1
- [ ] Feature 2
    - [ ] Nested Feature

> __Note__: See the [open issues](https://github.com/cychitivav/pai/issues) for a full list of proposed features (and known issues).




<!-- CONTRIBUTING -->
## :busts_in_silhouette:Contributing

If you have a suggestion that would make this better, please create a pull request.

1. Create your Branch (`git checkout -b <type>/<name>`)
2. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
3. Push to the Branch (`git push origin <type>/<name>`)
4. Open a Pull Request (in the `git push` response, it appears a link to open a PR) 

The available contribution types are:
* `docs`
* `feat`
* `dev`
* `fix`

Don't forget to give the project a star! Thanks again!



<!-- LICENSE -->
## :key:License
Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.



<!-- CONTACT -->
## :pencil2:Authors
* [@cychitivav](https://github.com/cychitivav)
* [@jsduenass](https://github.com/jsduenass)
* [@juvallejom](https://github.com/juvallejom)



<!-- ACKNOWLEDGMENTS -->
## :tada:Acknowledgments

* []()


<div align="right">

[:arrow_double_up:back to top](#readme-top)
</div>




