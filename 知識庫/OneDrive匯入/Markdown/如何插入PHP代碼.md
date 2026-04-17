#Markdown #PHP
如果你想在 <mark style="background: #BBFABBA6;">Markdown</mark> 文件中插入 <mark style="background: #FFB86CA6;">PHP</mark> 語法並使其顯示為程式碼區塊，你可以使用 **區塊程式碼** 的語法，並標註語言為 `php`。這樣，大多數支持語法高亮顯示的 Markdown 渲染器（如 <mark style="background: #FFF3A3A6;">GitHub</mark> 或 GitLab）會自動識別並對 PHP 進行<mark style="background: #FFB8EBA6;">高亮顯示</mark>。

### 插入 PHP 語法的 Markdown 寫法：

````markdown
```php
<?php
echo "Hello, World!";
?>
````

````

### 說明：
1. 使用三個重音符號（```` ``` ````）包裹你的 PHP 代碼。
2. 在第一行的三個重音符號後面加上 `php`，這樣渲染器就會知道你要插入的是 PHP 代碼，並根據語言高亮來顯示。

### 示例效果：
```php
<?php
echo "Hello, World!";
?>
````

這樣的標註可以讓你的 PHP 代碼在支持 Markdown 語法高亮的編輯器或平台上清晰可讀。如果你只需要展示 PHP 代碼並且不需要語法高亮，則可以簡單地使用普通的程式碼區塊：

這樣會顯示為純文本的 PHP 代碼，而不會有語法高亮。