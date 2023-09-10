# Use Puppet to Setup the web servers for the deployment of web_static

exec { 'apt_update':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin:/usr/local/bin:/bin/',
}

package { 'nginx':
  ensure => installed,
  require => Exec['apt_update'],
}

file { '/data':
  ensure  => 'directory',
}

file { '/data/web_static':
  ensure => 'directory',
}

file { '/data/web_static/releases':
  ensure => 'directory',
}

file { '/data/web_static/releases/test':
  ensure => 'directory',
}

file { '/data/web_static/shared':
  ensure => 'directory',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "<!DOCTYPE html>\n<html>\n  <head>\n  </head>\n  <body>\n    <p>Nginx server test</p>\n  </body>\n</html>",
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
}

exec { 'chown_data':
  command => 'chown -R ubuntu:ubuntu /data/',
  path    => '/usr/bin:/usr/local/bin:/bin/',
}

file { '/var/www':
  ensure => 'directory',
}

file { '/var/www/html':
  ensure => 'directory',
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "<!DOCTYPE html>\n<html>\n  <head>\n  </head>\n  <body>\n    <p>Nginx server test</p>\n  </body>\n</html>",
}

file { '/etc/nginx/sites-enabled/default':
  ensure  => 'file',
  content => file('/path/to/your/nginx_config_file.conf'), # Replace with the actual path to your Nginx configuration file
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['/etc/nginx/sites-enabled/default'],
}
