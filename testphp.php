<?php
function registerdevice() {
    $current_user = wp_get_current_user();
    if (empty($current_user)) {
        echo "Have a good day!";
    } else {
        $body = array(
            'id' => $current_user->display_name
        );
        $args = array(
            'body' => $body,
            'timeout' => '5',
            'redirection' => '5',
            'httpversion' => '1.0',
            'blocking' => true,
            'headers' => array(),
        $response = wp_remote_post( 'https://switch-hub.local:80/account', $args );
        echo "did it";
}



}
?>