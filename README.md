# My development environment in VIM
I decided to put my development environment into a vagrant VM provisioned by ansible since I use nvim and this will be easy
way to setup my development environment again
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

## Requirements

* make an `envs` file with your required environment variables, it should be in format `export VAR=test`
* symlink your code directory to ./code folder so it syncs to VM as /code root folder

This can all be re-configured via ansible config files directly too if needed.

## Install

To install this simply install https://www.vagrantup.com/ for your platform, and run vagrant up
