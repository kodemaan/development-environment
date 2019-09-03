# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.synced_folder "./code", "/code"
  config.vm.provision :ansible do |ansible|
    ansible.compatibility_mode = '2.0'
    ansible.playbook = "playbook.yml"
  end
end
