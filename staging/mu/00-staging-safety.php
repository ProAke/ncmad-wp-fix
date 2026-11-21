<?php
/**
 * Plugin Name: Local Staging Mail Block
 * Description: Prevents wp_mail() from sending messages in the local rehearsal.
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

add_filter( 'pre_wp_mail', '__return_false', PHP_INT_MAX );
