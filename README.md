# My development environment in VIM
I decided to put my development environment into a vagrant VM provisioned by ansible since I use nvim and this will be easy
way to setup my development environment again

## Requirements
make an `envs` file with your required environment variables
symlink your code directory to ./code folder so it syncs to VM

This can all be re-configured via ansible config files directly too if needed.
