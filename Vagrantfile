require 'rbconfig'

def get_os
    @os ||= (
        host_os = RbConfig::CONFIG['host_os']
        case host_os
        when /mswin|msys|mingw|cygwin|bccwin|wince|emc/
            :"windows"
        when /darwin|mac os/
            :"macosx"
        when /linux/
            :"linux"
        when /solaris|bsd/
            :"unix"
        else
            raise Error::WebDriverError, "unknown os: #{host_os.inspect}"
        end
    )
end

os = get_os.to_s
  
puts "host platform : #{RUBY_PLATFORM} (operative system : #{os})"

machines = {
    # name     => enabled
    :nix => true
}

Vagrant.configure('2') do |config|

    if machines[:nix]
        config.vm.define :nix do |nix_config|

            nix_config.vm.box = 'precise32'
            nix_config.vm.box_url = 'http://files.vagrantup.com/precise32.box'
            
            nix_config.vm.network :forwarded_port, guest: 8000, host: 8001
            nix_config.vm.network :forwarded_port, guest: 80, host: 8008
            nix_config.vm.network :forwarded_port, guest: 443, host: 8443

            nix_config.ssh.forward_agent = true

            # nfs requires static IP
            #nix_config.vm.synced_folder '.', '/vagrant/', :nfs => (os == "linux")
            nix_config.vm.synced_folder '.', '/vagrant/'

            nix_config.vm.provider :virtualbox do |vbox|
                vbox.gui = false
                #vbox.customize ['modifyvm', :id, '--natdnshostresolver1', 'on']
                #vbox.customize ['modifyvm', :id, '--memory', '256']
            end

            nix_config.vm.provision :shell, :path => 'vagrantbootstrap.sh', :privileged => false
        end
    end
end
