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

		extract($args);

		$title          = apply_filters( 'widget_title', $instance['title'] );
		$flickr_id      = (isset($instance['flickr_id']) && !empty($instance['flickr_id'])) ? esc_attr($instance['flickr_id']) : "";
		$photos_number  = (isset($instance['photos_number']) && is_numeric($instance['photos_number'])) ? esc_attr($instance['photos_number']) : 1;

		echo $before_widget;
		
			if ( ! empty( $title ) ){echo $before_title . $title . $after_title;}

			if (!empty($flickr_id)) {

				$api_key = 'your_own_api_key';

				$transient_prefix = esc_attr($flickr_id.$api_key);

				if ( false === ( $responce_results = get_transient( 'flickr-widget-' . $transient_prefix) ) ) {

					$url = 'https://www.flickr.com/services/rest/';

					$arguments = array(
						'api_key' => $api_key,
						'method'  => 'flickr.people.getPublicPhotos',
						'format'  => 'json',
						'user_id' => $flickr_id,
	                	'per_page'=> $photos_number,
					);

					$url_parameters = array();
		            foreach ($arguments as $key => $value){
		                $url_parameters[] = $key.'='.$value;
		            }

					$url .= '?'.implode('&', $url_parameters);

					$responce = file_get_contents($url);

					if ($responce) {

						$responce = str_replace('jsonFlickrApi(', '', $responce);
						$responce = str_replace('})', '}', $responce);
						$responce = json_decode($responce,true);

						$responce_results = array();

						if ($responce['stat'] == 'ok') {
							foreach ($responce['photos']['photo'] as $photo) {
								$responce_results[$photo['id']]['link'] = esc_url('//flickr.com/photos/'.$photo["owner"].'/'.$photo["id"]);
								$responce_results[$photo['id']]['url']  = esc_url('//farm'.$photo["farm"].'.staticflickr.com/'.$photo["server"].'/'.$photo["id"].'_'.$photo["secret"].'_s.jpg');
								$responce_results[$photo['id']]['alt']  = esc_attr($photo["title"]);
							}

			                if ( ! empty( $responce_results ) ) {
			                	$responce_results = base64_encode( serialize( $responce_results ) );
			                    set_transient( 'flickr-widget-' . $transient_prefix, $responce_results, apply_filters( 'null_flickr_cache_time', HOUR_IN_SECONDS * 2 ) );
			                }

						}

					} else {
						return new WP_Error( 'flickr_error', esc_html__('Could not get data', 'your-text-domain') );
					}

				}

				if (!empty($responce_results)) {
					$responce_results =  unserialize( base64_decode( $responce_results ) );
					wp_enqueue_style('widget-flickr');
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