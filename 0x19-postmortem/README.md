# Postmortem

Upon the release of ALX's System Engineering & DevOps project 0x19 at approximately 06:00 West African Time (WAT) in Nigeria, an outage occurred on an isolated Ubuntu 14.04 container running an Apache web server. GET requests to the server resulted in 500 Internal Server Errors instead of the expected HTML file for a simple Holberton WordPress site.

## Debugging Process

Bug debugger Bamidele (Lexxyla) encountered the issue upon starting the project at approximately 19:20 PST. Here is the step-by-step process used to identify and resolve the issue:

1. **Checked running processes:**
    - Used `ps aux` to list running processes. Two `apache2` processes (`root` and `www-data`) were running as expected.

2. **Checked the Apache configuration:**
    - Investigated the `sites-available` folder in the `/etc/apache2/` directory.
    - Confirmed the web server was serving content from `/var/www/html/`.

3. **Used strace to trace system calls:**
    - In one terminal, ran `strace` on the PID of the `root` Apache process.
    - In another terminal, sent a `curl` request to the server. `strace` did not provide useful information.

4. **Repeated strace on the `www-data` process:**
    - Ran `strace` on the PID of the `www-data` process and sent another `curl` request.
    - This time, `strace` revealed an `-1 ENOENT (No such file or directory)` error when attempting to access `/var/www/html/wp-includes/class-wp-locale.phpp`.

5. **Identified the typo:**
    - Searched through files in `/var/www/html/` using Vim pattern matching to locate the erroneous `.phpp` file extension.
    - Found the typo in `wp-settings.php` (Line 137: `require_once( ABSPATH . WPINC . '/class-wp-locale.php' );`).

6. **Corrected the typo:**
    - Removed the trailing `p` from `class-wp-locale.phpp` to correct it to `class-wp-locale.php`.

7. **Tested the fix:**
    - Sent another `curl` request to the server, which returned a 200 OK status.

8. **Automated the fix:**
    - Wrote a Puppet manifest to automate the correction of this specific error.

## Summary

The issue was caused by a simple typo in the WordPress `wp-settings.php` file, where `class-wp-locale.phpp` should have been `class-wp-locale.php`. The patch involved correcting this typo.

## Prevention

To prevent similar issues in the future:

- **Test thoroughly:** Ensure comprehensive testing of applications before deployment to catch such errors early.
- **Monitor status:** Implement an uptime-monitoring service like [UptimeRobot](https://uptimerobot.com/) for instant outage alerts.

In response to this incident, I created a Puppet manifest, [0-strace_is_your_friend.pp](https://github.com/glovic/alx-system_engineering-devops/blob/master/0x17-web_stack_debugging_3/0-strace_is_your_friend.pp), which automates the correction of any such typos in the `wp-settings.php` file.

But of course, it will never occur again, because we're programmers, and we never make errors!
