# My development environment in Vagrant
I decided to put my development environment into a vagrant VM provisioned by ansible since I use nvim and this will be easy
way to setup my development environment again. This works particularly well for me because I use vim but the mapped volume allows anyone to use this to program.
List of software
* tmux
* docker
* nodejs
* yarn
* make
* git
* zsh (oh-my-zsh)
* vim-plug
* monokai (color scheme)
* fzf
* docker
* ag (silver searcher)

## Requirements

* make an `envs` file with your required environment variables, it should be in format `export VAR=test`
* symlink your code directory to ./code folder so it syncs to VM as /code root folder

This can all be re-configured via ansible config files directly too if needed.

## Install

To install this simply install https://www.vagrantup.com/ for your platform, and run vagrant up
