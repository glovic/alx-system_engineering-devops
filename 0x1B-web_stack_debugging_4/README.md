# Web Stack Debugging #4

This project is the fifth in a series of web stack debugging projects. The objective is to identify and fix issues within isolated containers running web stacks. For each task, a script was created to automate the necessary commands to resolve the problems and bring the web stack to a working state.

## Tasks

### Task 0: Sky is the Limit, Let's Bring That Limit Higher

**File:** `0-the_sky_is_the_limit_not.pp`

**Description:**
This Puppet manifest increases the amount of traffic an Apache web server can handle. It does so by adjusting the `MaxRequestWorkers` directive in the Apache configuration to allow for more concurrent requests.

**Implementation:**
- Creates a configuration file `/etc/apache2/conf-available/limit.conf` with the `MaxRequestWorkers` set to 512.
- Enables the new configuration using `a2enconf`.
- Restarts the Apache service to apply the changes.

### Task 1: User Limit

**File:** `1-user_limit.pp`

**Description:**
This Puppet manifest adjusts the operating system configuration to ensure that the user `holberton` can log in and open files without encountering errors related to system limits.

**Implementation:**
- Updates `/etc/security/limits.conf` to set user-specific limits for `holberton`:
  - Soft limit for open files (`nofile`) set to 4096.
  - Hard limit for open files (`nofile`) set to 8192.
  - Soft limit for processes (`nproc`) set to 4096.
  - Hard limit for processes (`nproc`) set to 8192.

## Usage

1. **Increase Apache Traffic Handling Capacity:**
   - Apply the Puppet manifest `0-the_sky_is_the_limit_not.pp` to adjust Apache settings.
   - Ensure that the Apache service restarts to apply the new configuration.

   ```sh
   puppet apply 0-the_sky_is_the_limit_not.pp
   ```

2. **Adjust User Limits:**
   - Apply the Puppet manifest `1-user_limit.pp` to update user-specific limits in the system configuration.

   ```sh
   puppet apply 1-user_limit.pp
   ```

By using these manifests, the web stack can handle more concurrent requests, and the specified user can operate without hitting system limitations, thus improving overall system performance and usability.
