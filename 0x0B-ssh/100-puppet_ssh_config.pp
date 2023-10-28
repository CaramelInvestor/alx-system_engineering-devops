#!/usr/bin/pup
#Using puppet to refuse to authenticate using a password

file_line { 'Remove authentication':
  path     => '/etc/ssh/ssh_config',
  line     => '    PasswordAuthentication no',
  replace  => true,
}

file_line { 'Indicating the IdentityFile':
  path     => '/etc/ssh/ssh_config',
  line     => '    IdentityFile ~/.ssh/school',
  replace  => true,
}
