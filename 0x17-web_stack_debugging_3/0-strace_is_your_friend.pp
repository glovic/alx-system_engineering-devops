# Fixes bad `phpp` extensions to `php` in the WordPress file `wp-settings.php`

exec { 'fix-phpp-to-php-in-wp-settings':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => ['/usr/local/bin', '/usr/bin', '/bin', '/usr/sbin', '/sbin'],
  onlyif  => 'grep phpp /var/www/html/wp-settings.php',
}

