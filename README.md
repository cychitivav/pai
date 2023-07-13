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
Code and documentation for a UGV that can work and be teleoperated in a field.

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
	- [GitHub Codespace](#github-codespace)
- [:balloon:Usage](#balloonusage)
- [:key:License](#keylicense)
- [:pencil2:Authors](#pencil2authors)
- [:tada:Acknowledgments](#tadaacknowledgments)



<!-- ABOUT THE PROJECT -->
## :pushpin:About The Project

<div align="center">
	<a href="https://cad.onshape.com/documents/2c5667e2c198d5de4bff6632/w/6e55e179f397483a4657fa47/e/d5c2a6fd63cf397246fd908f?renderMode=0&uiState=64b078163855a86c0d9b8a6c">
		<img src="https://user-images.githubusercontent.com/30636259/235977670-f7890966-2141-477a-a577-54380ec47c93.png" alt="Logo" width="80%" style="min-width: 400px;" />
	</a>
</div>

Welcome to the PAI ROS 1 package repository! This package contains source code and documentation for a UGV that can work in a field. This project is part of the *PAI* subject at the Universidad Nacional de Colombia.

> __Note__: This package is being developed using ROS noetic 

<!-- BADGES
https://github.com/Ileriayo/markdown-badges -->
### Built With
* [![ROS](https://img.shields.io/badge/ros-%230A0FF9.svg?style=for-the-badge&logo=ros&logoColor=white)](ros.org)
* ![Raspberry Pi](https://img.shields.io/badge/-RaspberryPi-C51A4A?style=for-the-badge&logo=Raspberry-Pi)
* ![KiCAD](https://img.shields.io/badge/-KiCAD-4F9DB3?style=for-the-badge&logo=KiCad)


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

### GitHub Codespace
Codespaces add an easy way to start contributing to this project. Some extra step are needed to run the visualization in a remote machine. You need to create a GitHub Codespace:

1. To create a Codespace, click on the following button:
   
	[![Open in Visual Studio Code](https://img.shields.io/badge/-Open%20in%20Visual%20Studio%20Code-007ACC?style=for-the-badge&logo=visual-studio-code)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=600569804)
2. Choose the configuration that best suits you (A high performance configuration is recommended)
3. Wait for the Codespace to be created and set up (It will appear a terminal which is running some scripts)
4. Set a password for the root user
	```bash	
	passwd
	```

From your local machine, you will need to run the following command:

```bash	
gh cs ssh -- -XY
```

> __Note__: You need to have the [GitHub CLI](https://cli.github.com/manual/installation) installed in your local machine.

Then, select the Codespace that you want to connect to and enter the password that you set before.


<!-- USAGE EXAMPLES -->
## :balloon:Usage
In order to run the package, you will need to follow the next steps from the workspace directory (by default, `~\catkin_ws`):

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
<!-- ## :roller_coaster:Roadmap

- [ ] Feature 1
- [ ] Feature 2
    - [ ] Nested Feature

> __Note__: See the [open issues](https://github.com/cychitivav/pai/issues) for a full list of proposed features (and known issues). -->




<!-- CONTRIBUTING -->
<!-- ## :busts_in_silhouette:Contributing

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
 -->


<!-- LICENSE -->
## :key:License
Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.



<!-- CONTACT -->
## :pencil2:Authors
* [@cychitivav](https://github.com/cychitivav)
* [@jsduenass](https://github.com/jsduenass)
* [@juvallejom](https://github.com/juvallejom)
* [@Canborda](https://github.com/canborda)
* [@Camilo96A](https://github.com/camilo96a)
* [@jodiazro](https://github.com/jodiazro)


<!-- ACKNOWLEDGMENTS -->
## :tada:Acknowledgments

* Thanks to the [SIMA student group]() who help out supporting this project.


<div align="right">

[:arrow_double_up:back to top](#readme-top)
</div>




