file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/sshd_config',
  line   => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
}

service { 'ssh':
  ensure => running,
  enable => true,
  require => File_line['Turn off passwd auth', 'Declare identity file'],
}
