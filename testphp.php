<?php
function registerdevice() {
    $current_user = wp_get_current_user();

    $response = wp_remote_get( 'https://switch-hub.local:80/account');
    $json = json_decode( $response['body'] );
    return $json;
}



}

function cc_widget_logic( $display_logic ) {
    $current_user = wp_get_current_user();
    $response = wp_remote_get( 'https://switch-hub.local:80/account');
    $json = json_decode( $response['body'] );
	if (username_exists( $response.id ) ) {
		//Show widget with logic
		$display_logic .= false;
	} else {
		//Hide widget with logic
		$display_logic = true;
	}
return $display_logic;
}
add_filter( 'widget_options_logic_override', 'cc_widget_logic', 30, 1 );
?>