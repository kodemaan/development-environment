# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.synced_folder "./code", "/code"
  # I did this because for me VPN was causing issues with private network
  # It may work better without VPN on my home setup and i'll re-add
  config.vm.network "forwarded_port", guest: 9320, host: 9320
  config.vm.network "forwarded_port", guest: 8888, host: 8888
  config.vm.provision :ansible do |ansible|
    ansible.compatibility_mode = '2.0'
    ansible.playbook = "playbook.yml"
  end
end
