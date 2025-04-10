<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/documentation/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress' );

/** Database username */
define( 'DB_USER', 'root' );

/** Database password */
define( 'DB_PASSWORD', 'lamp.sh' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         '?HI~$7a0sn[(C=+kmx=JDV63[]sOnqKx|G51mk5f$igT~/NjljMgA#L dR]YUa z' );
define( 'SECURE_AUTH_KEY',  'VHqhArawbk GIa?/yw@5wKL8^n;X#1[~dx7ip/8d,CTMoowa7I>D>t]%,@V+Dff8' );
define( 'LOGGED_IN_KEY',    'N~l1*HAb~|6UV;]pkI./Tu11Z8$}1a{ZH0p2.z%221w]{vj<g?ELvb+qgWp u>r6' );
define( 'NONCE_KEY',        'Wu/sg/)nHQJ|sggXMb(@<,;NCc[AcMlL!5}p_N;fqmr-$Tt1Ex6x:(%T{{Ht&!Re' );
define( 'AUTH_SALT',        'zi$l=XQKDA0hF8Q4c(2]o_kU:!lz?;xuQkU3zB#8DnLZ6CUW:HX@%0FsG6=IRSZE' );
define( 'SECURE_AUTH_SALT', 'tiycIlY-:(Y)6I ayw2t/<#<RWUm6/,DsbY*;!ykNtT!B4|YM&($ u2X)mi.`r8z' );
define( 'LOGGED_IN_SALT',   '(kn%uPE>Up5}ehVO~}qG>]zfHO`oE[vdXzLi.N{)UlKcQ]cr/Vy*yisutrsJZ<&T' );
define( 'NONCE_SALT',       '6rzz2K[ztP}6KM ?5,c2S&)M!y;.}b6M/g{iOzO|sy;0.ePu ><z[v_0aHh$HD%}' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/documentation/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
