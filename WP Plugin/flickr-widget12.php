<?php
/*
    Plugin Name: Flickr widget
    Plugin URI: http://www.enovathemes.com
    Description: Display recent Flickr images
    Author: Enovathemes
    Version: 1.0
    Author URI: http://enovathemes.com
*/
if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

function register_script(){
	wp_register_style('widget-flickr', plugins_url('/widget-flickr.css', __FILE__ ));
}
add_action( 'wp_enqueue_scripts', 'register_script' );

add_action('widgets_init', 'register_flickr_widget');
function register_flickr_widget(){
	register_widget( 'WP_Widget_Flickr' );
}

class  WP_Widget_Flickr extends WP_Widget {

	public function __construct() {
		parent::__construct(
			'flickr',
			esc_html__('* Photos from flickr', 'your-text-domain'),
			array( 'description' => esc_html__('Display photos from flickr', 'your-text-domain'))
		);
	}

	public function widget( $args, $instance ) {


		echo $before_widget;
		
			if ( ! empty( $title ) ){echo $before_title . $title . $after_title;}



				$api_key = 'your_own_api_key';

				$transient_prefix = esc_attr($flickr_id.$api_key);

				if ( false === ( $responce_results = get_transient( 'flickr-widget-' . $transient_prefix) ) ) {

					$url = 'https://www.flickr.com/services/rest/';





					$url .= '?'.implode('&', $url_parameters);

					$responce = file_get_contents($url);

					if ($responce) {

						$responce = str_replace('jsonFlickrApi(', '', $responce);
						$responce = str_replace('})', '}', $responce);
						$responce = json_decode($responce,true);

						$responce_results = array();



				}

				if (!empty($responce_results)) {
					$responce_results =  unserialize( base64_decode( $responce_results ) );

					$output = '';
					$output .= '<ul class="widget-flickr-list">';
						foreach ($responce_results as $photo) {
							$output .= '<li>';
								$output .= '<a href="'.$photo['link'].'" target="_blank">';
									$output .= '<img src="'.$photo['url'].'" alt="'.$photo['alt'].'" />';
								$output .= '</a>';
							$output .= '</li>';
						}
					$output .= '</ul>';
					echo $output;
				}

			}

		echo $after_widget;
	}

 	public function form( $instance ) {

 		$defaults = array(
 			'title'          => esc_html__('Photos from flickr', 'your-text-domain'),
 			'photos_number'  => '1',
 			'flickr_id'      => '',
 		);

 		$instance = wp_parse_args((array) $instance, $defaults);

		?>
		<p>
			<label for="<?php echo $this->get_field_id( 'title' ); ?>"><?php echo esc_html__( 'Title:', 'your-text-domain' ); ?></label> 
			<input class="widefat" id="<?php echo $this->get_field_id( 'title' ); ?>" name="<?php echo $this->get_field_name( 'title' ); ?>" type="text" value="<?php echo esc_attr($instance['title']); ?>" />
		</p>
		<p>
			<label for="<?php echo $this->get_field_id( 'flickr_id' ); ?>"><?php echo esc_html__( 'Flickr id:', 'your-text-domain' ); ?></label> 
			<input class="widefat" id="<?php echo $this->get_field_id( 'flickr_id' ); ?>" name="<?php echo $this->get_field_name( 'flickr_id' ); ?>" type="text" value="<?php echo $instance['flickr_id']; ?>" />
		</p>
		<p>
			<label for="<?php echo $this->get_field_id( 'photos_number' ); ?>"><?php echo esc_html__( 'Number of photos to show:', 'your-text-domain' ); ?></label> 
			<input class="widefat" id="<?php echo $this->get_field_id( 'photos_number' ); ?>" name="<?php echo $this->get_field_name( 'photos_number' ); ?>" type="text" value="<?php echo $instance['photos_number']; ?>" size="3" />
		</p>
		<?php
	}

	public function update( $new_instance, $old_instance ) {
		$instance = $old_instance;
		$instance['title']          = strip_tags( $new_instance['title'] );
		$instance['photos_number']  = strip_tags( $new_instance['photos_number'] );
		$instance['flickr_id']      = strip_tags( $new_instance['flickr_id'] );

		$api_key        = 'your_own_api_key';
		$transient_name = 'flickr-widget-'.esc_attr($instance['flickr_id'].$api_key);

		delete_transient($transient_name);

		return $instance;
	}
}
?>